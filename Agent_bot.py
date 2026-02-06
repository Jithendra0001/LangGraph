##### Define state variable with a list of HumanMessage objects
##### Initialize a GPT-4o model using LangChain's ChatOpenAI
##### Sending and handling different types of messages
##### Building and compiling the graph of the Agent


from typing import TypedDict, List
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()

class AgentState(TypedDict):
    messages: List[HumanMessage]

llm = ChatOpenAI(model="gpt-4o")

def process(state: AgentState) ->AgentState:
    response = llm.invoke(state['messages'])
    print(f"\nAI: {response.content}")
    return state

graph = StateGraph(AgentState)
graph.add_node('process', process)
graph.add_edge(START, "process")
graph.add_edge("process",END)

agent = graph.compile()

# user_input = input("ENTER: ")

##single message
# agent.invoke({'messages': [HumanMessage(content=user_input)]})

##Multiple message

user_input = input("Enter: ")
while user_input != "exit":
    agent.invoke({"messages": [HumanMessage(content=user_input)]})
    user_input = input("Enter: ")


### This agent doesn't store the history of messages.
### Try

"""
AI: 2 + 2 equals 4.
Enter: Hi, I am jithendra.

AI: Hello, Jithendra! How can I assist you today?
Enter: What is my name?

AI: I'm sorry, but I cannot determine your name based on the information provided.
Enter: exit

"""