# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.core import AsyncPipelineClient
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from msrest import Deserializer, Serializer

from ._configuration import KeyVaultClientConfiguration
from ._operations_mixin import KeyVaultClientOperationsMixin

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class KeyVaultClient(KeyVaultClientOperationsMixin, MultiApiClientMixin, _SDKClient):
    """The key vault client performs cryptographic key operations and vault operations against the Key Vault service.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.
    :param api_version: API version to use if no profile is provided, or if missing in profile.
    :type api_version: str
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION = '2016-10-01'
    _PROFILE_TAG = "azure.keyvault.KeyVaultClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        api_version: Optional[str] = None,
        profile: KnownProfiles = KnownProfiles.default,
        **kwargs  # type: Any
    ) -> None:
        if api_version == '2016-10-01' or api_version == '7.0' or api_version == '7.1' or api_version == '7.2':
            base_url = '{vaultBaseUrl}'
        else:
            raise ValueError("API version {} is not available".format(api_version))
        self._config = KeyVaultClientConfiguration(**kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(KeyVaultClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2016-10-01: :mod:`v2016_10_01.models<azure.keyvault.v2016_10_01.models>`
           * 7.0: :mod:`v7_0.models<azure.keyvault.v7_0.models>`
           * 7.1: :mod:`v7_1.models<azure.keyvault.v7_1.models>`
           * 7.2: :mod:`v7_2.models<azure.keyvault.v7_2.models>`
        """
        if api_version == '2016-10-01':
            from ..v2016_10_01 import models
            return models
        elif api_version == '7.0':
            from ..v7_0 import models
            return models
        elif api_version == '7.1':
            from ..v7_1 import models
            return models
        elif api_version == '7.2':
            from ..v7_2 import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    async def close(self):
        await self._client.close()
    async def __aenter__(self):
        await self._client.__aenter__()
        return self
    async def __aexit__(self, *exc_details):
        await self._client.__aexit__(*exc_details)
