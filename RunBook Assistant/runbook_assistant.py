rom langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
import sys
import os

@tool
def read_md(path:str) -> str:
    """ Read md file from {path} and return content."""
    with open(path,"r") as f:
        return(f.read())


modelname="gpt-oss-120b"
model=ChatOpenAI(model=modelname)

agent=create_agent(
        model=model,
        tools=[read_md],
        system_prompt="You are helpfull assistant, Use the tool accordingly to answer user queries. The location of runbook is '/root/runbook.md'. Stay grounded and answer from the docuemnt. if the document does not cover it, say so rather than guessing"
        )
op=agent.invoke({"messages":[{"role":"user","content":sys.argv[1]}]})
print(op["messages"][-1].text)
