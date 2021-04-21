# coding: utf-8

"""
    Order API

    The Order API provides interfaces that let shoppers pay for items (for both eBay guest and eBay member buyers). It also returns payment and shipping status of the order. It enables eBay partners to use accept payment without being <a href=\"https://www.pcisecuritystandards.org/\">PCI compliant</a> and use the <a href=\"/api-docs/buy/static/api-order.html#Post\">Post Order API</a> for returns and cancellations for eBay member buyers.   <p>The Order API has the following resources:  </p>  <ul>  <li><b>checkout_session:</b> Lets eBay members purchase items using PayPal or a credit card.</li>  <li><b>guest_checkout_session:</b> Lets eBay guests purchase items using a credit card or the <a href=\"/api-docs/buy/static/api-order.html#spb-checkout\">PayPal Smart Button</a>.</li>   <li><b>proxy_guest_checkout_session:</b> Lets eBay guests purchase items through a <a href=\"/api-docs/buy/static/api-order.html#vsp-checkout\">vault service provider</a> (VSP). &nbsp;&nbsp;<b>*Note:* </b>Due to the requirement of having a VSP, this resource is not available in the eBay <a href=\"https://developer.ebay.com/my/api_test_tool?index=0\">API Explorer</a>.</li>  <li><b>guest_purchase_order</b> and <b>purchase_order:</b> Lets eBay partners track the payment status and show the buyers their purchase order. </li> </ul>  # noqa: E501

    OpenAPI spec version: v1_beta.29.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ...buy_order.api_client import ApiClient


class PurchaseOrderApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_purchase_order(self, purchase_order_id, **kwargs):  # noqa: E501
        """get_purchase_order  # noqa: E501

        This method retrieves the details about a specific eBay member purchase order. It returns the line items, including purchase order status; dates created and modified; item quantity and listing data; payment and shipping information; and prices, taxes, and discounts and credits. The purchaseOrderId is passed in as a URI parameter and is required. This method has no request payload. The placeOrder method initiates the payment process, which can sometimes take a few minutes. You can use this method to not only get the details of a purchase order but to check the value of the purchaseOrderPaymentStatus field to determine if the order has been paid for. If the order has been paid for, this field will return PAID. This method also returns the legacyItemId, legacyTransactionId, and legacyOrderId fields. The values in these fields enable eBay partners to use the Post Order API for eBay member checkouts, to process a return or cancellation. For more information, see Post order tasks in the Buy Integration Guide. Restrictions For a list of supported sites and other restrictions, see API Restrictions in the Order API overview.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_purchase_order(purchase_order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str purchase_order_id: The unique identifier of a purchase order made by an eBay member, for which details are to be retrieved. This value is returned by the placeOrder method in the purchaseOrderId field. The purchaseOrderId is passed in as a URI parameter and is required. (required)
        :return: PurchaseOrder
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_purchase_order_with_http_info(purchase_order_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_purchase_order_with_http_info(purchase_order_id, **kwargs)  # noqa: E501
            return data

    def get_purchase_order_with_http_info(self, purchase_order_id, **kwargs):  # noqa: E501
        """get_purchase_order  # noqa: E501

        This method retrieves the details about a specific eBay member purchase order. It returns the line items, including purchase order status; dates created and modified; item quantity and listing data; payment and shipping information; and prices, taxes, and discounts and credits. The purchaseOrderId is passed in as a URI parameter and is required. This method has no request payload. The placeOrder method initiates the payment process, which can sometimes take a few minutes. You can use this method to not only get the details of a purchase order but to check the value of the purchaseOrderPaymentStatus field to determine if the order has been paid for. If the order has been paid for, this field will return PAID. This method also returns the legacyItemId, legacyTransactionId, and legacyOrderId fields. The values in these fields enable eBay partners to use the Post Order API for eBay member checkouts, to process a return or cancellation. For more information, see Post order tasks in the Buy Integration Guide. Restrictions For a list of supported sites and other restrictions, see API Restrictions in the Order API overview.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_purchase_order_with_http_info(purchase_order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str purchase_order_id: The unique identifier of a purchase order made by an eBay member, for which details are to be retrieved. This value is returned by the placeOrder method in the purchaseOrderId field. The purchaseOrderId is passed in as a URI parameter and is required. (required)
        :return: PurchaseOrder
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['purchase_order_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_purchase_order" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'purchase_order_id' is set
        if ('purchase_order_id' not in params or
                params['purchase_order_id'] is None):
            raise ValueError("Missing the required parameter `purchase_order_id` when calling `get_purchase_order`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'purchase_order_id' in params:
            path_params['purchaseOrderId'] = params['purchase_order_id']  # noqa: E501

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
            '/purchase_order/{purchaseOrderId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PurchaseOrder',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
