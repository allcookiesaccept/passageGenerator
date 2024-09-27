from .client import GPTClient
from src.data import anchors


class PassageGenerator:

    def __init__(self, gpt_client: GPTClient):
        self.gpt_client = gpt_client

    def generate_passages(self, num_passages=10):
        prompt = (
            f"Представь, что ты русскоязычный seo-специалист, "
            f"которому необходимо подготовить несколько тысяч пассажей, разделенных на 3 части: "
            f"текст перед ссылкой, пассаж с анкором, текст после ссылки. Список ссылок таков {anchors}. "
            f"Пример ожидаемого пассажей: "
            f"Текст перед ссылкой: Хотите делать ставки с комфортом? "
            f"Пассаж с анкором: Скачать винлайн можно быстро и бесплатно с официального сайта букмекера. "
            f"Текст после анкора: Получите доступ ко всем функциям БК на своем смартфоне. "
            f"Необходимо сгенерировать {num_passages} подобных пассажей."
        )

        result = self.gpt_client.send_request(prompt)

        passages = [tuple(result.split("Пассаж с анкором: ")) for _ in range(num_passages)]

        return passages