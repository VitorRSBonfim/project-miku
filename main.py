from ollama import chat
from ollama import *

stream = chat(
    model='huihui_ai/qwen2.5-abliterate:7b-instruct',
    messages=[{'role': 'user', 'content': 'como funciona um holograma?'}],
    stream=True
)
for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)