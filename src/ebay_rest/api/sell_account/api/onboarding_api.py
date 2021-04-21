# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (the Fulfillment Policy, Payment Policy, and Return Policy), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br><br>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.6.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ...sell_account.api_client import ApiClient


class OnboardingApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_payments_program_onboarding(self, marketplace_id, payments_program_type, **kwargs):  # noqa: E501
        """get_payments_program_onboarding  # noqa: E501

        This method retrieves a seller's onboarding status of eBay managed payments for a specified marketplace. The overall onboarding status of the seller and the status of each onboarding step is returned. Presently, the only supported payments program type is EBAY_PAYMENTS. See Managed Payments on eBay and Payments Terms of Use. Note: Managed payments availability: eBay managed payments is presently available in the US and Germany, and will roll out to Canada, UK, and Australia in July 2020.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payments_program_onboarding(marketplace_id, payments_program_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str marketplace_id: The eBay marketplace ID associated with the onboarding status to retrieve. Only enums for marketplaces that support or will soon support eBay managed payments are allowed. Error 20408 is returned for any other eBay marketplace. No response payload is returned with this error. (required)
        :param str payments_program_type: The type of payments program whose status is returned by the call. Presently, the only supported payments program is EBAY_PAYMENTS. For details on the program, see Payments Terms of Use. (required)
        :return: PaymentsProgramOnboardingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_payments_program_onboarding_with_http_info(marketplace_id, payments_program_type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_payments_program_onboarding_with_http_info(marketplace_id, payments_program_type, **kwargs)  # noqa: E501
            return data

    def get_payments_program_onboarding_with_http_info(self, marketplace_id, payments_program_type, **kwargs):  # noqa: E501
        """get_payments_program_onboarding  # noqa: E501

        This method retrieves a seller's onboarding status of eBay managed payments for a specified marketplace. The overall onboarding status of the seller and the status of each onboarding step is returned. Presently, the only supported payments program type is EBAY_PAYMENTS. See Managed Payments on eBay and Payments Terms of Use. Note: Managed payments availability: eBay managed payments is presently available in the US and Germany, and will roll out to Canada, UK, and Australia in July 2020.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payments_program_onboarding_with_http_info(marketplace_id, payments_program_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str marketplace_id: The eBay marketplace ID associated with the onboarding status to retrieve. Only enums for marketplaces that support or will soon support eBay managed payments are allowed. Error 20408 is returned for any other eBay marketplace. No response payload is returned with this error. (required)
        :param str payments_program_type: The type of payments program whose status is returned by the call. Presently, the only supported payments program is EBAY_PAYMENTS. For details on the program, see Payments Terms of Use. (required)
        :return: PaymentsProgramOnboardingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['marketplace_id', 'payments_program_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payments_program_onboarding" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'marketplace_id' is set
        if ('marketplace_id' not in params or
                params['marketplace_id'] is None):
            raise ValueError("Missing the required parameter `marketplace_id` when calling `get_payments_program_onboarding`")  # noqa: E501
        # verify the required parameter 'payments_program_type' is set
        if ('payments_program_type' not in params or
                params['payments_program_type'] is None):
            raise ValueError("Missing the required parameter `payments_program_type` when calling `get_payments_program_onboarding`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'marketplace_id' in params:
            path_params['marketplace_id'] = params['marketplace_id']  # noqa: E501
        if 'payments_program_type' in params:
            path_params['payments_program_type'] = params['payments_program_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/payments_program/{marketplace_id}/{payments_program_type}/onboarding', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaymentsProgramOnboardingResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
