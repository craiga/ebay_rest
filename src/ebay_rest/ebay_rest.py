""" A tread-safe Python 3 pip package that conveniently wraps eBay’s REST APIs. """
# Standard library imports
from datetime import datetime, timedelta, timezone
import json
import logging
import os
import threading
import time

# Third party imports

# Local imports
from oath.credentialutil import credentialutil
from oath.model.model import environment
from oath.oauth2api import oauth2api

# Don't editing the anchors or in-between; modify the process_swagger_cache.py code generator.
# ANCHOR-er_imports-START"
import api.buy_browse as buy_browse
from api.buy_browse.rest import ApiException as BuyBrowseException
import api.buy_deal as buy_deal
from api.buy_deal.rest import ApiException as BuyDealException
import api.buy_feed as buy_feed
from api.buy_feed.rest import ApiException as BuyFeedException
import api.buy_marketing as buy_marketing
from api.buy_marketing.rest import ApiException as BuyMarketingException
import api.buy_marketplace_insights as buy_marketplace_insights
from api.buy_marketplace_insights.rest import ApiException as BuyMarketplaceInsightsException
import api.buy_offer as buy_offer
from api.buy_offer.rest import ApiException as BuyOfferException
import api.buy_order as buy_order
from api.buy_order.rest import ApiException as BuyOrderException
import api.commerce_catalog as commerce_catalog
from api.commerce_catalog.rest import ApiException as CommerceCatalogException
import api.commerce_charity as commerce_charity
from api.commerce_charity.rest import ApiException as CommerceCharityException
import api.commerce_identity as commerce_identity
from api.commerce_identity.rest import ApiException as CommerceIdentityException
import api.commerce_notification as commerce_notification
from api.commerce_notification.rest import ApiException as CommerceNotificationException
import api.commerce_taxonomy as commerce_taxonomy
from api.commerce_taxonomy.rest import ApiException as CommerceTaxonomyException
import api.commerce_translation as commerce_translation
from api.commerce_translation.rest import ApiException as CommerceTranslationException
import api.developer_analytics as developer_analytics
from api.developer_analytics.rest import ApiException as DeveloperAnalyticsException
import api.sell_account as sell_account
from api.sell_account.rest import ApiException as SellAccountException
import api.sell_analytics as sell_analytics
from api.sell_analytics.rest import ApiException as SellAnalyticsException
import api.sell_compliance as sell_compliance
from api.sell_compliance.rest import ApiException as SellComplianceException
import api.sell_feed as sell_feed
from api.sell_feed.rest import ApiException as SellFeedException
import api.sell_finances as sell_finances
from api.sell_finances.rest import ApiException as SellFinancesException
import api.sell_fulfillment as sell_fulfillment
from api.sell_fulfillment.rest import ApiException as SellFulfillmentException
import api.sell_inventory as sell_inventory
from api.sell_inventory.rest import ApiException as SellInventoryException
import api.sell_listing as sell_listing
from api.sell_listing.rest import ApiException as SellListingException
import api.sell_logistics as sell_logistics
from api.sell_logistics.rest import ApiException as SellLogisticsException
import api.sell_marketing as sell_marketing
from api.sell_marketing.rest import ApiException as SellMarketingException
import api.sell_metadata as sell_metadata
from api.sell_metadata.rest import ApiException as SellMetadataException
import api.sell_negotiation as sell_negotiation
from api.sell_negotiation.rest import ApiException as SellNegotiationException
import api.sell_recommendation as sell_recommendation
from api.sell_recommendation.rest import ApiException as SellRecommendationException
# ANCHOR-er_imports-END"

# Constants
EBAY_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"

# Globals

# Pertaining to launching threads once and only once.
# Are global because class variables are immutable in __init__.
_launch_lock = threading.Lock()
_launched = False
_rates_thread = None


class EbayDateTime:
    """ Helpers for the specific way that eBay does date-time. """

    @staticmethod
    def now():
        """ get the current time, as a python datetime object with eBay's timezone and precision
        Date-time values are in the ISO 8601 date and time format.
        Hours are in 24-hour format (e.g., 2:00:00pm is 14:00:00).
        Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT),
        also known as Zulu because the time portion of the time stamp ends with a Z """

        # TODO Precisely synchronize with eBay's clock.
        # https://ofr.ebay.ca/ws/eBayISAPI.dll?EbayTime  (only accurate to the second)
        # https://developer.ebay.com/Devzone/shopping/docs/CallRef/GeteBayTime.html
        # (not a REST-ful call, old SOAP)

        d_t = datetime.utcnow()
        excess_precision = timedelta(0, 0, d_t.microsecond - round(d_t.microsecond, -3))
        return d_t.replace(tzinfo=timezone.utc) - excess_precision

    @staticmethod
    def to_string(date_time):
        """ convert a python datetime object with eBay's timezone to an Ebay dateTime string
        string YYYY-MM-DDTHH:MM:SS.SSSZ (e.g., 2004-08-04T19:09:02.768Z) """
        string = date_time.strftime(EBAY_DATE_FORMAT)
        return string[0:10] + 'T' + string[11:23] + 'Z'

    @staticmethod
    def from_string(date_time_string):
        """ convert an Ebay dateTime string string to a python datetime object with eBay's timezone
        string YYYY-MM-DDTHH:MM:SS.SSSZ (e.g., 2004-08-04T19:09:02.768Z) """
        d_t = datetime.strptime(date_time_string, EBAY_DATE_FORMAT)
        return d_t.replace(tzinfo=timezone.utc)


class EbayRestError(Exception):
    """ Use to return all exceptions from this module. """

    def __init__(self, number, message):
        super().__init__()
        self.number = number
        self.message = message

    def __str__(self):
        return f'Error {self.number} is {self.message}.'


class _Singleton:   # pylint: disable=too-few-public-methods
    """ An abstract base class used to make Singletons. The singleton software design pattern
    restricts the instantiation of a class to one "single" instance. This is useful when exactly
    one object is needed to coordinate actions across the system.
    """
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(_Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]


# TODO If init parameters repeat then use a singleton to conserve resources.
# class EbayRest(_Singleton):
class EbayRest:
    """ A wrapper for eBay's APIs. """

    # Pertaining to eBay Application Token maintenance.
    _oauth2api_inst = None
    _token_lock = threading.Lock()
    _app_token = None               # use when locked
    _token_initialized = False      # use when locked

    def __init__(self, my_string):
        self.my_string = my_string
        self.use_sandbox = False
        self.site_id = 'EBAY-ENCA'  # strings ie. 'EBAY-ENCA' and numbers ie. 101 work
        self._containers = None
        self._enums = None

        global _launch_lock, _launched, _rates_thread
        with _launch_lock:
            if not _launched:
                threading.Thread(target=self._refresh_token_worker, daemon=True).start()
                # _rates_thread =  /
                # threading.Thread(target=self._developer_analytics_worker, daemon=True).start()
                _launched = True

    def print(self):
        """ Print the string that is supplied to the constructor. """
        print(self.my_string)

    @staticmethod
    def will_fail():
        """ Demonstrate what happens when a method call fails. """
        raise EbayRestError(0, "Sample error.")

    def get_containers(self):
        """ Get eBay container information. """
        # if the data needs caching
        if self._containers is None:
            # get the path to this python file, which is also where the data file is
            path, _fn = os.path.split(os.path.realpath(__file__))
            # to the path join the data file name and extension
            path_name = os.path.join(path, 'containers.json')
            with open(path_name) as file_handle:
                self._containers = json.load(file_handle)
        return self._containers

    def get_enums(self):
        """ Get eBay enumeration information. """
        # if the data needs caching
        if self._enums is None:
            # get the path to this python file, which is also where the data file is
            path, _fn = os.path.split(os.path.realpath(__file__))
            # to the path join the data file name and extension
            path_name = os.path.join(path, 'enums.json')
            with open(path_name) as file_handle:
                self._enums = json.load(file_handle)
        return self._enums

    @staticmethod
    def true():
        """ Always return true. """
        return True

    def developer_analytics_get_rate_limits(self):
        """ Refresh the local Developer Analytics values. """

        # Configure OAuth2 access token for authorization: api_auth
        configuration = developer_analytics.Configuration()
        configuration.access_token = self._get_token()

        # Configure the host endpoint
        # if the generated client library has a flawed host, then compensate
        if '{basePath}' in configuration.host:
            configuration.host = configuration.host.replace('{basePath}',
                                                            '/developer/analytics/v1_beta')
        if self.use_sandbox:
            configuration.host = configuration.host.replace('api.ebay.com',
                                                            'api.sandbox.ebay.com')

        # create an instance of the API class
        api_instance = \
            developer_analytics.RateLimitApi(developer_analytics.ApiClient(configuration))
        api_instance.api_client.default_headers['X-EBAY-C-MARKETPLACE-ID'] = self.site_id

        # str | This optional parameter filters the result to include only the specified context.
        # Acceptable values for the parameter are buy, sell, commerce, and developer. (optional)
        api_context = 'buy'

        # str | This optional query parameter filters the result to include only the APIs specified.
        # Example values are browse for the Buy APIs context, inventory for the Sell APIs context,
        # and taxonomy for the Commerce APIs context. (optional)
        # api_name = ''

        result = None
        try:
            api_response = api_instance.get_rate_limits(
                api_context=api_context,
                # api_name=api_name
            )

        except DeveloperAnalyticsException as error:
            logging.critical(f"APIException status {error.status},"
                             f" reason {error.reason},"
                             f" body{error.body}.")

        else:
            result = api_response

        return result

    def _refresh_token(self):
        """ Get a new eBay Application Token. """

        if self.use_sandbox:
            env = environment.SANDBOX
        else:
            env = environment.PRODUCTION
        # self._throttle()
        app_token = \
            self._oauth2api_inst.get_application_token(env,
                                                       ["https://api.ebay.com/oauth/api_scope"])
        if app_token.error is not None:
            logging.critical(f'app_token.error == {app_token.error}.')
        if (app_token.access_token is None) or (len(app_token.access_token) == 0):
            logging.critical('app_token.access_token is missing.')

        with self._token_lock:
            self._app_token = app_token

    def _refresh_token_worker(self):
        """ Before expiry, get a new eBay Application Token. """

        logging.debug('The refresh token worker started.')

        directory = os.getcwd()     # get the current working directory
        credentialutil.load(os.path.join(directory, 'ebay.yaml'))
        self._oauth2api_inst = oauth2api()
        self._refresh_token()
        with self._token_lock:
            self._token_initialized = True

        while True:  # TODO break out of this when the program is gracefully exited.
            with self._token_lock:
                expiry = self._app_token.token_expiry
            wait = expiry.replace(tzinfo=timezone.utc) - EbayDateTime.now()
            seconds = float(wait.seconds) + float(wait.microseconds) / 1000000
            seconds -= 60  # don't be late, so refresh a number of seconds before required
            if seconds > 0:
                time.sleep(seconds)
            self._refresh_token()

    def _get_token(self):
        """ Get the eBay Application Token. """

        self._token_lock.acquire()
        while not self._token_initialized:
            self._token_lock.release()
            time.sleep(0.1)
            self._token_lock.acquire()
        token = self._app_token.access_token
        self._token_lock.release()
        return token
