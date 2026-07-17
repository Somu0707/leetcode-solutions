from prompt_template import README_PROMPT


class AIGenerator:

    @staticmethod
    def generate(problem_name, code):

        prompt = README_PROMPT.format(
            problem_name=problem_name
        )

        print(prompt)

        print("\n\n========== CODE ==========\n")

        print(code[:300])

        return "AI generation will happen here."
