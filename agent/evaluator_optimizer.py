from utils import generate_text
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

if __name__ == "__main__":
    print("Evaluator Optimizer Example:\n")
    evaluator_optimizer_example()
    print("-----------------------------------------------------\n")
    