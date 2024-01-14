from openai_api import OpenAI_API

class QualityAssuranceAgent:
    def __init__(self, api_key):
        self.api = OpenAI_API(api_key)

    def review_summary(self, summary):
        # Use GPT-4 to review and adjust the summary
        refined_summary = self.api.refine_summary(summary)
        return refined_summary