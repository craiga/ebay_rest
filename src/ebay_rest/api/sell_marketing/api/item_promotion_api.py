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


class ItemPromotionApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_item_promotion(self, **kwargs):  # noqa: E501
        """create_item_promotion  # noqa: E501

        This method creates an item promotion, where the buyer receives a discount when they meet the buying criteria that's set for the promotion. Known here as &quot;threshold promotions&quot;, these promotions trigger when a threshold is met. eBay highlights promoted items by placing teasers for the promoted items throughout the online buyer flows. Discounts are specified as either a monetary amount or a percentage off the standard sales price of a listing, letting you offer deals such as &quot;Buy 1 Get 1&quot; and &quot;Buy $50, get 20% off&quot;. Volume pricing promotions increase the value of the discount as the buyer increases the quantity they purchase. Coded Coupons provide unique codes that a buyer can use during checkout to receive a discount. The seller can specify the number of times a buyer can use the coupon and the maximum amount across all purchases that can be discounted using the coupon. The coupon code can also be made public (appearing on the seller&rsquo;s Offer page, search pages, the item listing, and the checkout page) or private (only on the seller&rsquo;s Offer page, but the seller can include the code in email and social media). Note: Coded Coupons are currently available in the US, UK, DE, FR, IT, ES, and AU marketplaces. There are two ways to add items to a threshold promotion: Key-based promotions select items using either the listing IDs or inventory reference IDs of the items you want to promote. Note that if you use inventory reference IDs, you must specify both the inventoryReferenceId and the associated inventoryReferenceType of the item(s) you want to include the promotion. Rule-based promotions select items using a list of eBay category IDs or seller Store category IDs. Rules can further constrain items in a promotion by minimum and maximum prices, brands, and item conditions. You must create a new promotion in either a DRAFT or SCHEDULED state. Use the DRAFT state when you are initially creating a promotion and you want to be sure it's correctly configured before scheduling it to run. When you create a promotion, the promotion ID is returned in the Location response header. Use this ID to reference the promotion in subsequent requests. Tip: Refer to the Selling Integration Guide for details and examples showing how to create and manage threshold promotions using the Promotions Manager. For information on the eBay marketplaces that support item promotions, see Promotions Manager requirements and restrictions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_item_promotion(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ItemPromotion body: This type defines the fields that describe an item promotion.
        :return: BaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_item_promotion_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_item_promotion_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_item_promotion_with_http_info(self, **kwargs):  # noqa: E501
        """create_item_promotion  # noqa: E501

        This method creates an item promotion, where the buyer receives a discount when they meet the buying criteria that's set for the promotion. Known here as &quot;threshold promotions&quot;, these promotions trigger when a threshold is met. eBay highlights promoted items by placing teasers for the promoted items throughout the online buyer flows. Discounts are specified as either a monetary amount or a percentage off the standard sales price of a listing, letting you offer deals such as &quot;Buy 1 Get 1&quot; and &quot;Buy $50, get 20% off&quot;. Volume pricing promotions increase the value of the discount as the buyer increases the quantity they purchase. Coded Coupons provide unique codes that a buyer can use during checkout to receive a discount. The seller can specify the number of times a buyer can use the coupon and the maximum amount across all purchases that can be discounted using the coupon. The coupon code can also be made public (appearing on the seller&rsquo;s Offer page, search pages, the item listing, and the checkout page) or private (only on the seller&rsquo;s Offer page, but the seller can include the code in email and social media). Note: Coded Coupons are currently available in the US, UK, DE, FR, IT, ES, and AU marketplaces. There are two ways to add items to a threshold promotion: Key-based promotions select items using either the listing IDs or inventory reference IDs of the items you want to promote. Note that if you use inventory reference IDs, you must specify both the inventoryReferenceId and the associated inventoryReferenceType of the item(s) you want to include the promotion. Rule-based promotions select items using a list of eBay category IDs or seller Store category IDs. Rules can further constrain items in a promotion by minimum and maximum prices, brands, and item conditions. You must create a new promotion in either a DRAFT or SCHEDULED state. Use the DRAFT state when you are initially creating a promotion and you want to be sure it's correctly configured before scheduling it to run. When you create a promotion, the promotion ID is returned in the Location response header. Use this ID to reference the promotion in subsequent requests. Tip: Refer to the Selling Integration Guide for details and examples showing how to create and manage threshold promotions using the Promotions Manager. For information on the eBay marketplaces that support item promotions, see Promotions Manager requirements and restrictions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_item_promotion_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ItemPromotion body: This type defines the fields that describe an item promotion.
        :return: BaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_item_promotion" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/item_promotion', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BaseResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_item_promotion(self, promotion_id, **kwargs):  # noqa: E501
        """delete_item_promotion  # noqa: E501

        This method deletes the threshold promotion specified by the promotion_id path parameter. Call getPromotions to retrieve the IDs of a seller's promotions. You can delete any promotion with the exception of those that are currently active (RUNNING). To end a running threshold promotion, call updateItemPromotion and adjust the endDate field as appropriate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_item_promotion(promotion_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str promotion_id: This path parameter takes a concatenation of the ID of the promotion you want to delete plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an &quot;at sign&quot; (@). The ID of the promotion (promotionId) is a unique eBay-assigned value that's generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. Example: 1********5@EBAY_US (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_item_promotion_with_http_info(promotion_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_item_promotion_with_http_info(promotion_id, **kwargs)  # noqa: E501
            return data

    def delete_item_promotion_with_http_info(self, promotion_id, **kwargs):  # noqa: E501
        """delete_item_promotion  # noqa: E501

        This method deletes the threshold promotion specified by the promotion_id path parameter. Call getPromotions to retrieve the IDs of a seller's promotions. You can delete any promotion with the exception of those that are currently active (RUNNING). To end a running threshold promotion, call updateItemPromotion and adjust the endDate field as appropriate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_item_promotion_with_http_info(promotion_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str promotion_id: This path parameter takes a concatenation of the ID of the promotion you want to delete plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an &quot;at sign&quot; (@). The ID of the promotion (promotionId) is a unique eBay-assigned value that's generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. Example: 1********5@EBAY_US (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['promotion_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_item_promotion" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'promotion_id' is set
        if ('promotion_id' not in params or
                params['promotion_id'] is None):
            raise ValueError("Missing the required parameter `promotion_id` when calling `delete_item_promotion`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'promotion_id' in params:
            path_params['promotion_id'] = params['promotion_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/item_promotion/{promotion_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_item_promotion(self, promotion_id, **kwargs):  # noqa: E501
        """get_item_promotion  # noqa: E501

        This method returns the complete details of the threshold promotion specified by the promotion_id path parameter. Call getPromotions to retrieve the IDs of a seller's promotions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_item_promotion(promotion_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str promotion_id: This path parameter takes a concatenation of the ID of the promotion you want to retrieve plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an &quot;at sign&quot; (@). The ID of the promotion (promotionId) is a unique eBay-assigned value that's generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. Example: 1********5@EBAY_US (required)
        :return: ItemPromotionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_item_promotion_with_http_info(promotion_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_item_promotion_with_http_info(promotion_id, **kwargs)  # noqa: E501
            return data

    def get_item_promotion_with_http_info(self, promotion_id, **kwargs):  # noqa: E501
        """get_item_promotion  # noqa: E501

        This method returns the complete details of the threshold promotion specified by the promotion_id path parameter. Call getPromotions to retrieve the IDs of a seller's promotions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_item_promotion_with_http_info(promotion_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str promotion_id: This path parameter takes a concatenation of the ID of the promotion you want to retrieve plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an &quot;at sign&quot; (@). The ID of the promotion (promotionId) is a unique eBay-assigned value that's generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. Example: 1********5@EBAY_US (required)
        :return: ItemPromotionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['promotion_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_item_promotion" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'promotion_id' is set
        if ('promotion_id' not in params or
                params['promotion_id'] is None):
            raise ValueError("Missing the required parameter `promotion_id` when calling `get_item_promotion`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'promotion_id' in params:
            path_params['promotion_id'] = params['promotion_id']  # noqa: E501

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
            '/item_promotion/{promotion_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ItemPromotionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_item_promotion(self, promotion_id, **kwargs):  # noqa: E501
        """update_item_promotion  # noqa: E501

        This method updates the specified threshold promotion with the new configuration that you supply in the request. Indicate the promotion you want to update using the promotion_id path parameter. Call getPromotions to retrieve the IDs of a seller's promotions. When updating a promotion, supply all the fields that you used to configure the original promotion (and not just the fields you are updating). eBay replaces the specified promotion with the values you supply in the update request and if you don't pass a field that currently has a value, the update request will fail. The parameters you are allowed to update with this request depend on the status of the promotion you're updating: DRAFT or SCHEDULED promotions: You can update any of the parameters in these promotions that have not yet started to run, including the discountRules. RUNNING or PAUSED promotions: You can change the endDate and the item's inventory but you cannot change the promotional discount or the promotion's start date. ENDED promotions: Nothing can be changed. Tip: When updating a RUNNING or PAUSED promotion, set the status field to SCHEDULED for the update request. When the promotion is updated, the previous status (either RUNNING or PAUSED) is retained.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_item_promotion(promotion_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str promotion_id: This path parameter takes a concatenation of the ID of the promotion you want to update plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an &quot;at sign&quot; (@). The ID of the promotion (promotionId) is a unique eBay-assigned value that's generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. Example: 1********5@EBAY_US (required)
        :param ItemPromotion body: This type defines the fields that describe an item promotion.
        :return: BaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_item_promotion_with_http_info(promotion_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_item_promotion_with_http_info(promotion_id, **kwargs)  # noqa: E501
            return data

    def update_item_promotion_with_http_info(self, promotion_id, **kwargs):  # noqa: E501
        """update_item_promotion  # noqa: E501

        This method updates the specified threshold promotion with the new configuration that you supply in the request. Indicate the promotion you want to update using the promotion_id path parameter. Call getPromotions to retrieve the IDs of a seller's promotions. When updating a promotion, supply all the fields that you used to configure the original promotion (and not just the fields you are updating). eBay replaces the specified promotion with the values you supply in the update request and if you don't pass a field that currently has a value, the update request will fail. The parameters you are allowed to update with this request depend on the status of the promotion you're updating: DRAFT or SCHEDULED promotions: You can update any of the parameters in these promotions that have not yet started to run, including the discountRules. RUNNING or PAUSED promotions: You can change the endDate and the item's inventory but you cannot change the promotional discount or the promotion's start date. ENDED promotions: Nothing can be changed. Tip: When updating a RUNNING or PAUSED promotion, set the status field to SCHEDULED for the update request. When the promotion is updated, the previous status (either RUNNING or PAUSED) is retained.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_item_promotion_with_http_info(promotion_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str promotion_id: This path parameter takes a concatenation of the ID of the promotion you want to update plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an &quot;at sign&quot; (@). The ID of the promotion (promotionId) is a unique eBay-assigned value that's generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. Example: 1********5@EBAY_US (required)
        :param ItemPromotion body: This type defines the fields that describe an item promotion.
        :return: BaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['promotion_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_item_promotion" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'promotion_id' is set
        if ('promotion_id' not in params or
                params['promotion_id'] is None):
            raise ValueError("Missing the required parameter `promotion_id` when calling `update_item_promotion`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'promotion_id' in params:
            path_params['promotion_id'] = params['promotion_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/item_promotion/{promotion_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BaseResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
