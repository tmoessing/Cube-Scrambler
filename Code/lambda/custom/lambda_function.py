"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""


from __future__ import print_function
import random



# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, content, speech_output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>" + speech_output + "</speak>"
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': content
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_speechlet_response_with_image(title, content, speech_output, reprompt_text, should_end_session):

    smallImageUrl = 'https://s3.amazonaws.com/bojo-creatures/' + creature_caught + 'Small.png'
    largeImageUrl = 'https://s3.amazonaws.com/bojo-creatures/' + creature_caught + 'Large.png'
    
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': '<speak>' + speech_output + '</speak>'
        },
        'card': {
            'type': 'Standard',
            'title': title,
            'text': content,
            'image': {
                'smallImageUrl': smallImageUrl,
                'largeImageUrl': largeImageUrl
            }
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def handle_launch_request(session):
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title      = "Welcome"
    card_content    = "Welcome to Rubik's Puzzles Scrambler, what type of puzzle do you want me to scramble?"                      \


    speech_output   =  "Welcome to Rubik's Puzzles Scrambler, what type of puzzle do you want me to scramble?"                      \


    reprompt_text   =  "Go ahead and ask me, if you need help just ask! "                                  \

    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))



def handle_ThreeByThree_intent(intent_name, session):
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    possibilitiesArray = ['R','R inverted', 'R2',
                          'L','L inverted', 'L2',
                          'B','B inverted', 'B2',
                          'D','D inverted', 'D2',
                          'F','F inverted', 'F2',
                          'U','U inverted', 'U2']
                          

    picks = []
    count = 0
    previous_value = "None"
    while count < 25:
        current_value = random.choice(possibilitiesArray)
        if  current_value != previous_value:
            if  current_value[0] != previous_value[0]:
                picks.append(current_value)
                previous_value = current_value
                count += 1  # This is the same as count = count + 11

    scramble = ", <break time='750ms'/> ".join([str(x) for x in picks] )
    scramble1 = ", ".join([str(x) for x in picks] )

    session_attributes = {}
    card_title      = "3x3 Scramble"
    card_content    =  scramble1
                  
    speech_output   = "Alright! Here is your 3 by 3 scramble, " + scramble                 \
    


    reprompt_text   =  "Go ahead and ask me, if you need help just ask! "                                  \

    should_end_session = True

    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))


def handle_TwoByTwo_intent(intent_name, session):
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    possibilitiesArray = ['R','R inverted', 'R2',
                          'L','L inverted', 'L2',
                          'B','B inverted', 'B2',
                          'D','D inverted', 'D2',
                          'F','F inverted', 'F2',
                          'U','U inverted', 'U2']


    picks = []
    count = 0
    previous_value = "None"
    while count < 9:
        current_value = random.choice(possibilitiesArray)
        if  current_value != previous_value:
            if  current_value[0] != previous_value[0]:
                picks.append(current_value)
                previous_value = current_value
                count += 1  # This is the same as count = count + 11

    scramble = ", <break time='750ms'/> ".join([str(x) for x in picks] )
    scramble1 = ", ".join([str(x) for x in picks] )

    session_attributes = {}
    card_title      = "2x2 Scramble"
    card_content    =  scramble1
                  
    speech_output   = "Alright! Here is your 2 by 2 scramble, " + scramble                 \
    


    reprompt_text   =  "Go ahead and ask me, if you need help just ask! "                                  \

    should_end_session = True

    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))

def handle_Pyraminx_intent(intent_name, session):
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    

    possibilitiesArray = ['U','U inverted', 'L','L inverted','R','R inverted', 'B','B inverted']

    
    
    picks = []
    count = 0
    previous_value = "nothing"
    while count < 8:
        current_value = random.choice(possibilitiesArray)
        if  current_value != previous_value:
            if  current_value[0] != previous_value[0]:
                picks.append(current_value)
                previous_value = current_value
                count += 1  # This is the same as count = count + 11


    scramble = ", <break time='750ms'/> ".join([str(x) for x in picks] )
    scramble1 = ", ".join([str(x) for x in picks] )
    
    upossibilitiesArray = [ "small u", "small u inverted" ]
    lpossibilitiesArray = [ "small l", "small l inverted" ]
    rpossibilitiesArray = [ "small r", "small r inverted" ]
    bpossibilitiesArray = [ "small b", "small b inverted" ]
        
    smallpicks = []
    current_u_value = random.choice(upossibilitiesArray)   
    current_l_value = random.choice(lpossibilitiesArray)
    current_r_value = random.choice(rpossibilitiesArray)
    current_b_value = random.choice(bpossibilitiesArray)
    smallpicks.append(current_u_value)
    smallpicks.append(current_l_value)
    smallpicks.append(current_r_value)
    smallpicks.append(current_b_value)


    small  = ", <break time='750ms'/> ".join([str(x) for x in smallpicks] )
    small1 = ", ".join([str(x) for x in smallpicks] )

    session_attributes = {}
    card_title      = "Pyraminx Scramble"
    card_content    =  small1 + ", " + scramble1
                  
    speech_output   = "Alright! Here is your Pyraminx scramble, " + small + ", <break time='750ms'/>" + scramble              \


    reprompt_text   =  "Go ahead and ask me, if you need help just ask! "                                  \

    should_end_session = True

    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))

def handle_Megaminx_intent(intent_name, session):
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    possibilitiesArray = ["D minus minus","D++","R minus minus","R++",]
    upossibilitiesArray = ["U inverted","U"]
    realpossibilitiesArray = ["D minus minus","D++","R minus minus","R++","U inverted","U"]


    picks = []
    count = 0
    previous_value = "None"
    while count < 77:
        current_value = random.choice(realpossibilitiesArray)
        if  current_value != previous_value:
            if  current_value[0] != previous_value[0]:
                picks.append(current_value)
                previous_value = current_value
                count += 1  # This is the same as count = count + 11    


    scramble1 = ", ".join([str(x) for x in picks] )
    scramble = ", <break time='750ms'/>".join([str(x) for x in picks] )

    session_attributes = {}
    card_title      = "Megaminx Scramble"
    card_content    =  scramble1
                  
    speech_output   = "Alright! Here is your Megaminx scramble, " + scramble                 \
    
    reprompt_text   =  "Go ahead and ask me, if you need help just ask! "                                  \

    should_end_session = True

    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))


def handle_Void_intent(intent_name, session):
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    possibilitiesArray = ['R','R inverted', 'R2',
                          'L','L inverted', 'L2',
                          'B','B inverted', 'B2',
                          'D','D inverted', 'D2',
                          'F','F inverted', 'F2',
                          'U','U inverted', 'U2']
                          

    picks = []
    count = 0
    previous_value = "None"
    while count < 25:
        current_value = random.choice(possibilitiesArray)
        if  current_value != previous_value:
            if  current_value[0] != previous_value[0]:
                picks.append(current_value)
                previous_value = current_value
                count += 1  # This is the same as count = count + 11

    scramble = ", <break time='750ms'/> ".join([str(x) for x in picks] )
    scramble1 = ", ".join([str(x) for x in picks] )

    session_attributes = {}
    card_title      = "Void Cube Scramble"
    card_content    =  scramble1
                  
    speech_output   = "Alright! Here is your Void Cube scramble, " + scramble                 \
    

    reprompt_text   =  "Go ahead and ask me, if you need help just ask! "                                  \

    should_end_session = True

    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))




def handle_help_intent(intent_name, session):

    session_attributes = {}
    card_title      = "Help"
    card_content    = "So far I can scramble a 3 by 3, 2 by 2, Pyraminx, Megaminx, and a Void cube."

    speech_output   = "So far I can scramble a 3 by 3, 2 by 2, Pyraminx, Megaminx, and a Void cube, "               \
                    + "Say any of those for a randomized scramble. "                                \
                    + "<break time='750ms'/>If the cube you want is not listed, suggest it in the comments in the skill store. "

    reprompt_text   = "Say, 'scramble my 3x3' "

    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))

def handle_end_intent():

    session_attributes = {}
    card_title      = "Good bye"
    card_content    = "Goodbye, come for another scramble soon"

    speech_output   = "Goodbye, come for another scramble soon"

    should_end_session = True

    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, None, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])

def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return handle_launch_request(session)


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "ThreeByThreeIntent" :
        return handle_ThreeByThree_intent(intent_name, session)
    elif intent_name == "TwobyTwoIntent" :
        return handle_TwoByTwo_intent(intent_name,session)
    elif intent_name == "MegaminxIntent" :
        return handle_Megaminx_intent(intent_name,session)
    elif intent_name == "VoidIntent" :
        return handle_Void_intent(intent_name,session)
    elif intent_name == "PyraminxIntent" :
        return handle_Pyraminx_intent(intent_name,session)
    elif intent_name == "AMAZON.HelpIntent" :
        return handle_help_intent(intent_name,session)
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_end_intent()
    else:
        print("what the what is " + intent_name)
        raise ValueError("Invalid intent")

def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    if (event['session']['application']['applicationId'] !=
             "amzn1.ask.skill.9d25964e-f5a2-49d9-b10c-346769d85e04"):
         raise ValueError("Invalid Application ID")
    

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},event['session'])
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
