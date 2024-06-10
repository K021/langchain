# import getpass
# import os

# os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")

import openai
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

model = ChatOpenAI(model="gpt-3.5-turbo")

messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

try:
    response = model.invoke(messages)
except openai.AuthenticationError as e:
    print("Authentication error. Please check your OpenAI API key.")
else:
    print(response)
