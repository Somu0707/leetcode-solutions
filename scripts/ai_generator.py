from google import genai

from config import GEMINI_API_KEY, MODEL_NAME
from prompt_template import README_PROMPT


class AIGenerator:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate(self, metadata, code):

        prompt = README_PROMPT.format(
            problem_name=metadata["title"],
            difficulty=metadata["difficulty"],
            problem_content=metadata["content"],
            code=code
        )

        response = self.client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        return response.text