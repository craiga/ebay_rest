# coding: utf-8

"""
    Item Feed Service

    The Feed API provides the ability to download TSV_GZIP feed files containing eBay items and an hourly snapshot file of the items that have changed within an hour for a specific category, date and marketplace. <p>In addition to the API, there is an open source <a href=\"https://github.com/eBay/FeedSDK\" target=\"_blank\">Feed SDK</a> written in Java that downloads, combines files into a single file when needed, and unzips the entire feed file. It also lets you specify field filters to curate the items in the file.</p>  # noqa: E501

    OpenAPI spec version: v1_beta.25.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ...buy_feed.api_client import ApiClient


class ItemGroupApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_item_group_feed(self, x_ebay_c_marketplace_id, feed_scope, category_id, **kwargs):  # noqa: E501
        """get_item_group_feed  # noqa: E501

        This method lets you download a TSV_GZIP (tab separated value gzip) Item Group feed file. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc. There are two types of item group feed files generated: A daily Item Group feed file containing the item group variation information associated with items returned in the Item feed file for a specific day, category, and marketplace. (feed_scope = NEWLY_LISTED) A weekly Item Group Bootstrap feed file containing all the item group variation information associated with items returned in the Item Bootstrap feed file for all the items in a specific category. (feed_scope = ALL_ACTIVE) Note: Filters are applied to the feed files. For details, see Feed File Filters. When curating the items returned, be sure to code as if these filters are not applied as they can be changed or removed in the future. The contents of these feed files are based on the contents of the corresponding daily Item or Item Bootstrap feed file. When a new Item or Item Bootstrap feed file is generated, the service reads the file and if an item in the file has a primaryItemGroupId value, which indicates the item is part of an item group, it uses that value to return the item group (parent item) information for that item in the corresponding Item Group or Item Group Bootstrap feed file. This information includes the name/value pair of the aspects of the items in this group returned in the variesByLocalizedAspects column. For example, if the item was a shirt some of the variation names could be Size, Color, etc. Also the images for the various aspects are returned in the additionalImageUrls column. The first line in any feed file is the header, which labels the columns and indicates the order of the values on each line. Each header is described in the Response fields section. Combining the Item Group and Item feed files The Item Group or Item Group Bootstrap feed file contains details about the item group (parent item), including the item group ID itemGroupId. You match the value of itemGroupId from the Item Group feed file with the value of primaryItemGroupId from the corresponding daily Item or Item Bootstrap feed file. URLs for this method Production URL: https://api.ebay.com/buy/feed/v1_beta/item_group? Sandbox URL: https://api.sandbox.ebay.com/buy/feed/v1_beta/item_group? Downloading feed files Item Group feed files are binary gzip files. If the file is larger than 100 MB, the download must be streamed in chunks. You specify the size of the chunks in bytes using the Range request header. The content-range response header indicates where in the full resource this partial chunk of data belongs and the total number of bytes in the file. For more information about using these headers, see Retrieving a gzip feed file. Note: The response is always only a TSV_GZIP file. However for documentation purposes, the response is shown as JSON fields so that the value returned in each column can be explained. The order of the response fields, shows you the order of the columns in the feed file. Restrictions For a list of supported sites and other restrictions, see API Restrictions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_item_group_feed(x_ebay_c_marketplace_id, feed_scope, category_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_ebay_c_marketplace_id: The ID of the eBay marketplace where the item is hosted. Note: This value is case sensitive. For example: &nbsp;&nbsp;X-EBAY-C-MARKETPLACE-ID = EBAY_US For a list of supported sites see, API Restrictions. (required)
        :param str feed_scope: Specifies the type of file to return. Valid Values: NEWLY_LISTED - Returns the Item Group feed file containing the item group variation information for items in the daily Item feed file that were associated with an item group. The items in this type of Item feed file are items that were listed on the day specified by the date parameter in the category specified by the category_id parameter. /item_group?feed_scope=NEWLY_LISTED&amp;category_id=15032&amp;date=20170925 ALL_ACTIVE - Returns the weekly Item Group Bootstrap file containing the item group variation information for items in the weekly Item Bootstrap feed file that were associated with an item group. The items are Good 'Til Cancelled items in the category specified by the category_id parameter. Note: Bootstrap files are generated every Tuesday and the file is available on Wednesday. However, the exact time the file is available can vary so we recommend you download the Bootstrap file on Thursday. The item groups in the file are for the items that were in the specified category on Sunday. /item_group?feed_scope=ALL_ACTIVE&amp;category_id=15032 (required)
        :param str category_id: An eBay top-level category ID of the items to be returned in the feed file. The list of eBay category IDs changes over time and category IDs are not the same across all the eBay marketplaces. To get a list of the top-level categories for a marketplaces, you can use the Taxonomy API getCategoryTree method. This method retrieves the complete category tree for the marketplace. The top-level categories are identified by the categoryTreeNodeLevel field. For example: &nbsp;&nbsp;&quot;categoryTreeNodeLevel&quot;: 1 For details see Get Categories for Buy APIs. Restriction: Must be a top-level category (required)
        :param str range: This header specifies the range in bytes of the chunks of the gzip file being returned. Format: bytes=startpos-endpos For example, the following retrieves the first 10 MBs of the feed file. &nbsp;&nbsp;Range bytes=0-10485760 For more information about using this headers, see Retrieving a gzip feed file. Maximum: 100 MB (10MB in the Sandbox)
        :param str _date: The date of the daily Item Group feed file (feed_scope=NEWLY_LISTED) you want. The date is required only for the daily Item Group feed file. If you specify a date for the Item Group Bootstrap file (feed_scope=ALL_ACTIVE), the date is ignored and the latest file is returned. The date the Item Group Bootstrap feed file was generated is returned in the Last-Modified response header. The Item Group feed files are generated every day and there are 14 daily files available. There is a 48 hour latency when generating the files. This means on July 10, the latest feed file you can download is July 8. Note: The generated files are stored using MST (US Mountain Standard Time), which is -7 hours UTC time. Format: yyyyMMdd Requirement: Requirements: Required only when feed_scope=NEWLY_LISTED Must be within 3-14 days in the past
        :return: ItemGroupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_item_group_feed_with_http_info(x_ebay_c_marketplace_id, feed_scope, category_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_item_group_feed_with_http_info(x_ebay_c_marketplace_id, feed_scope, category_id, **kwargs)  # noqa: E501
            return data

    def get_item_group_feed_with_http_info(self, x_ebay_c_marketplace_id, feed_scope, category_id, **kwargs):  # noqa: E501
        """get_item_group_feed  # noqa: E501

        This method lets you download a TSV_GZIP (tab separated value gzip) Item Group feed file. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc. There are two types of item group feed files generated: A daily Item Group feed file containing the item group variation information associated with items returned in the Item feed file for a specific day, category, and marketplace. (feed_scope = NEWLY_LISTED) A weekly Item Group Bootstrap feed file containing all the item group variation information associated with items returned in the Item Bootstrap feed file for all the items in a specific category. (feed_scope = ALL_ACTIVE) Note: Filters are applied to the feed files. For details, see Feed File Filters. When curating the items returned, be sure to code as if these filters are not applied as they can be changed or removed in the future. The contents of these feed files are based on the contents of the corresponding daily Item or Item Bootstrap feed file. When a new Item or Item Bootstrap feed file is generated, the service reads the file and if an item in the file has a primaryItemGroupId value, which indicates the item is part of an item group, it uses that value to return the item group (parent item) information for that item in the corresponding Item Group or Item Group Bootstrap feed file. This information includes the name/value pair of the aspects of the items in this group returned in the variesByLocalizedAspects column. For example, if the item was a shirt some of the variation names could be Size, Color, etc. Also the images for the various aspects are returned in the additionalImageUrls column. The first line in any feed file is the header, which labels the columns and indicates the order of the values on each line. Each header is described in the Response fields section. Combining the Item Group and Item feed files The Item Group or Item Group Bootstrap feed file contains details about the item group (parent item), including the item group ID itemGroupId. You match the value of itemGroupId from the Item Group feed file with the value of primaryItemGroupId from the corresponding daily Item or Item Bootstrap feed file. URLs for this method Production URL: https://api.ebay.com/buy/feed/v1_beta/item_group? Sandbox URL: https://api.sandbox.ebay.com/buy/feed/v1_beta/item_group? Downloading feed files Item Group feed files are binary gzip files. If the file is larger than 100 MB, the download must be streamed in chunks. You specify the size of the chunks in bytes using the Range request header. The content-range response header indicates where in the full resource this partial chunk of data belongs and the total number of bytes in the file. For more information about using these headers, see Retrieving a gzip feed file. Note: The response is always only a TSV_GZIP file. However for documentation purposes, the response is shown as JSON fields so that the value returned in each column can be explained. The order of the response fields, shows you the order of the columns in the feed file. Restrictions For a list of supported sites and other restrictions, see API Restrictions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_item_group_feed_with_http_info(x_ebay_c_marketplace_id, feed_scope, category_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_ebay_c_marketplace_id: The ID of the eBay marketplace where the item is hosted. Note: This value is case sensitive. For example: &nbsp;&nbsp;X-EBAY-C-MARKETPLACE-ID = EBAY_US For a list of supported sites see, API Restrictions. (required)
        :param str feed_scope: Specifies the type of file to return. Valid Values: NEWLY_LISTED - Returns the Item Group feed file containing the item group variation information for items in the daily Item feed file that were associated with an item group. The items in this type of Item feed file are items that were listed on the day specified by the date parameter in the category specified by the category_id parameter. /item_group?feed_scope=NEWLY_LISTED&amp;category_id=15032&amp;date=20170925 ALL_ACTIVE - Returns the weekly Item Group Bootstrap file containing the item group variation information for items in the weekly Item Bootstrap feed file that were associated with an item group. The items are Good 'Til Cancelled items in the category specified by the category_id parameter. Note: Bootstrap files are generated every Tuesday and the file is available on Wednesday. However, the exact time the file is available can vary so we recommend you download the Bootstrap file on Thursday. The item groups in the file are for the items that were in the specified category on Sunday. /item_group?feed_scope=ALL_ACTIVE&amp;category_id=15032 (required)
        :param str category_id: An eBay top-level category ID of the items to be returned in the feed file. The list of eBay category IDs changes over time and category IDs are not the same across all the eBay marketplaces. To get a list of the top-level categories for a marketplaces, you can use the Taxonomy API getCategoryTree method. This method retrieves the complete category tree for the marketplace. The top-level categories are identified by the categoryTreeNodeLevel field. For example: &nbsp;&nbsp;&quot;categoryTreeNodeLevel&quot;: 1 For details see Get Categories for Buy APIs. Restriction: Must be a top-level category (required)
        :param str range: This header specifies the range in bytes of the chunks of the gzip file being returned. Format: bytes=startpos-endpos For example, the following retrieves the first 10 MBs of the feed file. &nbsp;&nbsp;Range bytes=0-10485760 For more information about using this headers, see Retrieving a gzip feed file. Maximum: 100 MB (10MB in the Sandbox)
        :param str _date: The date of the daily Item Group feed file (feed_scope=NEWLY_LISTED) you want. The date is required only for the daily Item Group feed file. If you specify a date for the Item Group Bootstrap file (feed_scope=ALL_ACTIVE), the date is ignored and the latest file is returned. The date the Item Group Bootstrap feed file was generated is returned in the Last-Modified response header. The Item Group feed files are generated every day and there are 14 daily files available. There is a 48 hour latency when generating the files. This means on July 10, the latest feed file you can download is July 8. Note: The generated files are stored using MST (US Mountain Standard Time), which is -7 hours UTC time. Format: yyyyMMdd Requirement: Requirements: Required only when feed_scope=NEWLY_LISTED Must be within 3-14 days in the past
        :return: ItemGroupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_ebay_c_marketplace_id', 'feed_scope', 'category_id', 'range', '_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_item_group_feed" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_ebay_c_marketplace_id' is set
        if ('x_ebay_c_marketplace_id' not in params or
                params['x_ebay_c_marketplace_id'] is None):
            raise ValueError("Missing the required parameter `x_ebay_c_marketplace_id` when calling `get_item_group_feed`")  # noqa: E501
        # verify the required parameter 'feed_scope' is set
        if ('feed_scope' not in params or
                params['feed_scope'] is None):
            raise ValueError("Missing the required parameter `feed_scope` when calling `get_item_group_feed`")  # noqa: E501
        # verify the required parameter 'category_id' is set
        if ('category_id' not in params or
                params['category_id'] is None):
            raise ValueError("Missing the required parameter `category_id` when calling `get_item_group_feed`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'feed_scope' in params:
            query_params.append(('feed_scope', params['feed_scope']))  # noqa: E501
        if 'category_id' in params:
            query_params.append(('category_id', params['category_id']))  # noqa: E501
        if '_date' in params:
            query_params.append(('date', params['_date']))  # noqa: E501

        header_params = {}
        if 'x_ebay_c_marketplace_id' in params:
            header_params['X-EBAY-C-MARKETPLACE-ID'] = params['x_ebay_c_marketplace_id']  # noqa: E501
        if 'range' in params:
            header_params['Range'] = params['range']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/tab-separated-values'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/item_group', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ItemGroupResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
