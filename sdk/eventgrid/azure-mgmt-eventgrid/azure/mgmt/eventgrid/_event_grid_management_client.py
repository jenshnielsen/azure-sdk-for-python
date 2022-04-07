# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Optional, TYPE_CHECKING

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

from . import models
from ._configuration import EventGridManagementClientConfiguration
from .operations import ChannelsOperations, DomainEventSubscriptionsOperations, DomainTopicEventSubscriptionsOperations, DomainTopicsOperations, DomainsOperations, EventChannelsOperations, EventSubscriptionsOperations, ExtensionTopicsOperations, Operations, PartnerConfigurationsOperations, PartnerDestinationsOperations, PartnerNamespacesOperations, PartnerRegistrationsOperations, PartnerTopicEventSubscriptionsOperations, PartnerTopicsOperations, PrivateEndpointConnectionsOperations, PrivateLinkResourcesOperations, SystemTopicEventSubscriptionsOperations, SystemTopicsOperations, TopicEventSubscriptionsOperations, TopicTypesOperations, TopicsOperations, VerifiedPartnersOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential

class EventGridManagementClient:
    """Azure EventGrid Management Client.

    :ivar channels: ChannelsOperations operations
    :vartype channels: azure.mgmt.eventgrid.operations.ChannelsOperations
    :ivar domains: DomainsOperations operations
    :vartype domains: azure.mgmt.eventgrid.operations.DomainsOperations
    :ivar domain_topics: DomainTopicsOperations operations
    :vartype domain_topics: azure.mgmt.eventgrid.operations.DomainTopicsOperations
    :ivar event_channels: EventChannelsOperations operations
    :vartype event_channels: azure.mgmt.eventgrid.operations.EventChannelsOperations
    :ivar event_subscriptions: EventSubscriptionsOperations operations
    :vartype event_subscriptions: azure.mgmt.eventgrid.operations.EventSubscriptionsOperations
    :ivar domain_topic_event_subscriptions: DomainTopicEventSubscriptionsOperations operations
    :vartype domain_topic_event_subscriptions:
     azure.mgmt.eventgrid.operations.DomainTopicEventSubscriptionsOperations
    :ivar topic_event_subscriptions: TopicEventSubscriptionsOperations operations
    :vartype topic_event_subscriptions:
     azure.mgmt.eventgrid.operations.TopicEventSubscriptionsOperations
    :ivar domain_event_subscriptions: DomainEventSubscriptionsOperations operations
    :vartype domain_event_subscriptions:
     azure.mgmt.eventgrid.operations.DomainEventSubscriptionsOperations
    :ivar system_topic_event_subscriptions: SystemTopicEventSubscriptionsOperations operations
    :vartype system_topic_event_subscriptions:
     azure.mgmt.eventgrid.operations.SystemTopicEventSubscriptionsOperations
    :ivar partner_topic_event_subscriptions: PartnerTopicEventSubscriptionsOperations operations
    :vartype partner_topic_event_subscriptions:
     azure.mgmt.eventgrid.operations.PartnerTopicEventSubscriptionsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.eventgrid.operations.Operations
    :ivar partner_configurations: PartnerConfigurationsOperations operations
    :vartype partner_configurations:
     azure.mgmt.eventgrid.operations.PartnerConfigurationsOperations
    :ivar partner_destinations: PartnerDestinationsOperations operations
    :vartype partner_destinations: azure.mgmt.eventgrid.operations.PartnerDestinationsOperations
    :ivar partner_namespaces: PartnerNamespacesOperations operations
    :vartype partner_namespaces: azure.mgmt.eventgrid.operations.PartnerNamespacesOperations
    :ivar partner_registrations: PartnerRegistrationsOperations operations
    :vartype partner_registrations: azure.mgmt.eventgrid.operations.PartnerRegistrationsOperations
    :ivar partner_topics: PartnerTopicsOperations operations
    :vartype partner_topics: azure.mgmt.eventgrid.operations.PartnerTopicsOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections:
     azure.mgmt.eventgrid.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources: azure.mgmt.eventgrid.operations.PrivateLinkResourcesOperations
    :ivar system_topics: SystemTopicsOperations operations
    :vartype system_topics: azure.mgmt.eventgrid.operations.SystemTopicsOperations
    :ivar topics: TopicsOperations operations
    :vartype topics: azure.mgmt.eventgrid.operations.TopicsOperations
    :ivar extension_topics: ExtensionTopicsOperations operations
    :vartype extension_topics: azure.mgmt.eventgrid.operations.ExtensionTopicsOperations
    :ivar topic_types: TopicTypesOperations operations
    :vartype topic_types: azure.mgmt.eventgrid.operations.TopicTypesOperations
    :ivar verified_partners: VerifiedPartnersOperations operations
    :vartype verified_partners: azure.mgmt.eventgrid.operations.VerifiedPartnersOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param base_url: Service URL. Default value is 'https://management.azure.com'.
    :type base_url: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = EventGridManagementClientConfiguration(credential=credential, subscription_id=subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.channels = ChannelsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.domains = DomainsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.domain_topics = DomainTopicsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.event_channels = EventChannelsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.event_subscriptions = EventSubscriptionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.domain_topic_event_subscriptions = DomainTopicEventSubscriptionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.topic_event_subscriptions = TopicEventSubscriptionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.domain_event_subscriptions = DomainEventSubscriptionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.system_topic_event_subscriptions = SystemTopicEventSubscriptionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.partner_topic_event_subscriptions = PartnerTopicEventSubscriptionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.partner_configurations = PartnerConfigurationsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.partner_destinations = PartnerDestinationsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.partner_namespaces = PartnerNamespacesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.partner_registrations = PartnerRegistrationsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.partner_topics = PartnerTopicsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.system_topics = SystemTopicsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.topics = TopicsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.extension_topics = ExtensionTopicsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.topic_types = TopicTypesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.verified_partners = VerifiedPartnersOperations(self._client, self._config, self._serialize, self._deserialize)


    def _send_request(
        self,
        request,  # type: HttpRequest
        **kwargs: Any
    ) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> EventGridManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
