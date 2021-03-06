# coding: utf-8

"""
    Healthbot APIs

    API interface for Healthbot application  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: healthbot-hackers@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ServicesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_services_device_groups_device_group_by_device_group_name(self, device_group_name, **kwargs):  # noqa: E501
        """Start a device-group&#39;s services.  # noqa: E501

        Start services of a device group. Use this to start stopped services.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_services_device_groups_device_group_by_device_group_name(device_group_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str device_group_name: Name of device group (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_services_device_groups_device_group_by_device_group_name_with_http_info(device_group_name, **kwargs)  # noqa: E501
        else:
            (data) = self.create_services_device_groups_device_group_by_device_group_name_with_http_info(device_group_name, **kwargs)  # noqa: E501
            return data

    def create_services_device_groups_device_group_by_device_group_name_with_http_info(self, device_group_name, **kwargs):  # noqa: E501
        """Start a device-group&#39;s services.  # noqa: E501

        Start services of a device group. Use this to start stopped services.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_services_device_groups_device_group_by_device_group_name_with_http_info(device_group_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str device_group_name: Name of device group (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_group_name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_services_device_groups_device_group_by_device_group_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_group_name' is set
        if ('device_group_name' not in params or
                params['device_group_name'] is None):
            raise ValueError("Missing the required parameter `device_group_name` when calling `create_services_device_groups_device_group_by_device_group_name`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_group_name' in params:
            path_params['device_group_name'] = params['device_group_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/octet-stream'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/services/device-group/{device_group_name}/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_services_network_group_by_network_group_name(self, network_group_name, **kwargs):  # noqa: E501
        """Start a network-group&#39;s services.  # noqa: E501

        Start services of a network group. Use this to start stopped services.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_services_network_group_by_network_group_name(network_group_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str network_group_name: Name of network group (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_services_network_group_by_network_group_name_with_http_info(network_group_name, **kwargs)  # noqa: E501
        else:
            (data) = self.create_services_network_group_by_network_group_name_with_http_info(network_group_name, **kwargs)  # noqa: E501
            return data

    def create_services_network_group_by_network_group_name_with_http_info(self, network_group_name, **kwargs):  # noqa: E501
        """Start a network-group&#39;s services.  # noqa: E501

        Start services of a network group. Use this to start stopped services.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_services_network_group_by_network_group_name_with_http_info(network_group_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str network_group_name: Name of network group (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['network_group_name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_services_network_group_by_network_group_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'network_group_name' is set
        if ('network_group_name' not in params or
                params['network_group_name'] is None):
            raise ValueError("Missing the required parameter `network_group_name` when calling `create_services_network_group_by_network_group_name`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'network_group_name' in params:
            path_params['network_group_name'] = params['network_group_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/octet-stream'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/services/network-group/{network_group_name}/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_services_device_groups_device_group_by_device_group_name(self, device_group_name, **kwargs):  # noqa: E501
        """Stop and remove a device-group&#39;s services.  # noqa: E501

        Stop and clean services of a device-group. This will remove all the services for a device-group, however, it  will not clean up the collected data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_services_device_groups_device_group_by_device_group_name(device_group_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str device_group_name: Name of device group (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_services_device_groups_device_group_by_device_group_name_with_http_info(device_group_name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_services_device_groups_device_group_by_device_group_name_with_http_info(device_group_name, **kwargs)  # noqa: E501
            return data

    def delete_services_device_groups_device_group_by_device_group_name_with_http_info(self, device_group_name, **kwargs):  # noqa: E501
        """Stop and remove a device-group&#39;s services.  # noqa: E501

        Stop and clean services of a device-group. This will remove all the services for a device-group, however, it  will not clean up the collected data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_services_device_groups_device_group_by_device_group_name_with_http_info(device_group_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str device_group_name: Name of device group (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_group_name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_services_device_groups_device_group_by_device_group_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_group_name' is set
        if ('device_group_name' not in params or
                params['device_group_name'] is None):
            raise ValueError("Missing the required parameter `device_group_name` when calling `delete_services_device_groups_device_group_by_device_group_name`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_group_name' in params:
            path_params['device_group_name'] = params['device_group_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/octet-stream'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/services/device-group/{device_group_name}/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_services_network_group_by_network_group_name(self, network_group_name, **kwargs):  # noqa: E501
        """Stop and remove a network-group&#39;s services.  # noqa: E501

        Stop and clean the services of a network group. This will remove all the services for a network-group, however, it will not clean up the collected data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_services_network_group_by_network_group_name(network_group_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str network_group_name: Name of network group (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_services_network_group_by_network_group_name_with_http_info(network_group_name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_services_network_group_by_network_group_name_with_http_info(network_group_name, **kwargs)  # noqa: E501
            return data

    def delete_services_network_group_by_network_group_name_with_http_info(self, network_group_name, **kwargs):  # noqa: E501
        """Stop and remove a network-group&#39;s services.  # noqa: E501

        Stop and clean the services of a network group. This will remove all the services for a network-group, however, it will not clean up the collected data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_services_network_group_by_network_group_name_with_http_info(network_group_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str network_group_name: Name of network group (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['network_group_name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_services_network_group_by_network_group_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'network_group_name' is set
        if ('network_group_name' not in params or
                params['network_group_name'] is None):
            raise ValueError("Missing the required parameter `network_group_name` when calling `delete_services_network_group_by_network_group_name`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'network_group_name' in params:
            path_params['network_group_name'] = params['network_group_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/octet-stream'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/services/network-group/{network_group_name}/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_services_device_groups_device_group_device_group(self, **kwargs):  # noqa: E501
        """Get running &#x60;device-group-name&#x60;s.  # noqa: E501

        Get the list of `device-group-name`s of device-groups whose services are running.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.retrieve_services_device_groups_device_group_device_group(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.retrieve_services_device_groups_device_group_device_group_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_services_device_groups_device_group_device_group_with_http_info(**kwargs)  # noqa: E501
            return data

    def retrieve_services_device_groups_device_group_device_group_with_http_info(self, **kwargs):  # noqa: E501
        """Get running &#x60;device-group-name&#x60;s.  # noqa: E501

        Get the list of `device-group-name`s of device-groups whose services are running.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.retrieve_services_device_groups_device_group_device_group_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_services_device_groups_device_group_device_group" % key
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

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/services/device-group/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_services_network_group(self, **kwargs):  # noqa: E501
        """Get running &#x60;network-group-name&#x60;s  # noqa: E501

        Get the list of `network-group-name`s of network-groups whose services are running.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.retrieve_services_network_group(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.retrieve_services_network_group_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_services_network_group_with_http_info(**kwargs)  # noqa: E501
            return data

    def retrieve_services_network_group_with_http_info(self, **kwargs):  # noqa: E501
        """Get running &#x60;network-group-name&#x60;s  # noqa: E501

        Get the list of `network-group-name`s of network-groups whose services are running.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.retrieve_services_network_group_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_services_network_group" % key
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

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/services/network-group/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
