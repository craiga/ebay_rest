# coding: utf-8

"""
    Marketing API

    <p>The <i>Marketing API </i> offers two platforms that sellers can use to promote and advertise their products:</p> <ul><li><b>Promoted Listings</b> is an eBay ad service that lets sellers set up <i>ad campaigns </i> for the products they want to promote. eBay displays the ads in search results and in other marketing modules as <b>SPONSORED</b> listings. If an item in a Promoted Listings campaign sells, the seller is assessed a Promoted Listings fee, which is a seller-specified percentage applied to the sales price. For complete details, see <a href=\"/api-docs/sell/static/marketing/promoted-listings.html\">Promoted Listings</a>.</li>  <li><b>Promotions Manager</b> gives sellers a way to offer discounts on specific items as a way to attract buyers to their inventory. Sellers can set up discounts (such as \"20% off\" and other types of offers) on specific items or on an entire customer order. To further attract buyers, eBay prominently displays promotion <i>teasers</i> throughout buyer flows. For complete details, see <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\">Promotions Manager</a>.</li></ul>  <p><b>Marketing reports</b>, on both the Promoted Listings and Promotions Manager platforms, give sellers information that shows the effectiveness of their marketing strategies. The data gives sellers the ability to review and fine tune their marketing efforts.</p> <p class=\"tablenote\"><b>Important!</b> Sellers must have an active eBay Store subscription, and they must accept the <b>Terms and Conditions</b> before they can make requests to these APIs in the Production environment. There are also site-specific listings requirements and restrictions associated with these marketing tools, as listed in the \"requirements and restrictions\" sections for <a href=\"/api-docs/sell/marketing/static/overview.html#PL-requirements\">Promoted Listings</a> and <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager</a>.</p> <p>The table below lists all the Marketing API calls grouped by resource.</p>  # noqa: E501

    OpenAPI spec version: v1.10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ...sell_marketing.api_client import ApiClient


class PromotionReportApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_promotion_reports(self, marketplace_id, **kwargs):  # noqa: E501
        """get_promotion_reports  # noqa: E501

        This method generates a report that lists the seller's running, paused, and ended promotions for the specified eBay marketplace. The result set can be filtered by the promotion status and the number of results to return. You can also supply keywords to limit the report to promotions that contain the specified keywords. Specify the eBay marketplace for which you want the report run using the marketplace_id query parameter. Supply additional query parameters to control the report as needed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_promotion_reports(marketplace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str marketplace_id: The eBay marketplace ID of the site for which you want the promotions report. Valid values: EBAY_AU = Australia EBAY_DE = Germany EBAY_ES = Spain EBAY_FR = France EBAY_GB = Great Britain EBAY_IT = Italy EBAY_US = United States (required)
        :param str limit: Specifies the maximum number of promotions returned on a page from the result set. Default: 200 Maximum: 200
        :param str offset: Specifies the number of promotions to skip in the result set before returning the first promotion in the paginated response. Combine offset with the limit query parameter to control the items returned in the response. For example, if you supply an offset of 0 and a limit of 10, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If offset is 10 and limit is 20, the first page of the response contains items 11-30 from the complete result set. Default: 0
        :param str promotion_status: Limits the results to the promotions that are in the state specified by this query parameter. Valid values: DRAFT SCHEDULED RUNNING PAUSED ENDEDMaximum number of values supported: 1
        :param str promotion_type: Filters the returned promotions in the report based on their campaign promotion type. Specify one of the following values to indicate the promotion type you want returned in the report: CODED_COUPON &ndash; A coupon code promotion set with createItemPromotion. MARKDOWN_SALE &ndash; A markdown promotion set with createItemPriceMarkdownPromotion. ORDER_DISCOUNT &ndash; A threshold promotion set with createItemPromotion. VOLUME_DISCOUNT &ndash; A volume pricing promotion set with createItemPromotion.
        :param str q: A string consisting of one or more keywords. eBay filters the response by returning only the promotions that contain the supplied keywords in the promotion title. Example: &quot;iPhone&quot; or &quot;Harry Potter.&quot; Commas that separate keywords are ignored. For example, a keyword string of &quot;iPhone, iPad&quot; equals &quot;iPhone iPad&quot;, and each results in a response that contains promotions with both &quot;iPhone&quot; and &quot;iPad&quot; in the title.
        :return: PromotionsReportPagedCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_promotion_reports_with_http_info(marketplace_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_promotion_reports_with_http_info(marketplace_id, **kwargs)  # noqa: E501
            return data

    def get_promotion_reports_with_http_info(self, marketplace_id, **kwargs):  # noqa: E501
        """get_promotion_reports  # noqa: E501

        This method generates a report that lists the seller's running, paused, and ended promotions for the specified eBay marketplace. The result set can be filtered by the promotion status and the number of results to return. You can also supply keywords to limit the report to promotions that contain the specified keywords. Specify the eBay marketplace for which you want the report run using the marketplace_id query parameter. Supply additional query parameters to control the report as needed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_promotion_reports_with_http_info(marketplace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str marketplace_id: The eBay marketplace ID of the site for which you want the promotions report. Valid values: EBAY_AU = Australia EBAY_DE = Germany EBAY_ES = Spain EBAY_FR = France EBAY_GB = Great Britain EBAY_IT = Italy EBAY_US = United States (required)
        :param str limit: Specifies the maximum number of promotions returned on a page from the result set. Default: 200 Maximum: 200
        :param str offset: Specifies the number of promotions to skip in the result set before returning the first promotion in the paginated response. Combine offset with the limit query parameter to control the items returned in the response. For example, if you supply an offset of 0 and a limit of 10, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If offset is 10 and limit is 20, the first page of the response contains items 11-30 from the complete result set. Default: 0
        :param str promotion_status: Limits the results to the promotions that are in the state specified by this query parameter. Valid values: DRAFT SCHEDULED RUNNING PAUSED ENDEDMaximum number of values supported: 1
        :param str promotion_type: Filters the returned promotions in the report based on their campaign promotion type. Specify one of the following values to indicate the promotion type you want returned in the report: CODED_COUPON &ndash; A coupon code promotion set with createItemPromotion. MARKDOWN_SALE &ndash; A markdown promotion set with createItemPriceMarkdownPromotion. ORDER_DISCOUNT &ndash; A threshold promotion set with createItemPromotion. VOLUME_DISCOUNT &ndash; A volume pricing promotion set with createItemPromotion.
        :param str q: A string consisting of one or more keywords. eBay filters the response by returning only the promotions that contain the supplied keywords in the promotion title. Example: &quot;iPhone&quot; or &quot;Harry Potter.&quot; Commas that separate keywords are ignored. For example, a keyword string of &quot;iPhone, iPad&quot; equals &quot;iPhone iPad&quot;, and each results in a response that contains promotions with both &quot;iPhone&quot; and &quot;iPad&quot; in the title.
        :return: PromotionsReportPagedCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['marketplace_id', 'limit', 'offset', 'promotion_status', 'promotion_type', 'q']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_promotion_reports" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'marketplace_id' is set
        if ('marketplace_id' not in params or
                params['marketplace_id'] is None):
            raise ValueError("Missing the required parameter `marketplace_id` when calling `get_promotion_reports`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'marketplace_id' in params:
            query_params.append(('marketplace_id', params['marketplace_id']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'promotion_status' in params:
            query_params.append(('promotion_status', params['promotion_status']))  # noqa: E501
        if 'promotion_type' in params:
            query_params.append(('promotion_type', params['promotion_type']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501

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
            '/promotion_report', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PromotionsReportPagedCollection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
