import openai

class SummaryAgent:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def summarize(self, document_segment):
        response = openai.Completion.create(
            engine="text-davinci-003.5",
            prompt=document_segment,
            temperature=0.3,
            max_tokens=150
        )
        return response.choices[0].text.strip()