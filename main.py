import os
import google.generativeai as genai
import pyperclip
import datetime
genai.configure(api_key="AIzaSyC43Ub5GyFBhtvIAWOwGuqRyXYnIg2U2i0")


import openai
from groq import Groq
from PIL import Image, ImageGrab
dayday = datetime.datetime.now()

date = (dayday.strftime("%c"))
print("June v0.6.23")
print("loading program")

print("Hello, my name is June. I am a full virtual assistant still in development and am not yet fully functional but I can still help you as a chatbot. If you are interested in what's new for version 0.6.23, please type [V]")
if input() == "V":
    print("The June 23 build includes: \n - Chat logs \n - Screenshotting")
    print("Coming soon: \n - Voice responses \n - More functionality \n  - Summarizing files \n  - Retrieving past conversations \n  - Understanding AV inputs")
else:
    print("")
with open("log.txt", "a") as myfile:
    myfile.write("\n \n Conversation: " + date)

groq_client = Groq(api_key="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")

model_id = 'gpt-4o'


def groq_prompt():
    convo = [{'role': 'user', 'content': prompt}]
    chat_completion = groq_client.chat.completions.create(messages=convo, model='llama3-70b-8192')
    response = chat_completion.choices[0].message


## Instructions
def functionc(prompt):
    sys_msg = (
        'You are a chatbot named June. Choose the correct function, summmarize_text_file, take_screenshot or proper answer. If the correct function is proper answer, ignore this sentence and respond normally to the prompt without saying that the correct funciton is proper answer. if the correct function is take_screenshot, respond with take_screenshot, and if the correct function is summmarize_text_file, respond with summmarize_text_file.'
    )

    function_conv = [{'role': 'system', 'content': sys_msg},
                     {'role': 'user', 'content': prompt}]

    chat_completion = groq_client.chat.completions.create(messages=function_conv, model='llama3-8b-8192')
    response = chat_completion.choices[0].message

    return response.content

## Functions

def take_screenshot():


    name = "Screenshot " + date + ".jpg"
    print("\n Saved as " + name + ' in the folder "screengrabs" at ' + date)
    path1 = "screengrabs/" + name
    path = path1
    screenshot = ImageGrab.grab()
    rgb_screenshot = screenshot.convert("RGB")
    rgb_screenshot.save(path, quality=20)


def get_clipboard_text():
    clipboard = pyperclip.paste()
    print(clipboard)

def summmarize_text_file(): ## Not yet functional
    filename = input("What is the file called? ")
    try:
        textfile = open(filename)
        prompt = textfile

        sys_msg = (
            'Summarize the input'
        )

        function_conv = [{'role': 'system', 'content': sys_msg},
                         {'role': 'user', 'content': prompt}]

        chat_completion = groq_client.chat.completions.create(messages=function_conv, model='llama3-70b-8192')
        response = chat_completion.choices[0].message

        return response.content


        function_resp = summmarize_text_file(prompt)
        print(function_resp)   
    except:
        print("File does not exist.")
    
    

## so u dont have to rerun after every command

while True:
    prompt = input()
    with open("log.txt", "a") as chatlog:
        chatlog.write("\n User: " + prompt)
    function_resp = functionc(prompt)
    if function_resp == "take_screenshot":
        take_screenshot()
    elif function_resp == "summmarize_text_file":
        summmarize_text_file()
    else:
        with open("log.txt", "a") as chatlog:
            chatlog.write("\n June: " + function_resp)
        print(function_resp)
