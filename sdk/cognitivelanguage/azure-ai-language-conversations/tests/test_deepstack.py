# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import pytest

from azure.core.exceptions import HttpResponseError, ClientAuthenticationError
from azure.core.credentials import AzureKeyCredential

from testcase import (
    ConversationTest,
    GlobalConversationAccountPreparer
)

from azure.ai.language.conversations import ConversationAnalysisClient
from azure.ai.language.conversations.models import (
    ConversationAnalysisInput,
    ConversationAnalysisResult,
    DeepstackPrediction
)


class DeepstackAnalysisTests(ConversationTest):

    @GlobalConversationAccountPreparer()
    def test_analysis(self, conv_account, conv_key, conv_project):

        # prepare data
        query = "One california maki please."
        input = ConversationAnalysisInput(
            query=query,
        )

        # run quey
        client = ConversationAnalysisClient(conv_account, AzureKeyCredential(conv_key))
        with client:
            result = client.analyze_conversations(
                input,
                project_name=conv_project,
                deployment_name='production'
            )
        
        # assert
        assert isinstance(result, ConversationAnalysisResult)
        assert result.query == query
        assert isinstance(result.prediction, DeepstackPrediction)
        assert result.prediction.project_kind == 'conversation'
        assert len(result.prediction.entities) > 0
        assert len(result.prediction.intents) > 0
        assert result.prediction.top_intent == 'Order'
        assert result.prediction.intents[0].category == 'Order'
        assert result.prediction.intents[0].confidence_score > 0
        assert result.prediction.entities[0].category == 'OrderItem'
        assert result.prediction.entities[0].text == 'california maki'
        assert result.prediction.entities[0].confidence_score > 0
        

    @GlobalConversationAccountPreparer()
    def test_analysis_with_dictparams(self, conv_account, conv_key, conv_project):
        client = ConversationAnalysisClient(conv_account, AzureKeyCredential(conv_key))
        params = {
            "query": "One california maki please.",
        }

        with client:
            result = client.analyze_conversations(
                params,
                project_name=conv_project,
                deployment_name='production'
            )
        
        assert isinstance(result, ConversationAnalysisResult)
        assert result.query == "One california maki please."
        assert isinstance(result.prediction, DeepstackPrediction)
        assert result.prediction.project_kind == 'conversation'
        assert len(result.prediction.entities) > 0
        assert len(result.prediction.intents) > 0
        assert result.prediction.top_intent == 'Order'
        assert result.prediction.intents[0].category == 'Order'
        assert result.prediction.intents[0].confidence_score > 0
        assert result.prediction.entities[0].category == 'OrderItem'
        assert result.prediction.entities[0].text == 'california maki'
        assert result.prediction.entities[0].confidence_score > 0
 