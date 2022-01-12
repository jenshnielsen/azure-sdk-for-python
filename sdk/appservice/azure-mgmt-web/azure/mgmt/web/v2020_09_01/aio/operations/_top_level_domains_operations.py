# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._top_level_domains_operations import build_get_request, build_list_agreements_request, build_list_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class TopLevelDomainsOperations:
    """TopLevelDomainsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.web.v2020_09_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list(
        self,
        **kwargs: Any
    ) -> AsyncIterable["_models.TopLevelDomainCollection"]:
        """Get all top-level domains supported for registration.

        Description for Get all top-level domains supported for registration.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either TopLevelDomainCollection or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.web.v2020_09_01.models.TopLevelDomainCollection]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TopLevelDomainCollection"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("TopLevelDomainCollection", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.DefaultErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/topLevelDomains'}  # type: ignore

    @distributed_trace_async
    async def get(
        self,
        name: str,
        **kwargs: Any
    ) -> "_models.TopLevelDomain":
        """Get details of a top-level domain.

        Description for Get details of a top-level domain.

        :param name: Name of the top-level domain.
        :type name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TopLevelDomain, or the result of cls(response)
        :rtype: ~azure.mgmt.web.v2020_09_01.models.TopLevelDomain
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TopLevelDomain"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            name=name,
            subscription_id=self._config.subscription_id,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.DefaultErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('TopLevelDomain', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/topLevelDomains/{name}'}  # type: ignore


    @distributed_trace
    def list_agreements(
        self,
        name: str,
        agreement_option: "_models.TopLevelDomainAgreementOption",
        **kwargs: Any
    ) -> AsyncIterable["_models.TldLegalAgreementCollection"]:
        """Gets all legal agreements that user needs to accept before purchasing a domain.

        Description for Gets all legal agreements that user needs to accept before purchasing a domain.

        :param name: Name of the top-level domain.
        :type name: str
        :param agreement_option: Domain agreement options.
        :type agreement_option: ~azure.mgmt.web.v2020_09_01.models.TopLevelDomainAgreementOption
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either TldLegalAgreementCollection or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.web.v2020_09_01.models.TldLegalAgreementCollection]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TldLegalAgreementCollection"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                _json = self._serialize.body(agreement_option, 'TopLevelDomainAgreementOption')
                
                request = build_list_agreements_request(
                    name=name,
                    subscription_id=self._config.subscription_id,
                    content_type=content_type,
                    json=_json,
                    template_url=self.list_agreements.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                _json = self._serialize.body(agreement_option, 'TopLevelDomainAgreementOption')
                
                request = build_list_agreements_request(
                    name=name,
                    subscription_id=self._config.subscription_id,
                    content_type=content_type,
                    json=_json,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("TldLegalAgreementCollection", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.DefaultErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_agreements.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/topLevelDomains/{name}/listAgreements'}  # type: ignore
