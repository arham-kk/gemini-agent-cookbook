from utils import generate_text, Tool, GoogleSearch

def simple_agent_example():
  agent_prompt = """
    I need to find the largest prime number below 1000. Can you first determine which tools you might need and then go through the steps to answer the question?
  """

  google_search_tool = Tool(google_search=GoogleSearch())
  tools = [google_search_tool]

  agent_response = generate_text(agent_prompt, tools)
  print(f"Agent Response: \n{agent_response}")

if __name__ == "__main__":
  print("Simple Agent Example:\n")
  simple_agent_example()
  print("-----------------------------------------------------\n")
  