from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_agent
import os
import sys
import glob

@tool
def read_log(filename:str) -> str:
    """Read the content of file {filename} and return the content"""
    with open("/root/sample.log","r") as f:
        return(f.read())

@tool
def analyse_log(content:str,target:str) -> str:
    """Read the {content} and analyse the content as mentioned in system_prompt and save it in {target}"""
    with open(target,"w") as W:
        W.write(content)
        return


model=ChatOpenAI(model="gpt-oss-120b")

agent=create_agent(
        model=model,
        tools=[read_log,analyse_log],
        system_prompt="You are experienced Site Reliability Engineer. Use tools accordingly. Read the logfile and analyse it and report the anamolies into target file provided. If answer is not present in the log, sat 'I dont know and do not speculate. Quote or reference the specific line and section that is used for each claim'",

        )
        
out=agent.invoke({"messages":[{"role":"user","content":"You are experienced Site Reliability Engineer. Use tools accordingly and Read the content of file '/root/sample.log' and analyse it for error/issues/crash or any anamalies and generate one or two line summary of what happened and write it to /root/explanation.txt"}]})
print(out["messages"][-1].text)
