# Get pass OpenAI API key from user input
# import getpass
# import os
# os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")

from dotenv import load_dotenv

import openai
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
# from langsmith import traceable

load_dotenv("secrets/.env")

model = ChatOpenAI(model="gpt-3.5-turbo")
str_parser = StrOutputParser()
chain = model | str_parser

messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

# traceable 을 직접 호출하지 않아도, ChatOpenAI 의 인스턴스의 input output 이 자동으로 로깅된다.
# @traceable
def invoke(messages):
    try:
        response = chain.invoke(messages)
    except openai.AuthenticationError as e:
        print("Authentication error. Please check your OpenAI API key.")
    
    print(response)


if __name__ == "__main__":
    invoke(messages)