# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential
    from azure.core.pipeline.transport import HttpRequest, HttpResponse

from ._configuration import AzureMediaServicesConfiguration
from .operations import AccountFiltersOperations
from .operations import Operations
from .operations import MediaservicesOperations
from .operations import PrivateLinkResourcesOperations
from .operations import PrivateEndpointConnectionsOperations
from .operations import LocationsOperations
from .operations import AssetsOperations
from .operations import AssetFiltersOperations
from .operations import ContentKeyPoliciesOperations
from .operations import TransformsOperations
from .operations import JobsOperations
from .operations import StreamingPoliciesOperations
from .operations import StreamingLocatorsOperations
from .operations import LiveEventsOperations
from .operations import LiveOutputsOperations
from .operations import StreamingEndpointsOperations
from . import models


class AzureMediaServices(object):
    """This Swagger was generated by the API Framework.

    :ivar account_filters: AccountFiltersOperations operations
    :vartype account_filters: azure.mgmt.media.operations.AccountFiltersOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.media.operations.Operations
    :ivar mediaservices: MediaservicesOperations operations
    :vartype mediaservices: azure.mgmt.media.operations.MediaservicesOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources: azure.mgmt.media.operations.PrivateLinkResourcesOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections: azure.mgmt.media.operations.PrivateEndpointConnectionsOperations
    :ivar locations: LocationsOperations operations
    :vartype locations: azure.mgmt.media.operations.LocationsOperations
    :ivar assets: AssetsOperations operations
    :vartype assets: azure.mgmt.media.operations.AssetsOperations
    :ivar asset_filters: AssetFiltersOperations operations
    :vartype asset_filters: azure.mgmt.media.operations.AssetFiltersOperations
    :ivar content_key_policies: ContentKeyPoliciesOperations operations
    :vartype content_key_policies: azure.mgmt.media.operations.ContentKeyPoliciesOperations
    :ivar transforms: TransformsOperations operations
    :vartype transforms: azure.mgmt.media.operations.TransformsOperations
    :ivar jobs: JobsOperations operations
    :vartype jobs: azure.mgmt.media.operations.JobsOperations
    :ivar streaming_policies: StreamingPoliciesOperations operations
    :vartype streaming_policies: azure.mgmt.media.operations.StreamingPoliciesOperations
    :ivar streaming_locators: StreamingLocatorsOperations operations
    :vartype streaming_locators: azure.mgmt.media.operations.StreamingLocatorsOperations
    :ivar live_events: LiveEventsOperations operations
    :vartype live_events: azure.mgmt.media.operations.LiveEventsOperations
    :ivar live_outputs: LiveOutputsOperations operations
    :vartype live_outputs: azure.mgmt.media.operations.LiveOutputsOperations
    :ivar streaming_endpoints: StreamingEndpointsOperations operations
    :vartype streaming_endpoints: azure.mgmt.media.operations.StreamingEndpointsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = AzureMediaServicesConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.account_filters = AccountFiltersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.mediaservices = MediaservicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.locations = LocationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.assets = AssetsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.asset_filters = AssetFiltersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.content_key_policies = ContentKeyPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.transforms = TransformsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.jobs = JobsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.streaming_policies = StreamingPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.streaming_locators = StreamingLocatorsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.live_events = LiveEventsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.live_outputs = LiveOutputsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.streaming_endpoints = StreamingEndpointsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, http_request, **kwargs):
        # type: (HttpRequest, Any) -> HttpResponse
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.HttpResponse
        """
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AzureMediaServices
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
