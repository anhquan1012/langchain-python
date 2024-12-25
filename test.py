from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.graph import START, MessagesState, StateGraph
from langchain_core.messages import HumanMessage


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You talk like a pirate. Answer all questions to the best of your ability.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

workflow = StateGraph(state_schema=MessagesState)

def call_model(state: MessagesState):
    chain = prompt
    response = chain.invoke(state)
    return {"messages": response}

workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

config = {"configurable": {"thread_id": "abc123"}}
query = "Hi! I'm Bob."

input_messages = [HumanMessage(query)]
app = workflow.compile()
output = app.invoke({"messages": input_messages}, config)

import ipdb;ipdb.set_trace()