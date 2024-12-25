
# %%
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser


# %%
model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="Hello, my name is H")
]

# %%
res = model.invoke(messages)

print(res)
# %%
parser.invoke(res)

# %%
chain = model | parser
chain.invoke(messages)
# %%
from langchain_core.prompts import ChatPromptTemplate

system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)
result = prompt_template.invoke({"language": "italian", "text": "hi"})

# %%
result.to_messages()
#%%
chain = prompt_template | model | parser
chain.invoke({"language": "italian", "text": "Hello, my name is H"})

