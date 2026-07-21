from pathlib import Path

from template_renderer import TemplateRenderer


class ProblemReadmeBuilder:

    def __init__(self):
        self.template = (
            Path(__file__).resolve().parent.parent
            / "templates"
            / "PROBLEM_README_TEMPLATE.md"
        ).read_text(encoding="utf-8")

    def build(
        self,
        problem_path,
        metadata,
        code,
        ai_text,
    ):
        """
        Generate README.md for a single LeetCode problem.
        """

        # Convert LeetCode HTML to Markdown
        markdown = TemplateRenderer.to_markdown(
            metadata["content"]
        )

        # Extract Follow Up (if present)
        follow_up = TemplateRenderer.follow_up(markdown).strip()

        if follow_up:
            follow_up = (
                "\n---\n\n"
                "# 💡 Follow Up\n\n"
                f"{follow_up}\n"
            )
        else:
            follow_up = ""

        # Placeholder values
        placeholders = {
            "{{ID}}": str(metadata["id"]),
            "{{TITLE}}": metadata["title"],
            "{{DIFFICULTY}}": metadata["difficulty"],
            "{{ACCEPTANCE}}": str(metadata["acceptance"]),
            "{{TOPIC_COUNT}}": str(len(metadata["topics"])),
            "{{TOPICS}}": ", ".join(metadata["topics"]),

            "{{PROBLEM_STATEMENT}}":
                TemplateRenderer.problem_statement(markdown).strip(),

            "{{EXAMPLES}}":
                TemplateRenderer.examples(markdown).strip(),

            "{{CONSTRAINTS}}":
                TemplateRenderer.constraints(markdown).strip(),

            "{{FOLLOW_UP}}":
                follow_up,

            "{{AI_EXPLANATION}}":
                ai_text.strip(),

            "{{CPP_CODE}}":
                code.strip(),
        }

        # Fill template
        readme = self.template

        for placeholder, value in placeholders.items():
            readme = readme.replace(
                placeholder,
                str(value),
            )

        # Save README
        output = Path(problem_path) / "README.md"

        output.write_text(
            readme,
            encoding="utf-8",
        )

        print(f"✅ Generated README -> {problem_path}")