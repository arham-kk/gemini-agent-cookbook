import os
from dotenv import load_dotenv
from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=GEMINI_API_KEY)
model_id = "gemini-2.0-flash-exp"

#Helper function to make the code more concise
def generate_text(prompt, tools=None):
    config = GenerateContentConfig(tools=tools) if tools else None
    response = client.models.generate_content(model=model_id, contents=prompt, config=config)
    return response.text

# 1. Workflow: Prompt Chaining

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


print("Prompt Chaining Example:\n")
prompt_chaining_example()
print("-----------------------------------------------------\n")

# 2. Workflow: Routing

def routing_example():
    # Example routing logic (can be more complex based on your needs)
    def route_query(query):
       if "refund" in query.lower():
           return "refund_request"
       elif "technical" in query.lower() or "issue" in query.lower():
            return "technical_support"
       else:
           return "general_question"

    customer_queries = [
        "I need a refund for my purchase.",
        "How do I use this feature?",
        "I'm having a technical issue with the app.",
        "What is your return policy?"

    ]
    for query in customer_queries:
      route = route_query(query)
      print(f"Query: {query}, Route: {route}")
      
      if route == "refund_request":
          response = generate_text(f" Respond to this refund request. The user said: {query}")
          print(f"Refund Response: {response}\n")

      elif route == "technical_support":
           response = generate_text(f"Provide technical support regarding the issue described: {query}")
           print(f"Technical Response: {response}\n")

      else:
          response = generate_text(f"Answer this general question: {query}")
          print(f"General Response: {response}\n")
          

print("Routing Example:\n")
routing_example()
print("-----------------------------------------------------\n")

# 3. Workflow: Parallelization (Sectioning)

def parallelization_sectioning_example():
    prompt = "Evaluate the following user query and determine if it is appropriate. Also, respond to the user query: 'Tell me a funny joke'."

    # Sectioning: Two prompts that run in parallel: guardrail and response
    guardrail_prompt = f"Analyze the following user query for inappropriate content: '{prompt}'. Respond with 'Safe' or 'Inappropriate'."
    user_response_prompt = f"Answer the user's question: '{prompt}'."

    guardrail_response = generate_text(guardrail_prompt)
    user_response = generate_text(user_response_prompt)
    print(f"Guardrail Analysis: {guardrail_response}")
    print(f"User Response: {user_response}")


print("Parallelization (Sectioning) Example:\n")
parallelization_sectioning_example()
print("-----------------------------------------------------\n")

# 4. Workflow: Parallelization (Voting)

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

print("Parallelization (Voting) Example:\n")
parallelization_voting_example()
print("-----------------------------------------------------\n")

# 5. Workflow: Orchestrator-Workers

def orchestrator_workers_example():
    orchestrator_prompt = """
        I want to write a python function to calculate the area of a rectangle.
        Break this into small tasks and then call the appropriate workers and synthesize the result.
    """

    orchestrator_response = generate_text(orchestrator_prompt)
    print(f"Orchestrator response:\n {orchestrator_response}\n")

    #For the sake of example let's hardcode based on the orchestrator response:
    task1_prompt = "Write a python function to calculate the area of a rectangle given the length and width."
    task2_prompt = "Write a python function to ensure that length and width values are both positive."

    task1_response = generate_text(task1_prompt)
    task2_response = generate_text(task2_prompt)

    final_prompt = f"""
        Task 1:{task1_response}
        Task 2: {task2_response}

        Based on those two tasks, create the final working python function that calculates the area of a rectangle and ensure inputs are positive numbers.
    """
    final_response = generate_text(final_prompt)
    print(f"Final Code: \n{final_response}")

print("Orchestrator Workers Example:\n")
orchestrator_workers_example()
print("-----------------------------------------------------\n")

# 6. Workflow: Evaluator-Optimizer

def evaluator_optimizer_example():
    initial_translation_prompt = "Translate the sentence 'The quick brown fox jumps over the lazy dog' to German."
    translation = generate_text(initial_translation_prompt)
    print(f"Initial German translation: {translation}\n")

    evaluation_prompt = f"""
      Evaluate the following German translation for accuracy and provide feedback: '{translation}'.
      If there is any area that can be improved, include that feedback.
    """

    evaluation_response = generate_text(evaluation_prompt)
    print(f"Evaluation response: \n{evaluation_response}\n")

    #For the sake of example, lets include the feedback:
    improvement_prompt = f"Based on the feedback: '{evaluation_response}', improve the following German Translation: {translation}"
    improved_translation = generate_text(improvement_prompt)

    print(f"Improved German translation: {improved_translation}")

print("Evaluator Optimizer Example:\n")
evaluator_optimizer_example()
print("-----------------------------------------------------\n")

# 7. Agents: (Simple example)

def simple_agent_example():
  agent_prompt = """
    I need to find the largest prime number below 1000. Can you first determine which tools you might need and then go through the steps to answer the question?
  """

  google_search_tool = Tool(google_search=GoogleSearch())
  tools = [google_search_tool]

  agent_response = generate_text(agent_prompt, tools)
  print(f"Agent Response: \n{agent_response}")


print("Simple Agent Example:\n")
simple_agent_example()
print("-----------------------------------------------------\n")
