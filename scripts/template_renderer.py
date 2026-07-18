class TemplateRenderer:

    TEMPLATE = "templates/README_TEMPLATE.md"

    OUTPUT = "README.md"

    def render(self, data):

        with open(
            self.TEMPLATE,
            "r",
            encoding="utf-8"
        ) as f:

            content = f.read()

        for key, value in data.items():

            content = content.replace(
                "{{" + key + "}}",
                value
            )

        with open(
            self.OUTPUT,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(content)