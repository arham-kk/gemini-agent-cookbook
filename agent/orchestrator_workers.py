from utils import generate_text

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

if __name__ == "__main__":
    print("Orchestrator Workers Example:\n")
    orchestrator_workers_example()
    print("-----------------------------------------------------\n")
    