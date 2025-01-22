from utils import generate_text
def prompt_chaining_example():
    prompt1 = "Generate a short marketing copy for a new AI-powered language learning app."
    response1 = generate_text(prompt1)
    print(f"Response 1:\n{response1}\n")

    prompt2 = f"Translate the following marketing copy into Spanish:\n{response1}"
    response2 = generate_text(prompt2)
    print(f"Response 2 (Translated):\n{response2}\n")
    
    prompt3 = f"Write a simplified version of the Spanish marketing copy aimed at children. \n {response2}"
    response3 = generate_text(prompt3)
    print(f"Response 3 (Translated for Children):\n{response3}\n")


if __name__ == "__main__":
    print("Prompt Chaining Example:\n")
    prompt_chaining_example()
    print("-----------------------------------------------------\n")
    