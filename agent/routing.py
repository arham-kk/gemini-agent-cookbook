from utils import generate_text

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

if __name__ == "__main__":
    print("Routing Example:\n")
    routing_example()
    print("-----------------------------------------------------\n")