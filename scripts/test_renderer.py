from metadata_handler import MetadataHandler
from template_renderer import TemplateRenderer


metadata = MetadataHandler.load("0001-two-sum")

markdown = TemplateRenderer.to_markdown(
    metadata["content"]
)

print("=" * 80)
print("FULL MARKDOWN")
print("=" * 80)
print(markdown)

print()

print("=" * 60)
print("PROBLEM")
print("=" * 60)
print(
    TemplateRenderer.problem_statement(markdown)
)

print()

print("=" * 60)
print("EXAMPLES")
print("=" * 60)
print(
    TemplateRenderer.examples(markdown)
)

print()

print("=" * 60)
print("CONSTRAINTS")
print("=" * 60)
print(
    TemplateRenderer.constraints(markdown)
)

print()

print("=" * 60)
print("FOLLOW UP")
print("=" * 60)
print(
    TemplateRenderer.follow_up(markdown)
)