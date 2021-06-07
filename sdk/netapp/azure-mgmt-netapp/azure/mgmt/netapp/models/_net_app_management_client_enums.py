# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class ActiveDirectoryStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Status of the Active Directory
    """

    #: Active Directory created but not in use.
    CREATED = "Created"
    #: Active Directory in use by SMB Volume.
    IN_USE = "InUse"
    #: Active Directory Deleted.
    DELETED = "Deleted"
    #: Error with the Active Directory.
    ERROR = "Error"
    #: Active Directory Updating.
    UPDATING = "Updating"

class BackupType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of backup Manual or Scheduled
    """

    #: Manual backup.
    MANUAL = "Manual"
    #: Scheduled backup.
    SCHEDULED = "Scheduled"

class CheckNameResourceTypes(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Resource type used for verification.
    """

    MICROSOFT_NET_APP_NET_APP_ACCOUNTS = "Microsoft.NetApp/netAppAccounts"
    MICROSOFT_NET_APP_NET_APP_ACCOUNTS_CAPACITY_POOLS = "Microsoft.NetApp/netAppAccounts/capacityPools"
    MICROSOFT_NET_APP_NET_APP_ACCOUNTS_CAPACITY_POOLS_VOLUMES = "Microsoft.NetApp/netAppAccounts/capacityPools/volumes"
    MICROSOFT_NET_APP_NET_APP_ACCOUNTS_CAPACITY_POOLS_VOLUMES_SNAPSHOTS = "Microsoft.NetApp/netAppAccounts/capacityPools/volumes/snapshots"

class CheckQuotaNameResourceTypes(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Resource type used for verification.
    """

    MICROSOFT_NET_APP_NET_APP_ACCOUNTS = "Microsoft.NetApp/netAppAccounts"
    MICROSOFT_NET_APP_NET_APP_ACCOUNTS_CAPACITY_POOLS = "Microsoft.NetApp/netAppAccounts/capacityPools"
    MICROSOFT_NET_APP_NET_APP_ACCOUNTS_CAPACITY_POOLS_VOLUMES = "Microsoft.NetApp/netAppAccounts/capacityPools/volumes"
    MICROSOFT_NET_APP_NET_APP_ACCOUNTS_CAPACITY_POOLS_VOLUMES_SNAPSHOTS = "Microsoft.NetApp/netAppAccounts/capacityPools/volumes/snapshots"

class CreatedByType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class EndpointType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates whether the local volume is the source or destination for the Volume Replication
    """

    SRC = "src"
    DST = "dst"

class InAvailabilityReasonType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """:code:`<code>Invalid</code>` indicates the name provided does not match Azure App Service
    naming requirements. :code:`<code>AlreadyExists</code>` indicates that the name is already in
    use and is therefore unavailable.
    """

    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"

class MirrorState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The status of the replication
    """

    UNINITIALIZED = "Uninitialized"
    MIRRORED = "Mirrored"
    BROKEN = "Broken"

class QosType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The qos type of the pool
    """

    #: qos type Auto.
    AUTO = "Auto"
    #: qos type Manual.
    MANUAL = "Manual"

class RelationshipStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Status of the mirror relationship
    """

    IDLE = "Idle"
    TRANSFERRING = "Transferring"

class ReplicationSchedule(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Schedule
    """

    _10_MINUTELY = "_10minutely"
    HOURLY = "hourly"
    DAILY = "daily"

class SecurityStyle(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The security style of volume, default unix, defaults to ntfs for dual protocol or CIFS protocol
    """

    NTFS = "ntfs"
    UNIX = "unix"

class ServiceLevel(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The service level of the file system
    """

    #: Standard service level.
    STANDARD = "Standard"
    #: Premium service level.
    PREMIUM = "Premium"
    #: Ultra service level.
    ULTRA = "Ultra"
