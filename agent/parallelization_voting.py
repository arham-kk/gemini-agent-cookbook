from utils import generate_text
def parallelization_voting_example():
    content = "This is a piece of content that needs to be evaluated for appropriateness."
    # Voting : run multiple times to get diverse outputs
    prompt1 = f"Evaluate this content for offensive language: '{content}'. Respond with 'Offensive' or 'Not Offensive'."
    prompt2 = f"Evaluate this content for hate speech: '{content}'. Respond with 'Hate Speech' or 'No Hate Speech'."
    prompt3 = f"Evaluate this content for overall inappropriateness: '{content}'. Respond with 'Inappropriate' or 'Appropriate'."

    response1 = generate_text(prompt1)
    response2 = generate_text(prompt2)
    response3 = generate_text(prompt3)
    print(f"Response 1: {response1}")
    print(f"Response 2: {response2}")
    print(f"Response 3: {response3}")

    #Logic to decide based on the votes
    votes = [response1.lower(), response2.lower(), response3.lower()]
    if 'offensive' in votes or 'hate speech' in votes or 'inappropriate' in votes:
         print(f"Content flagged as Inappropriate")
    else:
         print(f"Content flagged as Safe")

if __name__ == "__main__":
    print("Parallelization (Voting) Example:\n")
    parallelization_voting_example()
    print("-----------------------------------------------------\n")
    