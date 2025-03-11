# A simple api app with multiple routes to interact with mutiple different model. Different model has different capabilities and limitations
# For this example we are going to use OpenAi gpt_4o-mini, Llama-3.3-70B-Instruct and DeepSeek-V3
# We are using the LangChain framework to implement the api. 

# Model Name: gpt_4o-mini, Llama-3.3-70B-Instruct and DeepSeek-V3
# Usage Rate limit tier = High
# ----------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------

## Import Statements
from fastapi import FastAPI
from langserve import add_routes
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import uvicorn
import os
from dotenv import load_dotenv

### Getting keys and tokens from Environment veriables. 
#Setting the OPENAI_API_KEY in the environ make the key accessible from ChatOpenAI class below. 
os.environ['OPENAI_API_KEY'] = os.getenv('GITHU_ACEESS_KEY')

### Setting Constants or Global Veriables
github_base_url = "https://models.inference.ai.azure.com"


### Create a FastAPI app
app = FastAPI(title='API Hub', version='1.0',description='A Simple API Server')

### Create a Promt using the Prompt Template
prompt_openai = ChatPromptTemplate.from_messages(
    [
        ("system","You are a knowledgeable tutor who only help users for writing and analyzing programing code. Please dont assist user on anything else. "
                 "If there is a request for doing anything else please gently let them know that you will not be able to assist them on that." ),
        ("user","Question:{question}")
    ]
)

### Create a Promt using the Prompt Template
prompt_llama = ChatPromptTemplate.from_messages(
    [
        ("system","You are a knowledgeable translator who can translate the given text from English to Bengali. Please dont assist user on anything else. "
                 "If there is a request for doing anything else please gently let them know that you will not be able to assist them on that." ),
        ("user","Question:{question}")
    ]
)

### Create different llm objects
llm_openai = ChatOpenAI(model="gpt-4o-mini",base_url=github_base_url)

llm_llama = ChatOpenAI(model="Llama-3.3-70B-Instruct",base_url=github_base_url)


### Creating routes for accessing different models through apis. Add ing the models into the app and setting the path for them
add_routes(
    app,
    prompt_openai|llm_openai,
    path="/tutor"
)

add_routes(
    app,
    prompt_llama|llm_llama,
    path="/translator"
)

### To run the application use : python3 api_app.py
### To check the swagger UI for Documentation : http://localhost:8000/docs

if __name__ == "__main__":
    uvicorn.run(app,host="localhost", port=8000)