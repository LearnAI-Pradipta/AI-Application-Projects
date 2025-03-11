# A Simple Chatbot app to get your query resolved.
# Using OpenAi model we are going to create a chatbot application. 
# We are using the LangChain framework to implement the ChatBot. 

# Model Name: gpt-4o-mini
# Usage Rate limit tier = Low
# ----------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------

## Import Statements
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import find_dotenv,load_dotenv
import streamlit as st

### Getting keys and tokens from Environment veriables. 
#Setting the OPENAI_API_KEY in the environ make the key accessible from ChatOpenAI class below. 
os.environ['OPENAI_API_KEY'] = os.getenv('GITHU_ACEESS_KEY')

### Setting Constants or Global Veriables
github_base_url = "https://models.inference.ai.azure.com"

#### ToDo: Create a new LangChain API Key and Use the Langchain Tracing (LangSmith) feature to know about the Langchain call we are making. Source : https://www.youtube.com/watch?v=5CJA1Hbutqc&list=PLZoTAELRMXVOQPRG7VAuHL--y97opD5GQ&index=3

### Create a Promt using the Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant that translates English to Bengali. Translate the user sentence. Please dont do anything else apart from translation."),
        ("user","Question:{question}")
    ]
)

### Define the Streamlit framework
st.title('LangChain Demo with OPENAI API')
input_text = st.text_input('Provide an input')


### Create the llm object by mentioning the model name and the base url. 
### The api_key is getting from OPENAI_API_KEY environment veriable.
llm = ChatOpenAI(model="gpt-4o-mini",base_url=github_base_url)


### Creating a output parser and creating a chain of prompt, llm and output parser to invoke the LLM model
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))