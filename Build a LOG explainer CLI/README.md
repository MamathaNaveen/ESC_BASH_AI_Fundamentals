Project: log explainer CLI
You are on call at esc bash. An alert fires at 2am and you are staring at a wall of log lines. Build the tool you wish you had: point it at a log file and get back a short, human explanation of what went wrong.
Set up the project
Run this to drop a realistic log file at /root/sample.log:

What to build
Write a command-line tool at /root/explain.py that takes a log file path, reads the file, and asks a model to explain it. Give the model a clear role (an experienced site reliability engineer) and ask for two things in plain English: a one or two sentence summary of what happened, and the most likely cause.
Run your tool on /root/sample.log and save its output to /root/explanation.txt.
This combines a role prompt, grounding the answer in the actual log text you pass in, and wrapping a model call in a small reusable CLI. Keep the log text inside the user message so the model explains this log, not a generic one.

Press Submit once /root/explain.py exists and /root/explanation.txt holds its explanation of /root/sample.log.
