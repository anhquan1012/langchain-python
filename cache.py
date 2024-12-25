#%%
from langchain.globals import set_llm_cache
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# To make the caching really obvious, lets use a slower model.
llm = OpenAI(model_name="gpt-3.5-turbo-instruct", n=2, best_of=2)
#%%
from langchain.cache import InMemoryCache

set_llm_cache(InMemoryCache())

# The first time, it is not yet in cache, so it should take longer
llm.predict("Tell me a joke")

# %%
llm.invoke("Tell me 2 jokes about natural and human")

# %%
