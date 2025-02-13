# coding: utf-8

"""
    Notification API

    The eBay Notification API enables management of the entire end-to-end eBay notification experience by allowing users to:<ul><li>Browse for supported notification topics and retrieve topic details</li><li>Create, configure, and manage notification destination endpionts</li><li>Configure, manage, and test notification subscriptions</li><li>Process eBay notifications and verify the integrity of the message payload</li></ul>  # noqa: E501

    OpenAPI spec version: v1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ...commerce_notification.api_client import ApiClient


class ConfigApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_config(self, **kwargs):  # noqa: E501
        """get_config  # noqa: E501

        This method allows applications to retrieve a previously created configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_config(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Config
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_config_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_config_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_config_with_http_info(self, **kwargs):  # noqa: E501
        """get_config  # noqa: E501

        This method allows applications to retrieve a previously created configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_config_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Config
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_config" % key
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/config', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Config',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_config(self, **kwargs):  # noqa: E501
        """update_config  # noqa: E501

        This method allows applications to create a new configuration or update an existing configuration. This app-level configuration allows developers to set up alerts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_config(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Config body: The configurations for this application.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_config_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.update_config_with_http_info(**kwargs)  # noqa: E501
            return data

    def update_config_with_http_info(self, **kwargs):  # noqa: E501
        """update_config  # noqa: E501

        This method allows applications to create a new configuration or update an existing configuration. This app-level configuration allows developers to set up alerts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_config_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Config body: The configurations for this application.
        :return: None
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
                    " to method update_config" % key
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
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/config', 'PUT',
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
