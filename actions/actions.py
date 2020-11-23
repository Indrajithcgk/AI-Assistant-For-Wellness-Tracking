# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class HealthForm(FormAction):

    def name(self):
        return ("health_form")

    @staticmethod
    def required_slots(tracker):

        if tracker.get_slot("confirm_exercise")== True:
            return ["confirm_exercise","exercise","diet","sleep","stress","goal"]
        else:
            return ["confirm_exercise","diet","sleep","stress","goal"]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text,Any],
    )    -> List[Dict]:
            return []

    def slot_mapping(self) -> Dict[Text,Union[Dict, List[Dict]]]:
        return {
            "confirm_exercise": [
                self.from_intent(intent="affirm",value=True),
                self.from_intent(intent="deny",value=False),
                self.from_intent(intent="inform", value=True),
            ],
            "sleep": [
                self.from_entity(entity="sleep"),
                self.from_intent(intent="deny",value="None"),

            ],
            "diet": [
                self.from_text(intent="inform"),
                self.from_text(intent="affirm"),
                self.from_text(intent="deny"),
            ],
            "goal": [
                self.from_text(intent="inform"),
            ]

        }


