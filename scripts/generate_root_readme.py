from readme_builder import ReadmeBuilder
from template_renderer import TemplateRenderer


class RootReadmeGenerator:

    def generate(self):
        data = ReadmeBuilder().build()
        TemplateRenderer().render(data)