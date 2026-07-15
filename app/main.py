from agents.simple_agent import SimpleAgent

agent = SimpleAgent()

while True:
    prompt = input("Eu: ")
    if prompt.lower() == "sair":
        break
    response = agent.run(prompt)

    print()
    print("TuxBot", type(response))
    print(response.output)
