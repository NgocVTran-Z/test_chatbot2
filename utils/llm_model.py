import os
from langchain_openai import AzureChatOpenAI


os.environ["AZURE_OPENAI_API_KEY"] = ""
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://--.openai.azure.com/"

# model
llm = AzureChatOpenAI(
    openai_api_version="2023-05-15",
    azure_deployment="apac-gpt-35-turbo",
    temperature=0.8
)
