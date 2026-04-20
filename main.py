import ollama

model = 'huihui_ai/qwen2.5-abliterate:7b-instruct'
print(f"Iniciando chat com {model}. Digite 'sair' para encerrar.")

messages = []

while True:
    user_input = input("\nVocê: ")

    if user_input.lower() in ['sair', 'exit', 'quit']:
        print("Encerrando chat. Até mais!")
        break

    messages.append({'role': 'user', 'content': user_input})

    response = ollama.chat(
        model=model,
        messages=messages,
        stream=True
    )

    print("Ollama: ", end="", flush=True)

    bot_response = ""

    for chunk in response:
        content = chunk['message']['content']
        print(content, end="", flush=True)
        bot_response += content

    print()  # quebra de linha

    messages.append({'role': 'assistant', 'content': bot_response})