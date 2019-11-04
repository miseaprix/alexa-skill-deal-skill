#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dealabs import Dealabs
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model.ui import SimpleCard

from six import PY2
try:
    from HTMLParser import HTMLParser
except ImportError:
    from html.parser import HTMLParser


################################################

class SSMLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.full_str_list = []
        if not PY2:
            self.strict = False
            self.convert_charrefs = True

    def handle_data(self, d):
        self.full_str_list.append(d)

    def get_data(self):
        return ''.join(self.full_str_list)

################################################

skill_name = "Hot deals"
help_text = ("Vous pouvez demander : "
             "Donne moi les deals du jour")

sb = SkillBuilder()


@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    # Handler for Skill Launch
    speech = "Bienvenue dans le skill Hot deals."

    handler_input.response_builder.speak(
        speech + " " + help_text).ask(help_text)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
    # Handler for Help Intent
    handler_input.response_builder.speak(help_text).ask(help_text)
    return handler_input.response_builder.response


@sb.request_handler(
    can_handle_func=lambda input:
        is_intent_name("AMAZON.CancelIntent")(input) or
        is_intent_name("AMAZON.StopIntent")(input))
def cancel_and_stop_intent_handler(handler_input):
    # Single handler for Cancel and Stop Intent
    speech_text = "Au revoir!"

    return handler_input.response_builder.speak(speech_text).response


@sb.request_handler(can_handle_func=is_request_type("SessionEndedRequest"))
def session_ended_request_handler(handler_input):
    # Handler for Session End
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_intent_name(
    "demande_deals_les_plus_hot"))
def demande_deals_les_plus_hot(handler_input):
    slots = handler_input.request_envelope.request.intent.slots

    if "periode_slot" in slots:
        var = slots["AMAZON.DURATION"].value

    params = {
    	"days": "1", # can be 1, 7 or 30 days
    	"page": "1", # page number
    	"limit":"25" # article per page
    }

    list_p = dealabs.get_deals_hot(params=params)
    if len(liste_p) < 1:
	 speech = "Aucun deal de trouver pour la periode souhaitee {}.".format(var)

    for p in list_p:
	if p is None:
		speech = "Aucun deal de trouver {}.".format(var)
	else:
		speech += "Voici les deals du jour {}".format(p)

    handler_input.response_builder.speak(speech)
    return handler_input.response_builder.response


def convert_speech_to_text(ssml_speech):
    # convert ssml speech to text, by removing html tags
    s = SSMLStripper()
    s.feed(ssml_speech)
    return s.get_data()


@sb.global_response_interceptor()
def add_card(handler_input, response):
    # Add a card by translating ssml text to card content
    response.card = SimpleCard(
        title=skill_name,
        content=convert_speech_to_text(response.output_speech.ssml))


@sb.global_response_interceptor()
def log_response(handler_input, response):
    # Log response from alexa service
    print("Alexa Response: {}\n".format(response))


@sb.global_request_interceptor()
def log_request(handler_input):
    # Log request to alexa service
    print("Alexa Request: {}\n".format(handler_input.request_envelope.request))


@sb.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(handler_input, exception):
    # Catch all exception handler, log exception and
    # respond with custom message
    print("Encountered following exception: {}".format(exception))

    speech = "Désolé, je n'ai pas compris. \
Dite aide pour obtenir des exemples d'utilisation."
    handler_input.response_builder.speak(speech).ask(speech)

    return handler_input.response_builder.response


# Handler to be provided in lambda console.
handler = sb.lambda_handler()
