from ollama import chat
from ollama import *

stream = chat(
    model='huihui_ai/qwen2.5-abliterate:7b-instruct',
    messages=[{'role': 'user', 'content': 'desliga meu pc por favor!'}],
    stream=True
)
for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)