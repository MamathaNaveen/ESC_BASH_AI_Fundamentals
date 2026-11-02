
# AI_Fundamentals
ESC BASH_Certification_SelfCodedProjects
Project: support ticket triage tool
You are an engineer at esc bash. The support inbox is overflowing and nobody has time to read every message just to route it. Your job is to build a tool that does the first pass automatically.

Set up the project
Run this to drop a folder of real-looking support tickets at /root/tickets/:

bash
What to build
Turn each raw ticket into a small, structured record a dashboard could load: what kind of issue it is, and how urgent it looks.

Write a tool that reads every ticket in /root/tickets/ and, for each one, asks a model to classify it and return JSON with at least these two fields:
category - one of billing, technical, account, or other
priority - one of low, medium, or high
Save each result to /root/triaged/ in a file named after the ticket, with a .json extension (so tickets/deploy-500.txt produces triaged/deploy-500.json).
Every .json file must be valid JSON that jq can parse and must contain both fields.
This pulls together what you have practiced: a clear, specific prompt, asking for structured JSON output, and looping the call over many inputs from code. Keep the prompt strict so the model returns only JSON.

Press Submit once every ticket in /root/tickets/ has a matching, valid JSON result in /root/triaged/.

