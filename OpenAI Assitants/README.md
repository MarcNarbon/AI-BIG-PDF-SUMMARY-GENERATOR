# My OpenAI Project

This project uses Python and the OpenAI Assistants API to segment, summarize, refine, and review PDF documents. It is structured in a modular way to maintain organization and clarity.

## Project Structure

The project is structured into several directories and files:

- `/agents`: Contains individual modules for each type of agent.
- `/utils`: Holds utility functions and common tools.
- `/communication`: Manages inter-agent communication.
- `main.py`: The main script that orchestrates the workflow.

## Detailed Architecture

### /agents

- `document_segmenter.py`: Contains the DocumentSegmenter class to handle PDF segmentation. It includes functions to read a PDF and split it into sections.
- `summary_agent.py`: Contains the SummaryAgent class for GPT-3.5-based summarization. It includes functions for receiving document segments and returning summaries.
- `integrator_agent.py`: Contains the IntegratorAgent class using GPT-4 for summary refinement. It includes functions to compile and refine summaries.
- `quality_assurance_agent.py`: Contains the QualityAssuranceAgent class also using GPT-4. It includes functions for final review and adjustment of the summary.

### /utils

- `openai_api.py`: Contains wrapper functions for interacting with the OpenAI API. It includes functions for setting up GPT-3.5 and GPT-4 requests.
- `pdf_tools.py`: Contains utility functions for PDF parsing.

### /communication

- `message_queue.py`: Contains an implementation of a message queue or a similar mechanism for agent communication. It includes functions for sending and receiving messages between agents.

### main.py

This script orchestrates the entire process. It creates instances of each agent and manages their interactions. It handles the initial input (PDF file) and outputs the final summary.

## Usage

To use this project, run the `main.py` script with a PDF file as input. The script will segment the document, summarize each segment, refine the summaries, and review the final summary before outputting it.

## Dependencies

This project requires Python and the OpenAI Assistants API. Please refer to the official OpenAI documentation for installation and usage instructions.