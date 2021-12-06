from ruamel.yaml import YAML
import logging
import base64
import os
import urllib.parse as urlparse
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction, EventType, Restarted
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from pathlib import Path
from typing import Dict, Text, Any, List, Optional
from rasa_sdk.executor import CollectingDispatcher
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ruamel_yaml = YAML(typ='safe')
domain_data = ruamel_yaml.load(Path('domain.yml'))


# class ActionShowTime(Action):
#
#     def name(self) -> Text:  # регистрация имени действия
#         return "action_show_time"
#
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # при вызове действия, возвращать ответ с текущим временем:
#         text = tracker.latest_message['text']
#         utter = f'На ваш вопрос "{text}" отвечу: {dt.now().strftime("%H:%M")}'
#         dispatcher.utter_message(text=utter)
#         # dispatcher.utter_message(text=f'Сейчас {dt.now().strftime("%H:%M")}')
#
#         return []


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")

        return []

class ActionFAQ(Action):

    def name(self) -> Text:
        return "action_faq"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain) -> List[EventType]:
        text = tracker.latest_message['text']
        text = text.lower()
        intent = tracker.get_intent_of_latest_message()
        if intent in domain_data.get('answers', {}):
            message = domain_data['answers'][intent]['text']
            utter = f'На ваш вопрос "{text}" отвечу: {message}'
        if not intent:
            return [FollowupAction('action_classification')]

        dispatcher.utter_message(text=utter)

        return [Restarted()]


class ActionClassification(Action):

    def name(self) -> Text:
        return "action_classification"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain) -> List[EventType]:
        dispatcher.utter_message(text="Работает!")

        return [Restarted()]
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions



#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#::q

#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
