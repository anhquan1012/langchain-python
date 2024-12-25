#%%
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI, OpenAI
llm = ChatOpenAI()
llm2 = OpenAI()
question = "What is after Monday?"

#%%
llm.invoke(question)    
# %%
llm2.invoke(question)