from pathlib import Path

from readme_builder import ReadmeBuilder


class RootReadmeGenerator:

    def __init__(self):
        self.template = (
            Path(__file__).resolve().parent.parent
            / "templates"
            / "README_TEMPLATE.md"
        )

        self.output = (
            Path(__file__).resolve().parent.parent
            / "README.md"
        )

    def generate(self):

        data = ReadmeBuilder().build()

        readme = self.template.read_text(
            encoding="utf-8"
        )

        for key, value in data.items():
            readme = readme.replace(
                "{{" + key + "}}",
                str(value)
            )

        self.output.write_text(
            readme,
            encoding="utf-8"
        )

        print("✅ Root README generated")