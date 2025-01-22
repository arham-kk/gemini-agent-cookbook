# Gemini Agentic Workflows

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains Python code demonstrating various agentic workflow patterns using the Gemini 2.0 API and the Google Gen AI SDK. These examples are inspired by the [Building effective agents](https://www.anthropic.com/research/building-effective-agents) article from Anthropic, adapted for the Google Gemini platform.

## Overview

This project explores the implementation of agentic systems with Gemini, focusing on the building blocks and workflow patterns described in the Anthropic article. The key idea is to build effective applications by starting with simple prompts and gradually adding complexity, using agentic workflows when simpler solutions aren't sufficient.

The following patterns are implemented:

1.  **Prompt Chaining:** Decomposing a task into a sequence of steps, where each LLM call uses the output of the previous one.
2.  **Routing:** Classifying an input and directing it to a specialized task or LLM call.
3.  **Parallelization:** Running multiple LLM calls simultaneously:
    *   **Sectioning:** Breaking a task into independent subtasks for concurrent execution.
    *   **Voting:** Running the same task multiple times to get diverse outputs and improve the final result.
4.  **Orchestrator-Workers:** A central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes results.
5.  **Evaluator-Optimizer:** One LLM generates a response while another provides evaluation and feedback in a loop.
6.  **Simple Agents:** LLMs using tools based on environmental feedback in a loop for autonomous tasks.

## Getting Started

### Prerequisites

*   Python 3.8 or higher
*   A Google AI Gemini API key (get one from [Google AI Studio](https://aistudio.google.com/app/apikey))

### Installation

1.  Clone this repository:

    ```bash
    git clone https://github.com/arham-kk/gemini-agent-cookbook.git
    cd gemini-agent-cookbook
    ```
2.  Install the required Python packages:

     ```bash
    pip install -r requirements.txt
    ```
     
3. **Set up your API key:**

   *    Add your Gemini API key to the `.env` file in the following format:

        ```
        GEMINI_API_KEY=your_api_key_here
        ```

## License

This project is licensed under the MIT License

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.
