from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn 
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="AI Sensing",
    description="API for AI Sensing",
    version="1.0"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)
model = ChatOpenAI()


#checks if imported or not
if __name__ == "__main__": 
    #executed only if run as a script and not imported
    uvicorn.run(app, host="localhost", port=8000)