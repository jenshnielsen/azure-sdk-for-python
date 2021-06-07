# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorDetail
    from ._models_py3 import ErrorResponse
    from ._models_py3 import FilteringTag
    from ._models_py3 import IdentityProperties
    from ._models_py3 import LogRules
    from ._models_py3 import LogzMonitorResource
    from ._models_py3 import LogzMonitorResourceListResponse
    from ._models_py3 import LogzMonitorResourceUpdateParameters
    from ._models_py3 import LogzOrganizationProperties
    from ._models_py3 import LogzSingleSignOnProperties
    from ._models_py3 import LogzSingleSignOnResource
    from ._models_py3 import LogzSingleSignOnResourceListResponse
    from ._models_py3 import MonitorProperties
    from ._models_py3 import MonitorUpdateProperties
    from ._models_py3 import MonitoredResource
    from ._models_py3 import MonitoredResourceListResponse
    from ._models_py3 import MonitoringTagRules
    from ._models_py3 import MonitoringTagRulesListResponse
    from ._models_py3 import MonitoringTagRulesProperties
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
    from ._models_py3 import OperationResult
    from ._models_py3 import PlanData
    from ._models_py3 import SystemData
    from ._models_py3 import UserInfo
    from ._models_py3 import UserRoleListResponse
    from ._models_py3 import UserRoleRequest
    from ._models_py3 import UserRoleResponse
    from ._models_py3 import VMExtensionPayload
    from ._models_py3 import VMHostUpdateRequest
    from ._models_py3 import VMResources
    from ._models_py3 import VMResourcesListResponse
except (SyntaxError, ImportError):
    from ._models import ErrorAdditionalInfo  # type: ignore
    from ._models import ErrorDetail  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import FilteringTag  # type: ignore
    from ._models import IdentityProperties  # type: ignore
    from ._models import LogRules  # type: ignore
    from ._models import LogzMonitorResource  # type: ignore
    from ._models import LogzMonitorResourceListResponse  # type: ignore
    from ._models import LogzMonitorResourceUpdateParameters  # type: ignore
    from ._models import LogzOrganizationProperties  # type: ignore
    from ._models import LogzSingleSignOnProperties  # type: ignore
    from ._models import LogzSingleSignOnResource  # type: ignore
    from ._models import LogzSingleSignOnResourceListResponse  # type: ignore
    from ._models import MonitorProperties  # type: ignore
    from ._models import MonitorUpdateProperties  # type: ignore
    from ._models import MonitoredResource  # type: ignore
    from ._models import MonitoredResourceListResponse  # type: ignore
    from ._models import MonitoringTagRules  # type: ignore
    from ._models import MonitoringTagRulesListResponse  # type: ignore
    from ._models import MonitoringTagRulesProperties  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import OperationResult  # type: ignore
    from ._models import PlanData  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import UserInfo  # type: ignore
    from ._models import UserRoleListResponse  # type: ignore
    from ._models import UserRoleRequest  # type: ignore
    from ._models import UserRoleResponse  # type: ignore
    from ._models import VMExtensionPayload  # type: ignore
    from ._models import VMHostUpdateRequest  # type: ignore
    from ._models import VMResources  # type: ignore
    from ._models import VMResourcesListResponse  # type: ignore

from ._microsoft_logz_enums import (
    CreatedByType,
    LiftrResourceCategories,
    ManagedIdentityTypes,
    MarketplaceSubscriptionStatus,
    MonitoringStatus,
    ProvisioningState,
    SingleSignOnStates,
    TagAction,
    UserRole,
    VMHostUpdateStates,
)

__all__ = [
    'ErrorAdditionalInfo',
    'ErrorDetail',
    'ErrorResponse',
    'FilteringTag',
    'IdentityProperties',
    'LogRules',
    'LogzMonitorResource',
    'LogzMonitorResourceListResponse',
    'LogzMonitorResourceUpdateParameters',
    'LogzOrganizationProperties',
    'LogzSingleSignOnProperties',
    'LogzSingleSignOnResource',
    'LogzSingleSignOnResourceListResponse',
    'MonitorProperties',
    'MonitorUpdateProperties',
    'MonitoredResource',
    'MonitoredResourceListResponse',
    'MonitoringTagRules',
    'MonitoringTagRulesListResponse',
    'MonitoringTagRulesProperties',
    'OperationDisplay',
    'OperationListResult',
    'OperationResult',
    'PlanData',
    'SystemData',
    'UserInfo',
    'UserRoleListResponse',
    'UserRoleRequest',
    'UserRoleResponse',
    'VMExtensionPayload',
    'VMHostUpdateRequest',
    'VMResources',
    'VMResourcesListResponse',
    'CreatedByType',
    'LiftrResourceCategories',
    'ManagedIdentityTypes',
    'MarketplaceSubscriptionStatus',
    'MonitoringStatus',
    'ProvisioningState',
    'SingleSignOnStates',
    'TagAction',
    'UserRole',
    'VMHostUpdateStates',
]
