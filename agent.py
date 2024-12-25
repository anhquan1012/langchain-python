# %%
from dotenv import load_dotenv
load_dotenv()

#%%
from langchain_community.tools.tavily_search import TavilySearchResults

search = TavilySearchResults(max_results=2)
search_results = search.invoke("what is the weather in SF")
print(search_results)
# If we want, we can create other tools.
# Once we have all the tools we want, we can put them in a list that we will reference later.
tools = [search]

#%%
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")
model_with_tools = model.bind_tools(tools)

# %%
from langchain_core.messages import HumanMessage
response = model_with_tools.invoke([HumanMessage(content="Hi!")])

print(f"ContentString: {response.content}")
print(f"ToolCalls: {response.tool_calls}")
# %%
response = model_with_tools.invoke([HumanMessage(content="What's the weather in SF?")])

print(f"ContentString: {response.content}")
print(f"ToolCalls: {response.tool_calls}")
# %%
from langgraph.prebuilt import create_react_agent

agent_executor = create_react_agent(model, tools)
# %%
response = agent_executor.invoke({"messages": [HumanMessage(content="hi!")]})

response["messages"]
# %%
response = agent_executor.invoke(
    {"messages": [HumanMessage(content="whats the weather in sf?")]}
)
response["messages"]
# %%
