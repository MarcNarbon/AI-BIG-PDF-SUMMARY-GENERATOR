from openai_api import GPT4

class IntegratorAgent:
    def __init__(self):
        self.gpt4 = GPT4()

    def refine_summary(self, summary):
        refined_summary = self.gpt4.generate_summary(summary)
        return refined_summary