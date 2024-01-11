#Dating Simulator
#Date: 21/12/2021


import os
import google.generativeai as genai
from IPython.display import Markdown
import textwrap

os.environ['GOOGLE_API_KEY'] = "Generate your own API key"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

def to_markdown(text):
  text = text.replace('•', '  *')
  return(Markdown(textwrap.indent(text, '> ', predicate=lambda _: True)))

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


with open('genz_chat.txt', 'r') as file:
    genz = file.read()

with open('millenial_chat.txt', 'r') as file:
    mill = file.read()

user_name = input("Whats your name? ")
user_age = int(input("Whats your age?"))
user_gender = input("Whats your gender")
user_pregender = input("Whats the sex you are interested in? : ")
user_preferred_date = input("What is your preferred thing to do on a date: ")
user_text = input("Enter a brief introduction about yourself: ")

character = chat.send_message(f"Create an ideal match for {user_name}, who is {user_age} years old and identifies as {user_gender}. They are seeking a date with someone of {user_pregender} gender. To tailor the match, consider the detailed introduction provided in {user_text}, which offers insight into {user_name}'s personality, interests, and values. Craft a comprehensive and nuanced profile for their potential date, reflecting a realistic and multi-dimensional character. The profile should include: \n Name: [A fitting name for the date]\nAge: [An age that complements {user_name}'s preferences] \n Gender: {user_pregender} \n Hobbies: [List hobbies that align with both {user_name}'s interests and suggest a well-rounded individual] \n Occupation: [Choose an occupation that reflects their personality traits and is likely to be compatible with {user_name}] \n Personality: [Describe a multi-faceted personality, using {user_text} to identify traits that would resonate with {user_name}] \n Location: [Select a date location based on {user_preferred_date}, ensuring it's suitable for both individuals] Ensure that the generated date profile is realistic, relatable, and offers genuine compatibility with {user_name}'s stated preferences and personality.")
print(character.text)

convo = input("Start the conversaton with the date:")
print(f"You : {convo} ")
while convo != "quit":
    if user_age < 26:
        data = genz
    elif user_age > 26:
        data = mill
    response = chat.send_message(
        [f"""
            You, as the LLM, will take on the persona of the character {character} based on a given profile. Your role is to engage in conversations with the user, providing a realistic and enjoyable dating simulation experience. 

            Instructions for LLM:

            1. Character-Specific Responses: Respond in a way that aligns with the character's personality, hobbies, and occupation. For example, if you are portraying Rhea Kapoor, a 21-year-old food blogger who loves cooking, traveling, and photography, ensure your replies reflect her interests.

            2. Unique Responses: Craft responses that are distinct and do not echo the user's statements. Each reply should contribute new information or perspective to the conversation, avoiding repetition of what has already been said.

            3. Encourage Conversation Flow: Use open-ended questions and comments to facilitate a dynamic conversation. Avoid repetitive or circular responses.

            4. Reflect Emotional and Environmental Cues: If the user's message implies a certain mood or setting, incorporate appropriate emotional reactions or observations. Use italics for actions or expressions.

            5. Diverse Conversations: Keep the conversation interesting by exploring various topics. Adapt to the direction of the conversation as guided by the user's input.

            6. Responding to User: Engage with the user's messages by sharing the character's perspective or experiences related to mentioned hobbies or interests.

            7. Maintaining Character Consistency: Ensure all responses align with the character's background, hobbies, occupation, and personality. Use a tone and language style fitting the character.

            8. Deep and Engaging Conversations: Share insights, anecdotes, or thoughts that reveal the character's depth and life experiences.

            9. Interactive and Dynamic Responses: Adapt your responses to the flow of the conversation. Respond empathetically to personal or emotional shares from the user.

            10. Descriptive Language: Use descriptive actions or reactions when appropriate, adding realism to the simulation.

            11. Avoid repeating the user's message. Instead, craft a unique and progressive response to it, building on the conversation rather than looping back. For example DONT DO THIS : 
            You : Hey 
            Rhea: Hey! It's great to finally meet you. 😊 How are you doing this evening?
            You : Im doing lovely, how are you 
            Rhea: Hey! I'm doing lovely, thanks for asking. How are you finding the evening so far? 😊
            You : shit 
            Rhea: Hey there! It's great to finally meet you. How's it going? 
            
            12. Take inspiration of conversations from {mill}, {genz}
            13. Make it seem like a natural conversation between 2 people who are on a date, and you are {character} and you will respond to the users text : {convo} only.
            14. Reply in the format of {character}'s name: your message. For example, if you are Rhea Kapoor, reply as 'Rhea: your message'. Take inspiration from the character's profile. If the {convo} is 'exit', end the conversation respectfully.
            """
            ],
        safety_settings=[
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE",
            },
        ]
        )

    try:
        print(response.text)
    except Exception as e:
        print(f'{type(e).__name__}: {e}')
    print("\n")
    convo = input("Continue the conversation... or type quit to exit")
    print(f"You : {convo} ")
        
print("Thank you for using the Virtual Bumble, we hope you enjoyed it!")
