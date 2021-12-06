
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

from datetime import datetime as dt
from typing import Any, Text, Dict, List


class ActionShowTime(Action):

    def name(self) -> Text:  # регистрация имени действия
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # при вызове действия, возвращать ответ с текущим временем:
        text = tracker.latest_message['text']
        utter = f'На ваш вопрос "{text}" отвечу: {dt.now().strftime("%H:%M")}'
        dispatcher.utter_message(text=utter)
        # dispatcher.utter_message(text=f'Сейчас {dt.now().strftime("%H:%M")}')

        return []


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")

        return []


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
