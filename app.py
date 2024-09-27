from settings import logger, DataManager
import openai



class GPTBot:
    def __init__(self):
        self.data_manager = DataManager.get_instance()
        openai.api_key = self.data_manager.GPT.token
        openai.organization = self.data_manager.GPT.organization


    def get_response(self, prompt, model="text-davinci-003", max_tokens=150):
        try:
            response = openai.Completion.create(
                engine=model,
                prompt=prompt,
                max_tokens=max_tokens,
                n=1,
                stop=None,
                temperature=0.7,
            )
            return response
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            return None

    def _request_generator(self):
        ...
