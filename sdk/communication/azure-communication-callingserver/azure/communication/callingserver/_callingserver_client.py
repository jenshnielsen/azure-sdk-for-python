# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
# pylint: disable=too-many-public-methods
from typing import TYPE_CHECKING, Any, List, Optional  # pylint: disable=unused-import
from azure.core.tracing.decorator import distributed_trace
from azure.core.pipeline.transport import HttpResponse
from azure.core.exceptions import (
    HttpResponseError,
    map_error
)

from .utils._utils import CallingServerUtils
from ._content_downloader import ContentDownloader
from ._download import ContentStreamDownloader

from ._communication_identifier_serializer import serialize_identifier
from ._communication_call_locator_serializer import serialize_call_locator
from ._generated._azure_communication_calling_server_service import \
    AzureCommunicationCallingServerService
from ._generated.models import (
    CreateCallRequest,
    PhoneNumberIdentifierModel,
    PlayAudioResult,
    AddParticipantResult,
    CallRecordingProperties,
    StartCallRecordingWithCallLocatorRequest,
    StartCallRecordingResult,
    RecordingContentType,
    RecordingChannelType,
    RecordingFormatType,
    CallParticipant,
    CallMediaType,
    CallingEventSubscriptionType,
    AnswerCallResult,
    CallRejectReason
    )

from ._shared.models import CommunicationIdentifier
from ._call_connection import CallConnection
from ._converters import (
    JoinCallRequestConverter,
    AnswerCallRequestConverter,
    RejectCallRequestConverter,
    RedirectCallRequestConverter,
    PlayAudioWithCallLocatorRequestConverter,
    PlayAudioToParticipantWithCallLocatorRequestConverter,
    AddParticipantWithCallLocatorRequestConverter,
    RemoveParticipantWithCallLocatorRequestConverter,
    CancelMediaOperationWithCallLocatorRequestConverter,
    CancelParticipantMediaOperationWithCallLocatorRequestConverter,
    GetAllParticipantsWithCallLocatorRequestConverter,
    GetParticipantWithCallLocatorRequestConverter,
    MuteParticipantWithCallLocatorRequestConverter,
    UnmuteParticipantWithCallLocatorRequestConverter,
    HoldMeetingAudioWithCallLocatorRequestConverter,
    ResumeMeetingAudioWithCallLocatorRequestConverter
    )
from ._shared.utils import get_authentication_policy, get_host_header_policy, parse_connection_str
from ._version import SDK_MONIKER

if TYPE_CHECKING:
    from azure.core.credentials import TokenCredential
    from ._models import (
        CreateCallOptions,
        JoinCallOptions,
        PlayAudioOptions,
        ParallelDownloadOptions,
        CallLocator
    )

class CallingServerClient(object):
    """A client to interact with the AzureCommunicationService Calling Server.

    This client provides calling operations.

    :param str endpoint:
        The endpoint url for Azure Communication Service resource.
    :param TokenCredential credential:
        The TokenCredential we use to authenticate against the service.

    .. admonition:: Example:

        .. literalinclude:: ../samples/identity_samples.py
            :language: python
            :dedent: 8
    """

    def __init__(
        self,
        endpoint,  # type: str
        credential,  # type: TokenCredential
        **kwargs  # type: Any
    ):  # type: (...) -> None
        try:
            if not endpoint.lower().startswith('http'):
                endpoint = "https://" + endpoint
        except AttributeError:
            raise ValueError("Account URL must be a string.")

        if not credential:
            raise ValueError(
                "You need to provide account shared key to authenticate.")

        self._endpoint = endpoint
        self._callingserver_service_client = AzureCommunicationCallingServerService(
            self._endpoint,
            headers_policy=get_host_header_policy(endpoint, credential),
            authentication_policy=get_authentication_policy(endpoint, credential),
            sdk_moniker=SDK_MONIKER,
            **kwargs)

        self._call_connection_client = self._callingserver_service_client.call_connections
        self._server_call_client = self._callingserver_service_client.server_calls

    @classmethod
    def from_connection_string(
        cls,
        conn_str,  # type: str
        **kwargs  # type: Any
    ):  # type: (...) -> CallingServerClient
        """Create CallingServerClient from a Connection String.

        :param str conn_str:
            A connection string to an Azure Communication Service resource.
        :returns: Instance of CallingServerClient.
        :rtype: ~azure.communication.callingserver.CallingServerClient

        .. admonition:: Example:

            .. literalinclude:: ../samples/callingserver_sample.py
                :start-after: [START auth_from_connection_string]
                :end-before: [END auth_from_connection_string]
                :language: python
                :dedent: 8
                :caption: Creating the CallingServerClient from a connection string.
        """
        endpoint, access_key = parse_connection_str(conn_str)

        return cls(endpoint, access_key, **kwargs)

    def get_call_connection(
        self,
        call_connection_id  # type: str
    ):  # type: (...) -> CallConnection
        """Initializes a new instance of CallConnection.

        :param str call_connection_id:
           The thread id for the ChatThreadClient instance.
        :returns: Instance of CallConnection.
        :rtype: ~azure.communication..callingserver.CallConnection
        """
        if not call_connection_id:
            raise ValueError("call_connection_id can not be None")

        return CallConnection(call_connection_id, self._call_connection_client)

    @distributed_trace()
    def create_call_connection(
        self,
        source,  # type: CommunicationIdentifier
        targets,  # type: List[CommunicationIdentifier]
        options,  # type: CreateCallOptions
        **kwargs  # type: Any
    ):  # type: (...) -> CallConnection
        """Create an outgoing call from source to target identities.

        :param CommunicationIdentifier source:
           The source identity.
        :param List[CommunicationIdentifier] targets:
           The target identities.
        :param CreateCallOptions options:
           The call options.
        :returns: CallConnection for a successful creating callConnection request.
        :rtype: ~azure.communication.callingserver.CallConnection
        """
        if not source:
            raise ValueError("source can not be None")

        if not targets:
            raise ValueError("targets can not be None or empty")

        if not options:
            raise ValueError("options can not be None")

        request = CreateCallRequest(
            source=serialize_identifier(source),
            targets=[serialize_identifier(m) for m in targets],
            callback_uri=options.callback_uri,
            requested_media_types=options.requested_media_types,
            requested_call_events=options.requested_call_events,
            alternate_caller_id=(None
                if options.alternate_Caller_Id is None
                else PhoneNumberIdentifierModel(value=options.alternate_Caller_Id.properties['value'])),
            subject=options.subject
        )

        create_call_response = self._call_connection_client.create_call(
            call_request=request,
            **kwargs
        )

        return CallConnection(create_call_response.call_connection_id, self._call_connection_client)  # pylint:disable=protected-access

    @distributed_trace()
    def join_call(
        self,
        call_locator,  # type: CallLocator
        source,  # type: CommunicationIdentifier
        call_options,  # type: JoinCallOptions
        **kwargs  # type: Any
    ):  # type: (...) -> CallConnection
        """Join the call using call_locator.

        :param CallLocator call_locator:
           The callLocator.
        :param CommunicationIdentifier targets:
           The source identity.
        :param JoinCallOptions options:
           The call Options.
        :returns: CallConnection for a successful join request.
        :rtype: ~azure.communication.callingserver.CallConnection
        """
        if not call_locator:
            raise ValueError("call_locator can not be None")
        if not source:
            raise ValueError("source can not be None")
        if not call_options:
            raise ValueError("call_options can not be None")

        join_call_request = JoinCallRequestConverter.convert(
            call_locator=serialize_call_locator(call_locator),
            source=serialize_identifier(source),
            join_call_options=call_options
            )

        join_call_response = self._server_call_client.join_call(
            call_request=join_call_request,
            **kwargs
        )

        return CallConnection(
            join_call_response.call_connection_id,
            self._call_connection_client
            )

    @distributed_trace()
    def answer_call(
        self,
        incoming_call_context,  # type: str
        callback_uri=None,  # type: str
        requested_media_types=None,  # type: List[CallMediaType]
        requested_call_events=None,  # type: List[CallingEventSubscriptionType]
        **kwargs  # type: Any
    ):  # type: (...) -> AnswerCallResult

        if not incoming_call_context:
            raise ValueError("incoming_call_context can not be None")

        answer_call_request = AnswerCallRequestConverter.convert(
            incoming_call_context=incoming_call_context,
            callback_uri=callback_uri,
            requested_media_types=requested_media_types,
            requested_call_events=requested_call_events
            )

        return self._server_call_client.answer_call(
            answer_call_request=answer_call_request,
            **kwargs
        )

    @distributed_trace()
    def reject_call(
        self,
        incoming_call_context,  # type: str
        call_reject_reason=None,  # type: CallRejectReason
        callback_uri=None,  # type: str
        **kwargs  # type: Any
    ):  # type: (...) -> None

        if not incoming_call_context:
            raise ValueError("incoming_call_context can not be None")

        reject_call_request = RejectCallRequestConverter.convert(
            incoming_call_context=incoming_call_context,
            call_reject_reason=call_reject_reason,
            callback_uri=callback_uri
            )

        return self._server_call_client.reject_call(
            reject_call_request=reject_call_request,
            **kwargs
        )

    @distributed_trace()
    def redirect_call(
        self,
        incoming_call_context,  # type: str
        targets,  # type: List[CommunicationIdentifier]
        callback_uri=None,  # type: str
        timeout_in_seconds=None,  # type: int
        **kwargs  # type: Any
    ):  # type: (...) -> None

        if not incoming_call_context:
            raise ValueError("incoming_call_context can not be None")

        redirect_call_request = RedirectCallRequestConverter.convert(
            incoming_call_context=incoming_call_context,
            target_identities=[serialize_identifier(m) for m in targets],
            callback_uri=callback_uri,
            timeout_in_seconds=timeout_in_seconds
            )

        return self._server_call_client.redirect_call(
            redirect_call_request=redirect_call_request,
            **kwargs
        )

    @distributed_trace()
    def play_audio(
        self,
        call_locator,  # type: CallLocator
        audio_url,  # type: str
        play_audio_options,  # type: PlayAudioOptions
        **kwargs  # type: Any
    ):  # type: (...) -> PlayAudioResult

        play_audio_request = PlayAudioWithCallLocatorRequestConverter.convert(
            call_locator=serialize_call_locator(call_locator),
            audio_url=audio_url,
            play_audio_options=play_audio_options
            )

        return self._server_call_client.play_audio(
            play_audio_request=play_audio_request,
            **kwargs
        )

    @distributed_trace()
    def play_audio_to_participant(
        self,
        call_locator,  # type: CallLocator
        participant,  # type: CommunicationIdentifier
        audio_url,  # type: str
        play_audio_options,  # type: PlayAudioOptions
        **kwargs  # type: Any
    ):  # type: (...) -> PlayAudioResult

        play_audio_to_participant_request = PlayAudioToParticipantWithCallLocatorRequestConverter.convert(
            call_locator=serialize_call_locator(call_locator),
            identifier=serialize_identifier(participant),
            audio_url=audio_url,
            play_audio_options=play_audio_options
            )

        return self._server_call_client.participant_play_audio(
            play_audio_to_participant_request=play_audio_to_participant_request,
            **kwargs
        )

    @distributed_trace()
    def add_participant( # pylint: disable=too-many-arguments
        self,
        call_locator,  # type: CallLocator
        participant,  # type: CommunicationIdentifier
        callback_uri,  # type: str
        alternate_caller_id=None,  # type: Optional[str]
        operation_context=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):  # type: (...) -> AddParticipantResult

        if not call_locator:
            raise ValueError("call_locator can not be None")
        if not participant:
            raise ValueError("participant can not be None")

        alternate_caller_id = (None
            if alternate_caller_id is None
            else PhoneNumberIdentifierModel(value=alternate_caller_id))

        add_participant_with_call_locator_request = AddParticipantWithCallLocatorRequestConverter.convert(
            serialize_call_locator(call_locator),
            serialize_identifier(participant),
            alternate_caller_id=alternate_caller_id,
            operation_context=operation_context,
            callback_uri=callback_uri
            )

        return self._server_call_client.add_participant(
            add_participant_with_call_locator_request=add_participant_with_call_locator_request,
            **kwargs
        )

    @distributed_trace()
    def remove_participant(
        self,
        call_locator,  # type: CallLocator
        participant,  # type: CommunicationIdentifier
        **kwargs  # type: Any
    ): # type: (...) -> None

        if not call_locator:
            raise ValueError("call_locator can not be None")
        if not participant:
            raise ValueError("participant can not be None")

        remove_participant_with_call_locator_request = RemoveParticipantWithCallLocatorRequestConverter.convert(
            serialize_call_locator(call_locator),
            serialize_identifier(participant)
            )

        return self._server_call_client.remove_participant(
            remove_participant_with_call_locator_request=remove_participant_with_call_locator_request,
            **kwargs
        )

    @distributed_trace()
    def get_participants(
            self,
            call_locator,  # type: CallLocator
            **kwargs  # type: Any
        ): # type: (...) -> List[CallParticipant]

        get_all_participants_with_call_locator_request = GetAllParticipantsWithCallLocatorRequestConverter.convert(
            serialize_call_locator(call_locator)
            )

        return self._server_call_client.get_participants(
            get_all_participants_with_call_locator_request=get_all_participants_with_call_locator_request,
            **kwargs
        )

    @distributed_trace()
    def get_participant(
            self,
            call_locator,  # type: CallLocator
            participant,  # type: CommunicationIdentifier
            **kwargs  # type: Any
        ): # type: (...) -> List[CallParticipant]

        get_participant_with_call_locator_request = GetParticipantWithCallLocatorRequestConverter.convert(
            serialize_call_locator(call_locator),
            serialize_identifier(participant)
            )

        return self._server_call_client.get_participant(
            get_participant_with_call_locator_request=get_participant_with_call_locator_request,
            **kwargs
        )

    @distributed_trace()
    def mute_participant(
            self,
            call_locator,  # type: CallLocator
            participant,  # type: CommunicationIdentifier
            **kwargs  # type: Any
        ):  # type: (...) -> None

        if not participant:
            raise ValueError("participant can not be None")

        mute_participant_with_call_locator_request = MuteParticipantWithCallLocatorRequestConverter.convert(
            serialize_call_locator(call_locator),
            serialize_identifier(participant)
            )

        return self._server_call_client.mute_participant(
            mute_participant_with_call_locator_request=mute_participant_with_call_locator_request,
            **kwargs
        )

    @distributed_trace()
    def unmute_participant(
            self,
            call_locator,  # type: CallLocator
            participant,  # type: CommunicationIdentifier
            **kwargs  # type: Any
        ):  # type: (...) -> None

        if not participant:
            raise ValueError("participant can not be None")

        unmute_participant_with_call_locator_request = UnmuteParticipantWithCallLocatorRequestConverter.convert(
            serialize_call_locator(call_locator),
            serialize_identifier(participant)
            )

        return self._server_call_client.unmute_participant(
            unmute_participant_with_call_locator_request=unmute_participant_with_call_locator_request,
            **kwargs
        )

    @distributed_trace()
    def cancel_media_operation(
        self,
        call_locator,  # type: CallLocator
        media_operation_id,  # type: str
        **kwargs  # type: Any
    ): # type: (...) -> None

        if not call_locator:
            raise ValueError("call_locator can not be None")
        if not media_operation_id:
            raise ValueError("media_operation_id can not be None")

        cancel_media_operation_request = CancelMediaOperationWithCallLocatorRequestConverter.convert(
            serialize_call_locator(call_locator),
            media_operation_id=media_operation_id
            )

        return self._server_call_client.cancel_media_operation(
            cancel_media_operation_request=cancel_media_operation_request,
            **kwargs
        )

    @distributed_trace()
    def cancel_participant_media_operation(
        self,
        call_locator,  # type: CallLocator
        participant,  # type: CommunicationIdentifier
        media_operation_id,  # type: str
        **kwargs  # type: Any
    ): # type: (...) -> None

        if not call_locator:
            raise ValueError("call_locator can not be None")
        if not participant:
            raise ValueError("participant can not be None")
        if not media_operation_id:
            raise ValueError("media_operation_id can not be None")

        cancel_participant_media_operation_request = \
        CancelParticipantMediaOperationWithCallLocatorRequestConverter.convert(
            serialize_call_locator(call_locator),
            serialize_identifier(participant),
            media_operation_id=media_operation_id
            )

        return self._server_call_client.cancel_participant_media_operation(
            cancel_participant_media_operation_request=cancel_participant_media_operation_request,
            **kwargs
            )

    @distributed_trace()
    def hold_participant_meeting_audio(
            self,
            call_locator,  # type: CallLocator
            participant,  # type: CommunicationIdentifier
            **kwargs  # type: Any
        ):  # type: (...) -> None

        if not participant:
            raise ValueError("participant can not be None")

        hold_meeting_audio_with_call_locator_request = HoldMeetingAudioWithCallLocatorRequestConverter.convert(
            serialize_call_locator(call_locator),
            serialize_identifier(participant)
            )

        return self._server_call_client.hold_participant_meeting_audio(
            hold_meeting_audio_with_call_locator_request=hold_meeting_audio_with_call_locator_request,
            **kwargs
        )

    @distributed_trace()
    def resume_participant_meeting_audio(
            self,
            call_locator,  # type: CallLocator
            participant,  # type: CommunicationIdentifier
            **kwargs  # type: Any
        ):  # type: (...) -> None

        if not participant:
            raise ValueError("participant can not be None")

        resume_meeting_audio_with_call_locator_request = ResumeMeetingAudioWithCallLocatorRequestConverter.convert(
            serialize_call_locator(call_locator),
            serialize_identifier(participant)
            )

        return self._server_call_client.resume_participant_meeting_audio(
            resume_meeting_audio_with_call_locator_request=resume_meeting_audio_with_call_locator_request,
            **kwargs
        )

    @distributed_trace()
    def start_recording( # pylint: disable=too-many-arguments
        self,
        call_locator,  # type: CallLocator
        recording_state_callback_uri,  # type: str
        recording_content_type=None, # type: Optional[RecordingContentType]
        recording_channel_type=None, # type: Optional[RecordingChannelType]
        recording_format_type=None, # type: Optional[RecordingFormatType]
        **kwargs  # type: Any
    ):  # type: (...) -> StartCallRecordingResult

        start_call_recording_with_calllocator_request = StartCallRecordingWithCallLocatorRequest(
            call_locator=serialize_call_locator(call_locator),
            recording_state_callback_uri=recording_state_callback_uri,
            recording_content_type=recording_content_type,
            recording_channel_type=recording_channel_type,
            recording_format_type=recording_format_type,
            **kwargs
        )

        return self._server_call_client.start_recording(
           start_call_recording_with_call_locator_request=start_call_recording_with_calllocator_request,
            **kwargs
        )

    @distributed_trace()
    def pause_recording(
        self,
        recording_id,  # type: str
        **kwargs  # type: Any
    ):  # type: (...) -> HttpResponse

        return self._server_call_client.pause_recording(
            recording_id=recording_id,
            **kwargs
        )

    @distributed_trace()
    def resume_recording(
        self,
        recording_id,  # type: str
        **kwargs  # type: Any
    ):  # type: (...) -> HttpResponse

        return self._server_call_client.resume_recording(
            recording_id=recording_id,
            **kwargs
        )

    @distributed_trace()
    def stop_recording(
        self,
        recording_id,  # type: str
        **kwargs  # type: Any
    ):  # type: (...) -> HttpResponse

        return self._server_call_client.stop_recording(
            recording_id=recording_id,
            **kwargs
        )

    @distributed_trace()
    def get_recording_properities(
        self,
        recording_id,  # type: str
        **kwargs  # type: Any
    ):  # type: (...) -> CallRecordingProperties

        return self._server_call_client.get_recording_properties(
            recording_id=recording_id,
            **kwargs
        )

    @distributed_trace()
    def download(
        self,
        content_url,  # type: str
        start_range=None,  # type: int
        end_range=None,  # type: int
        parallel_download_options=None,  # type: ParallelDownloadOptions
        **kwargs  # type: Any
    ):  # type: (...) -> ContentStreamDownloader
        """Download using content url.

        :param str content_url:
            The content url.
        :returns: ContentStreamDownloader for a successful download request.
        :rtype: ~ContentStreamDownloader
        """
        if not content_url:
            raise ValueError("content_url can not be None")

        if not CallingServerUtils.is_valid_url(content_url):
            raise ValueError("content_url is invalid")

        # pylint:disable=protected-access
        content_downloader = ContentDownloader(
            self._callingserver_service_client._client,
            self._callingserver_service_client._serialize,
            self._callingserver_service_client._deserialize,
            self._callingserver_service_client._config)

        return ContentStreamDownloader(
            content_downloader,
            self._callingserver_service_client._config,
            start_range,
            end_range,
            endpoint=content_url,
            parallel_download_options=parallel_download_options,
            **kwargs
        )

    @distributed_trace()
    def delete_recording(
        self,
        content_delete_url, # type: str
        **kwargs # type: Any

    ): # type: (...) -> HttpResponse
        # pylint: disable=protected-access
        if not content_delete_url:
            raise ValueError("content_delete_url can not be None")

        url = content_delete_url
        uri_to_sign_with = CallingServerUtils.get_url_to_sign_request_with(self._endpoint, url)

        query_parameters = {} # type: Dict[str, Any]
        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['UriToSignWith'] = self._callingserver_service_client._serialize.header(
            name="uri_to_sign_with",
            data=uri_to_sign_with,
            data_type='str')

        error_map = CallingServerUtils.get_error_response_map(
            kwargs.pop('error_map', {}))
        client = self._callingserver_service_client._client
        request = client.delete(url, query_parameters, header_parameters) #pylint: disable=specify-parameter-names-in-call
        pipeline_response = client._pipeline.run(request, **kwargs)
        response = pipeline_response.http_response
        if response.status_code not in [200]:
            map_error(status_code=response.status_code,
                        response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        return response
