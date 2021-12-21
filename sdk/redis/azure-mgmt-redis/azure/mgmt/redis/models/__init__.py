# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import CheckNameAvailabilityParameters
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorDetail
    from ._models_py3 import ErrorResponse
    from ._models_py3 import ExportRDBParameters
    from ._models_py3 import ImportRDBParameters
    from ._models_py3 import ManagedServiceIdentity
    from ._models_py3 import NotificationListResponse
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
    from ._models_py3 import PrivateEndpoint
    from ._models_py3 import PrivateEndpointConnection
    from ._models_py3 import PrivateEndpointConnectionListResult
    from ._models_py3 import PrivateLinkResource
    from ._models_py3 import PrivateLinkResourceListResult
    from ._models_py3 import PrivateLinkServiceConnectionState
    from ._models_py3 import ProxyResource
    from ._models_py3 import RedisAccessKeys
    from ._models_py3 import RedisCommonProperties
    from ._models_py3 import RedisCommonPropertiesRedisConfiguration
    from ._models_py3 import RedisCreateParameters
    from ._models_py3 import RedisCreateProperties
    from ._models_py3 import RedisFirewallRule
    from ._models_py3 import RedisFirewallRuleCreateParameters
    from ._models_py3 import RedisFirewallRuleListResult
    from ._models_py3 import RedisForceRebootResponse
    from ._models_py3 import RedisInstanceDetails
    from ._models_py3 import RedisLinkedServer
    from ._models_py3 import RedisLinkedServerCreateParameters
    from ._models_py3 import RedisLinkedServerCreateProperties
    from ._models_py3 import RedisLinkedServerProperties
    from ._models_py3 import RedisLinkedServerWithProperties
    from ._models_py3 import RedisLinkedServerWithPropertiesList
    from ._models_py3 import RedisListResult
    from ._models_py3 import RedisPatchSchedule
    from ._models_py3 import RedisPatchScheduleListResult
    from ._models_py3 import RedisProperties
    from ._models_py3 import RedisRebootParameters
    from ._models_py3 import RedisRegenerateKeyParameters
    from ._models_py3 import RedisResource
    from ._models_py3 import RedisUpdateParameters
    from ._models_py3 import RedisUpdateProperties
    from ._models_py3 import Resource
    from ._models_py3 import ScheduleEntry
    from ._models_py3 import Sku
    from ._models_py3 import TrackedResource
    from ._models_py3 import UpgradeNotification
    from ._models_py3 import UserAssignedIdentity
except (SyntaxError, ImportError):
    from ._models import CheckNameAvailabilityParameters  # type: ignore
    from ._models import ErrorAdditionalInfo  # type: ignore
    from ._models import ErrorDetail  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import ExportRDBParameters  # type: ignore
    from ._models import ImportRDBParameters  # type: ignore
    from ._models import ManagedServiceIdentity  # type: ignore
    from ._models import NotificationListResponse  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import PrivateEndpoint  # type: ignore
    from ._models import PrivateEndpointConnection  # type: ignore
    from ._models import PrivateEndpointConnectionListResult  # type: ignore
    from ._models import PrivateLinkResource  # type: ignore
    from ._models import PrivateLinkResourceListResult  # type: ignore
    from ._models import PrivateLinkServiceConnectionState  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import RedisAccessKeys  # type: ignore
    from ._models import RedisCommonProperties  # type: ignore
    from ._models import RedisCommonPropertiesRedisConfiguration  # type: ignore
    from ._models import RedisCreateParameters  # type: ignore
    from ._models import RedisCreateProperties  # type: ignore
    from ._models import RedisFirewallRule  # type: ignore
    from ._models import RedisFirewallRuleCreateParameters  # type: ignore
    from ._models import RedisFirewallRuleListResult  # type: ignore
    from ._models import RedisForceRebootResponse  # type: ignore
    from ._models import RedisInstanceDetails  # type: ignore
    from ._models import RedisLinkedServer  # type: ignore
    from ._models import RedisLinkedServerCreateParameters  # type: ignore
    from ._models import RedisLinkedServerCreateProperties  # type: ignore
    from ._models import RedisLinkedServerProperties  # type: ignore
    from ._models import RedisLinkedServerWithProperties  # type: ignore
    from ._models import RedisLinkedServerWithPropertiesList  # type: ignore
    from ._models import RedisListResult  # type: ignore
    from ._models import RedisPatchSchedule  # type: ignore
    from ._models import RedisPatchScheduleListResult  # type: ignore
    from ._models import RedisProperties  # type: ignore
    from ._models import RedisRebootParameters  # type: ignore
    from ._models import RedisRegenerateKeyParameters  # type: ignore
    from ._models import RedisResource  # type: ignore
    from ._models import RedisUpdateParameters  # type: ignore
    from ._models import RedisUpdateProperties  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ScheduleEntry  # type: ignore
    from ._models import Sku  # type: ignore
    from ._models import TrackedResource  # type: ignore
    from ._models import UpgradeNotification  # type: ignore
    from ._models import UserAssignedIdentity  # type: ignore

from ._redis_management_client_enums import (
    DayOfWeek,
    DefaultName,
    ManagedServiceIdentityType,
    PrivateEndpointConnectionProvisioningState,
    PrivateEndpointServiceConnectionStatus,
    ProvisioningState,
    PublicNetworkAccess,
    RebootType,
    RedisKeyType,
    ReplicationRole,
    SkuFamily,
    SkuName,
    TlsVersion,
)

__all__ = [
    'CheckNameAvailabilityParameters',
    'ErrorAdditionalInfo',
    'ErrorDetail',
    'ErrorResponse',
    'ExportRDBParameters',
    'ImportRDBParameters',
    'ManagedServiceIdentity',
    'NotificationListResponse',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'PrivateEndpoint',
    'PrivateEndpointConnection',
    'PrivateEndpointConnectionListResult',
    'PrivateLinkResource',
    'PrivateLinkResourceListResult',
    'PrivateLinkServiceConnectionState',
    'ProxyResource',
    'RedisAccessKeys',
    'RedisCommonProperties',
    'RedisCommonPropertiesRedisConfiguration',
    'RedisCreateParameters',
    'RedisCreateProperties',
    'RedisFirewallRule',
    'RedisFirewallRuleCreateParameters',
    'RedisFirewallRuleListResult',
    'RedisForceRebootResponse',
    'RedisInstanceDetails',
    'RedisLinkedServer',
    'RedisLinkedServerCreateParameters',
    'RedisLinkedServerCreateProperties',
    'RedisLinkedServerProperties',
    'RedisLinkedServerWithProperties',
    'RedisLinkedServerWithPropertiesList',
    'RedisListResult',
    'RedisPatchSchedule',
    'RedisPatchScheduleListResult',
    'RedisProperties',
    'RedisRebootParameters',
    'RedisRegenerateKeyParameters',
    'RedisResource',
    'RedisUpdateParameters',
    'RedisUpdateProperties',
    'Resource',
    'ScheduleEntry',
    'Sku',
    'TrackedResource',
    'UpgradeNotification',
    'UserAssignedIdentity',
    'DayOfWeek',
    'DefaultName',
    'ManagedServiceIdentityType',
    'PrivateEndpointConnectionProvisioningState',
    'PrivateEndpointServiceConnectionStatus',
    'ProvisioningState',
    'PublicNetworkAccess',
    'RebootType',
    'RedisKeyType',
    'ReplicationRole',
    'SkuFamily',
    'SkuName',
    'TlsVersion',
]
