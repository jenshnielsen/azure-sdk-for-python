# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

__all__ = [
    'prepare_add_connection_to_group',
    'prepare_add_user_to_group',
    'prepare_check_connection_existence',
    'prepare_check_group_existence',
    'prepare_check_permission',
    'prepare_check_user_existence',
    'prepare_check_user_existence_in_group',
    'prepare_close_client_connection',
    'prepare_grant_permission',
    'prepare_healthapi_get_health_status',
    'prepare_remove_connection_from_group',
    'prepare_remove_user_from_all_groups',
    'prepare_remove_user_from_group',
    'prepare_revoke_permission',
    'prepare_send_to_all',
    'prepare_send_to_connection',
    'prepare_send_to_group',
    'prepare_send_to_user'
]

from typing import TYPE_CHECKING

from msrest import Serializer
from azure.messaging.webpubsubservice.core.rest import HttpRequest
from azure.core.pipeline.transport._base import _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, IO, List, Optional, Union, Dict
    try:
        from typing import Literal
    except ImportError: # < 3.8
        from typing_extensions import Literal
    Permissions = Union[Literal['joinLeaveGroup'], Literal['sendToGroup']]

_SERIALIZER = Serializer()


def prepare_healthapi_get_health_status(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-10-01")  # type: Optional[str]

    # Construct URL
    url = kwargs.pop("template_url", '/api/health')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if api_version is not None:
        query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    return HttpRequest(
        method="HEAD",
        url=url,
        params=query_parameters,
    )


def prepare_send_to_all(
    hub,  # type: str
    body,
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    excluded = kwargs.pop('excluded', None)  # type: Optional[List[str]]
    api_version = kwargs.pop('api_version', "2020-10-01")  # type: Optional[str]
    content_type = kwargs.pop("content_type", "application/octet-stream")

    # Construct URL
    url = kwargs.pop("template_url", '/api/hubs/{hub}/:send')
    path_format_arguments = {
        'hub': _SERIALIZER.url("hub", hub, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if excluded is not None:
        query_parameters['excluded'] = [
            _SERIALIZER.query("excluded", q, 'str') if q is not None else '' for q in excluded
        ]
    if api_version is not None:
        query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')

    body_content_kwargs = {}  # type: Dict[str, Any]
    if header_parameters['Content-Type'].split(";")[0] in ['application/octet-stream']:
        body_content_kwargs['content'] = body

    elif header_parameters['Content-Type'].split(";")[0] in ['text/plain']:
        body_content_kwargs['content'] = body
    elif header_parameters['Content-Type'].split(";")[0] in ['application/json']:
        body_content_kwargs['content'] = body


    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **body_content_kwargs
    )


def prepare_check_connection_existence(
    hub,  # type: str
    connection_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-10-01")  # type: Optional[str]

    # Construct URL
    url = kwargs.pop("template_url", '/api/hubs/{hub}/connections/{connectionId}')
    path_format_arguments = {
        'hub': _SERIALIZER.url("hub", hub, 'str'),
        'connectionId': _SERIALIZER.url("connection_id", connection_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if api_version is not None:
        query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    return HttpRequest(
        method="HEAD",
        url=url,
        params=query_parameters,
    )


def prepare_close_client_connection(
    hub,  # type: str
    connection_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    reason = kwargs.pop('reason', None)  # type: Optional[str]
    api_version = kwargs.pop('api_version', "2020-10-01")  # type: Optional[str]

    # Construct URL
    url = kwargs.pop("template_url", '/api/hubs/{hub}/connections/{connectionId}')
    path_format_arguments = {
        'hub': _SERIALIZER.url("hub", hub, 'str'),
        'connectionId': _SERIALIZER.url("connection_id", connection_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if reason is not None:
        query_parameters['reason'] = _SERIALIZER.query("reason", reason, 'str')
    if api_version is not None:
        query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
    )


def prepare_send_to_connection(
    hub,  # type: str
    connection_id,  # type: str
    body, # type: Union[IO, str, Dict]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-10-01")  # type: Optional[str]
    content_type = kwargs.pop("content_type", "application/octet-stream")

    # Construct URL
    url = kwargs.pop("template_url", '/api/hubs/{hub}/connections/{connectionId}/:send')
    path_format_arguments = {
        'hub': _SERIALIZER.url("hub", hub, 'str'),
        'connectionId': _SERIALIZER.url("connection_id", connection_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if api_version is not None:
        query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')

    body_content_kwargs = {}  # type: Dict[str, Any]
    if header_parameters['Content-Type'].split(";")[0] in ['application/octet-stream']:
        body_content_kwargs['content'] = body

    elif header_parameters['Content-Type'].split(";")[0] in ['text/plain']:
        body_content_kwargs['content'] = body
    elif header_parameters['Content-Type'].split(";")[0] in ['application/json']:
        body_content_kwargs['content'] = body


    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **body_content_kwargs
    )


def prepare_check_group_existence(
    hub,  # type: str
    group,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-10-01")  # type: Optional[str]

    # Construct URL
    url = kwargs.pop("template_url", '/api/hubs/{hub}/groups/{group}')
    path_format_arguments = {
        'hub': _SERIALIZER.url("hub", hub, 'str'),
        'group': _SERIALIZER.url("group", group, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if api_version is not None:
        query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    return HttpRequest(
        method="HEAD",
        url=url,
        params=query_parameters,
    )


def prepare_send_to_group(
    hub,  # type: str
    group,  # type: str
    body, # type: Union[IO, str, Dict]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    excluded = kwargs.pop('excluded', None)  # type: Optional[List[str]]
    api_version = kwargs.pop('api_version', "2020-10-01")  # type: Optional[str]
    content_type = kwargs.pop("content_type", "application/octet-stream")

    # Construct URL
    url = kwargs.pop("template_url", '/api/hubs/{hub}/groups/{group}/:send')
    path_format_arguments = {
        'hub': _SERIALIZER.url("hub", hub, 'str'),
        'group': _SERIALIZER.url("group", group, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if excluded is not None:
        query_parameters['excluded'] = [
            _SERIALIZER.query("excluded", q, 'str') if q is not None else '' for q in excluded
        ]
    if api_version is not None:
        query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')

    body_content_kwargs = {}  # type: Dict[str, Any]
    if header_parameters['Content-Type'].split(";")[0] in ['application/octet-stream']:
        body_content_kwargs['content'] = body

    elif header_parameters['Content-Type'].split(";")[0] in ['text/plain']:
        body_content_kwargs['content'] = body
    elif header_parameters['Content-Type'].split(";")[0] in ['application/json']:
        body_content_kwargs['content'] = body


    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **body_content_kwargs
    )


def prepare_add_connection_to_group(
    hub,  # type: str
    group,  # type: str
    connection_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-10-01")  # type: Optional[str]

    # Construct URL
    url = kwargs.pop("template_url", '/api/hubs/{hub}/groups/{group}/connections/{connectionId}')
    path_format_arguments = {
        'hub': _SERIALIZER.url("hub", hub, 'str'),
        'group': _SERIALIZER.url("group", group, 'str'),
        'connectionId': _SERIALIZER.url("connection_id", connection_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if api_version is not None:
        query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
    )


def prepare_remove_connection_from_group(
    hub,  # type: str
    group,  # type: str
    connection_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-10-01")  # type: Optional[str]

    # Construct URL
    url = kwargs.pop("template_url", '/api/hubs/{hub}/groups/{group}/connections/{connectionId}')
    path_format_arguments = {
        'hub': _SERIALIZER.url("hub", hub, 'str'),
        'group': _SERIALIZER.url("group", group, 'str'),
        'connectionId': _SERIALIZER.url("connection_id", connection_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if api_version is not None:
        query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
    )


def prepare_check_user_existence(
    hub,  # type: str
    user_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-10-01")  # type: Optional[str]

    # Construct URL
    url = kwargs.pop("template_url", '/api/hubs/{hub}/users/{userId}')
    path_format_arguments = {
        'hub': _SERIALIZER.url("hub", hub, 'str'),
        'userId': _SERIALIZER.url("user_id", user_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if api_version is not None:
        query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    return HttpRequest(
        method="HEAD",
        url=url,
        params=query_parameters,
    )


def prepare_send_to_user(
    hub,  # type: str
    user_id,  # type: str
    body, # type: Union[IO, str, Dict]

    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-10-01")  # type: Optional[str]
    content_type = kwargs.pop("content_type", "application/octet-stream")

    # Construct URL
    url = kwargs.pop("template_url", '/api/hubs/{hub}/users/{userId}/:send')
    path_format_arguments = {
        'hub': _SERIALIZER.url("hub", hub, 'str'),
        'userId': _SERIALIZER.url("user_id", user_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if api_version is not None:
        query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')

    body_content_kwargs = {}  # type: Dict[str, Any]
    if header_parameters['Content-Type'].split(";")[0] in ['application/octet-stream']:
        body_content_kwargs['content'] = body

    elif header_parameters['Content-Type'].split(";")[0] in ['text/plain']:
        body_content_kwargs['content'] = body
    elif header_parameters['Content-Type'].split(";")[0] in ['application/json']:
        body_content_kwargs['content'] = body


    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **body_content_kwargs
    )


def prepare_check_user_existence_in_group(
    hub,  # type: str
    group,  # type: str
    user_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-10-01")  # type: Optional[str]

    # Construct URL
    url = kwargs.pop("template_url", '/api/hubs/{hub}/users/{userId}/groups/{group}')
    path_format_arguments = {
        'hub': _SERIALIZER.url("hub", hub, 'str'),
        'group': _SERIALIZER.url("group", group, 'str'),
        'userId': _SERIALIZER.url("user_id", user_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if api_version is not None:
        query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    return HttpRequest(
        method="HEAD",
        url=url,
        params=query_parameters,
    )


def prepare_add_user_to_group(
    hub,  # type: str
    group,  # type: str
    user_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-10-01")  # type: Optional[str]

    # Construct URL
    url = kwargs.pop("template_url", '/api/hubs/{hub}/users/{userId}/groups/{group}')
    path_format_arguments = {
        'hub': _SERIALIZER.url("hub", hub, 'str'),
        'group': _SERIALIZER.url("group", group, 'str'),
        'userId': _SERIALIZER.url("user_id", user_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if api_version is not None:
        query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
    )


def prepare_remove_user_from_group(
    hub,  # type: str
    group,  # type: str
    user_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-10-01")  # type: Optional[str]

    # Construct URL
    url = kwargs.pop("template_url", '/api/hubs/{hub}/users/{userId}/groups/{group}')
    path_format_arguments = {
        'hub': _SERIALIZER.url("hub", hub, 'str'),
        'group': _SERIALIZER.url("group", group, 'str'),
        'userId': _SERIALIZER.url("user_id", user_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if api_version is not None:
        query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
    )


def prepare_remove_user_from_all_groups(
    hub,  # type: str
    user_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-10-01")  # type: Optional[str]

    # Construct URL
    url = kwargs.pop("template_url", '/api/hubs/{hub}/users/{userId}/groups')
    path_format_arguments = {
        'hub': _SERIALIZER.url("hub", hub, 'str'),
        'userId': _SERIALIZER.url("user_id", user_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if api_version is not None:
        query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
    )


def prepare_grant_permission(
    hub,  # type: str
    permission,  # type: Permissions
    connection_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    target_name = kwargs.pop('target_name', None)  # type: Optional[str]
    api_version = kwargs.pop('api_version', "2020-10-01")  # type: Optional[str]

    # Construct URL
    url = kwargs.pop("template_url", '/api/hubs/{hub}/permissions/{permission}/connections/{connectionId}')
    path_format_arguments = {
        'hub': _SERIALIZER.url("hub", hub, 'str'),
        'permission': _SERIALIZER.url("permission", permission, 'str'),
        'connectionId': _SERIALIZER.url("connection_id", connection_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if target_name is not None:
        query_parameters['targetName'] = _SERIALIZER.query("target_name", target_name, 'str')
    if api_version is not None:
        query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
    )


def prepare_revoke_permission(
    hub,  # type: str
    permission,  # type: Permissions
    connection_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    target_name = kwargs.pop('target_name', None)  # type: Optional[str]
    api_version = kwargs.pop('api_version', "2020-10-01")  # type: Optional[str]

    # Construct URL
    url = kwargs.pop("template_url", '/api/hubs/{hub}/permissions/{permission}/connections/{connectionId}')
    path_format_arguments = {
        'hub': _SERIALIZER.url("hub", hub, 'str'),
        'permission': _SERIALIZER.url("permission", permission, 'str'),
        'connectionId': _SERIALIZER.url("connection_id", connection_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if target_name is not None:
        query_parameters['targetName'] = _SERIALIZER.query("target_name", target_name, 'str')
    if api_version is not None:
        query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
    )


def prepare_check_permission(
    hub,  # type: str
    permission,  # type: Permissions
    connection_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    target_name = kwargs.pop('target_name', None)  # type: Optional[str]
    api_version = kwargs.pop('api_version', "2020-10-01")  # type: Optional[str]

    # Construct URL
    url = kwargs.pop("template_url", '/api/hubs/{hub}/permissions/{permission}/connections/{connectionId}')
    path_format_arguments = {
        'hub': _SERIALIZER.url("hub", hub, 'str'),
        'permission': _SERIALIZER.url("permission", permission, 'str'),
        'connectionId': _SERIALIZER.url("connection_id", connection_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if target_name is not None:
        query_parameters['targetName'] = _SERIALIZER.query("target_name", target_name, 'str')
    if api_version is not None:
        query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    return HttpRequest(
        method="HEAD",
        url=url,
        params=query_parameters,
    )
