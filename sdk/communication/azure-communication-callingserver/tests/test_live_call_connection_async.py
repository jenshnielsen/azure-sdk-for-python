# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import time
import uuid
import os
import pytest
import urllib.parse
from azure.core.credentials import AccessToken
from azure.communication.callingserver.aio import CallingServerClient, CallConnection
from azure.communication.callingserver import (
    PlayAudioOptions,
    PhoneNumberIdentifier,
    CreateCallOptions,
    MediaType,
    EventSubscriptionType,
    CommunicationUserIdentifier
    )
from azure.communication.callingserver._shared.utils import parse_connection_str
from azure.communication.identity.aio import CommunicationIdentityClient
from live_test_utils._test_utils_async import CallingServerLiveTestUtils, Helper
from azure.identity.aio import DefaultAzureCredential
from _shared.asynctestcase  import AsyncCommunicationTestCase
from _shared.testcase import (
    BodyReplacerProcessor, ResponseReplacerProcessor
)
from devtools_testutils import is_live
from _shared.utils import get_http_logging_policy

SKIP_CALLINGSERVER_INTERACTION_LIVE_TESTS = is_live and os.getenv("SKIP_CALLINGSERVER_INTERACTION_LIVE_TESTS", "false") == "true"
CALLINGSERVER_INTERACTION_LIVE_TESTS_SKIP_REASON = "SKIP_CALLINGSERVER_INTERACTION_LIVE_TESTS skips certain callingserver tests that required human interaction"

IncomingRequestSecret = "helloworld"
AppBaseUrl = "https://dummy.ngrok.io"
AppCallbackUrl = f"{AppBaseUrl}/api/incident/callback?SecretKey={urllib.parse.quote(IncomingRequestSecret)}"
AudioFileName = "sample-message.wav"
AudioFileUrl = f"{AppBaseUrl}/audio/{AudioFileName}"

class FakeTokenCredential(object):
    def __init__(self):
        self.token = AccessToken("Fake Token", 0)

    async def get_token(self, *args):
        return self.token

@pytest.mark.skipif(SKIP_CALLINGSERVER_INTERACTION_LIVE_TESTS, reason=CALLINGSERVER_INTERACTION_LIVE_TESTS_SKIP_REASON)
class CallConnectionTestAsync(AsyncCommunicationTestCase):

    def setUp(self):
        super(CallConnectionTestAsync, self).setUp()

        self.from_user = Helper.get_new_user_id(self.connection_str)
        self.to_user = Helper.get_new_user_id(self.connection_str)

        if self.is_playback():
            self.from_phone_number = "+15551234567"
            self.to_phone_number = "+15551234567"
            self.recording_processors.extend([
                BodyReplacerProcessor(keys=["alternateCallerId", "targets", "source", "callbackUri"])])
        else:
            self.to_phone_number = os.getenv("AZURE_PHONE_NUMBER")
            self.from_phone_number = os.getenv("ALTERNATE_CALLERID")
            self.recording_processors.extend([
                BodyReplacerProcessor(keys=["alternateCallerId", "targets", "source", "callbackUri"]),
                ResponseReplacerProcessor(keys=[self._resource_name])])
        
    @AsyncCommunicationTestCase.await_prepared_test
    async def test_create_play_cancel_hangup_scenario_async(self):

        # create CallingServerClient
        endpoint, _ = parse_connection_str(self.connection_str)
        self.endpoint = endpoint

        if not is_live():
            credential = FakeTokenCredential()
        else:
            credential = DefaultAzureCredential()

        self.callingserver_client = CallingServerClient(
            self.endpoint,
            credential,
            http_logging_policy=get_http_logging_policy()
        )

        # create option
        self.options = CreateCallOptions(
            callback_uri=AppCallbackUrl,
            requested_media_types=[MediaType.AUDIO],
            requested_call_events=[EventSubscriptionType.PARTICIPANTS_UPDATED, EventSubscriptionType.DTMF_RECEIVED]
        )
        self.options.alternate_Caller_Id = PhoneNumberIdentifier(self.from_phone_number)

        # Establish a call
        async with self.callingserver_client:
            call_connection_async = await self.callingserver_client.create_call_connection(
                        source=CommunicationUserIdentifier(self.from_user),
                        targets=[PhoneNumberIdentifier(self.to_phone_number)],
                        options=self.options,
                        )

            CallingServerLiveTestUtils.validate_callconnection_Async(call_connection_async)

            if is_live():
                time.sleep(10)

            async with call_connection_async:
                # Play Audio
                OperationContext = str(uuid.uuid4())
                AudioFileId = str(uuid.uuid4())
                options = PlayAudioOptions(
                    loop = True,
                    audio_file_id = AudioFileId,
                    callback_uri = AppCallbackUrl,
                    operation_context = OperationContext
                    )

                play_audio_result = await call_connection_async.play_audio(
                    AudioFileUrl,
                    options
                    )

                CallingServerLiveTestUtils.validate_play_audio_result_Async(play_audio_result)

                # Cancel All Media Operations
                CancelMediaOperationContext = str(uuid.uuid4())
                cancel_all_media_operations_result = await call_connection_async.cancel_all_media_operations(
                    CancelMediaOperationContext
                    )   

                CallingServerLiveTestUtils.validate_cancel_all_media_operations_Async(cancel_all_media_operations_result)
                if is_live():
                    time.sleep(5)

                # Hang up
                await call_connection_async.hang_up()

    @AsyncCommunicationTestCase.await_prepared_test
    async def test_create_add_remove_hangup_scenario_async(self):

        # create CallingServerClient
        endpoint, _ = parse_connection_str(self.connection_str)
        self.endpoint = endpoint

        if not is_live():
            credential = FakeTokenCredential()
        else:
            credential = DefaultAzureCredential()

        self.callingserver_client = CallingServerClient(
            self.endpoint,
            credential,
            http_logging_policy=get_http_logging_policy()
        )

        # create option
        self.options = CreateCallOptions(
            callback_uri=AppCallbackUrl,
            requested_media_types=[MediaType.AUDIO],
            requested_call_events=[EventSubscriptionType.PARTICIPANTS_UPDATED, EventSubscriptionType.DTMF_RECEIVED]
        )
        self.options.alternate_Caller_Id = PhoneNumberIdentifier(self.from_phone_number)

        # Establish a call
        async with self.callingserver_client:
            call_connection_async = await self.callingserver_client.create_call_connection(
                        source=CommunicationUserIdentifier(self.from_user),
                        targets=[PhoneNumberIdentifier(self.to_phone_number)],
                        options=self.options,
                        )

            CallingServerLiveTestUtils.validate_callconnection_Async(call_connection_async)

            if is_live():
                time.sleep(10)

            async with call_connection_async:

                # Add Participant
                OperationContext = str(uuid.uuid4())
                add_participant_result = await call_connection_async.add_participant(
                    participant=CommunicationUserIdentifier(self.to_user),
                    alternate_caller_id=None,
                    operation_context=OperationContext
                    )

                CallingServerLiveTestUtils.validate_add_participant_Async(add_participant_result)

                participant_id=add_participant_result.participant_id

                # Remove Participant
                await call_connection_async.remove_participant(participant_id)

                if is_live():
                    time.sleep(5)

                # Hang up
                await call_connection_async.hang_up()
