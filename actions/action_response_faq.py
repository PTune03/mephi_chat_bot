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


