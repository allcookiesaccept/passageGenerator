import openai

class GPTClient:

    def __init__(self, api_key, organization):
        openai.api_key = api_key
        openai.organization = organization

    def send_request(self, prompt, model="gpt-4o-mini", max_tokens=4000, temperature=0.7):
        response = openai.ChatCompletion.create(
            engine=model,
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=temperature,
        )
        return response.choices[0].text.strip()