from utils import generate_text

def parallelization_sectioning_example():
    prompt = "Evaluate the following user query and determine if it is appropriate. Also, respond to the user query: 'Tell me a funny joke'."

    # Sectioning: Two prompts that run in parallel: guardrail and response
    guardrail_prompt = f"Analyze the following user query for inappropriate content: '{prompt}'. Respond with 'Safe' or 'Inappropriate'."
    user_response_prompt = f"Answer the user's question: '{prompt}'."

    guardrail_response = generate_text(guardrail_prompt)
    user_response = generate_text(user_response_prompt)
    print(f"Guardrail Analysis: {guardrail_response}")
    print(f"User Response: {user_response}")

if __name__ == "__main__":
    print("Parallelization (Sectioning) Example:\n")
    parallelization_sectioning_example()
    print("-----------------------------------------------------\n")
    