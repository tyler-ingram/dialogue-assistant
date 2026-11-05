from llm import ask, GENERATE_DIALOGUE_PROMPT
if __name__ == "__main__":
    prompt = "Generate a dialogue between two characters in a fantasy setting."
    system_prompt = GENERATE_DIALOGUE_PROMPT
    response = ask(prompt, system=system_prompt)
    print(response)