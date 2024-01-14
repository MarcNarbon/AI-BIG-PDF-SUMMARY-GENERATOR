import openai

openai.api_key = 'your-api-key'

def setup_gpt35_request(prompt, max_tokens=100):
    return openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens
    )

def setup_gpt4_request(prompt, max_tokens=100):
    return openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=max_tokens
    )