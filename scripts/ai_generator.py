import re
import time

from google import genai

from config import GEMINI_API_KEY, MODEL_NAME
from prompt_template import README_PROMPT


class AIGenerator:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    @staticmethod
    def clean_response(text: str) -> str:
        """
        Clean Gemini output before inserting it into README.
        """

        text = text.strip()

        # Remove duplicate top-level heading if Gemini generates one
        text = re.sub(
            r"^#\s*.*?(?:Solution Explanation|Explanation).*?\n+",
            "",
            text,
            flags=re.IGNORECASE,
        )

        # Remove leading horizontal rule
        text = re.sub(
            r"^---\s*\n+",
            "",
            text,
        )

        # Collapse excessive blank lines
        text = re.sub(
            r"\n{3,}",
            "\n\n",
            text,
        )

        return text.strip()

    def generate(self, metadata, code):

        prompt = README_PROMPT.format(
            problem_name=metadata["title"],
            difficulty=metadata["difficulty"],
            problem_content=metadata["content"],
            code=code,
        )

        retries = 3

        for attempt in range(retries):
            try:

                response = self.client.models.generate_content(
                    model=MODEL_NAME,
                    contents=prompt,
                )

                time.sleep(1)

                return self.clean_response(response.text)

            except Exception:

                if attempt == retries - 1:
                    raise

                print(
                    f"⚠️ Gemini unavailable. Retrying ({attempt + 1}/{retries})..."
                )

                time.sleep(5)