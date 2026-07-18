from collections import Counter

from scanner import RepositoryScanner
from metadata_handler import MetadataHandler


class ReadmeBuilder:

    def __init__(self):
        self.scanner = RepositoryScanner()

    def _progress_data(self, total):
        milestones = [100, 250, 500, 1000]

        for milestone in milestones:
            if total < milestone:
                target = milestone
                break
        else:
            target = ((total // 500) + 1) * 500

        percentage = round((total / target) * 100, 1)

        filled = int(percentage // 5)
        bar = "█" * filled + "░" * (20 - filled)

        return {
            "target": target,
            "percentage": percentage,
            "bar": bar
        }

    def build(self):

        problems = self.scanner.scan()

        total = len(problems)

        easy = medium = hard = 0
        acceptance_sum = 0.0

        topic_counter = Counter()

        table = [
            "| # | Problem | Difficulty | Acceptance | Topics | README |",
            "|---:|---------|------------|-----------:|--------|:------:|"
        ]

        recent = []

        for problem in problems:

            metadata = MetadataHandler.load(problem)

            number = metadata["id"].zfill(4)
            title = metadata["title"]
            difficulty = metadata["difficulty"]
            acceptance = metadata["acceptance"]
            topics = metadata["topics"]

            acceptance_sum += acceptance

            for topic in topics:
                topic_counter[topic] += 1

            if difficulty == "Easy":
                easy += 1
                badge = "🟢 Easy"
            elif difficulty == "Medium":
                medium += 1
                badge = "🟠 Medium"
            else:
                hard += 1
                badge = "🔴 Hard"

            topic_string = ", ".join(topics[:3])

            table.append(
                f"| {number} | [{title}](./{problem}/README.md) | {badge} | {acceptance:.2f}% | {topic_string} | ✅ |"
            )

            recent.append(f"- 🆕 [{title}](./{problem}/README.md)")

        average_acceptance = (
            round(acceptance_sum / total, 2)
            if total else 0
        )

        unique_topics = len(topic_counter)

        progress = self._progress_data(total)

        top_topics = ""

        for topic, count in topic_counter.most_common(5):
            top_topics += f"- **{topic}** : {count}\n"

        return {
            "TOTAL_PROBLEMS": str(total),
            "EASY": str(easy),
            "MEDIUM": str(medium),
            "HARD": str(hard),
            "AVERAGE_ACCEPTANCE": str(average_acceptance),
            "UNIQUE_TOPICS": str(unique_topics),

            "PROGRESS_BAR": progress["bar"],
            "NEXT_MILESTONE": str(progress["target"]),
            "PROGRESS_PERCENTAGE": str(progress["percentage"]),

            "TOP_TOPICS": top_topics.strip(),
            "RECENT_PROBLEMS": "\n".join(reversed(recent[:5])),
            "PROBLEM_TABLE": "\n".join(table)
        }