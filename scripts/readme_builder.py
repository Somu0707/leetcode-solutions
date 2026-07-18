from collections import Counter, defaultdict
from datetime import datetime

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

    def _difficulty_bar(self, count, maximum):
        if maximum == 0:
            return ""

        width = 20
        filled = round((count / maximum) * width)
        return "█" * filled + "░" * (width - filled)

    def _achievement(self, total, milestone):
        return "✅" if total >= milestone else "⏳"

    def build(self):

        problems = self.scanner.scan()
        last_updated = datetime.now().strftime("%d %b %Y %H:%M")

        total = len(problems)

        easy = medium = hard = 0
        acceptance_sum = 0.0

        topic_counter = Counter()
        monthly_activity = defaultdict(int)

        table = [
            "| # | Problem | Difficulty | Acceptance | Topics | README |",
            "|---:|---------|------------|-----------:|--------|:------:|"
        ]

        recent = []

        for problem in problems:
            metadata = MetadataHandler.load(problem)

            solved_at = metadata.get(
                "solved_at",
                "1970-01-01T00:00:00"
            )

            month = datetime.fromisoformat(solved_at).strftime("%B %Y")
            monthly_activity[month] += 1

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

            table.append(
                f"| {number} | [{title}](./{problem}/README.md) | "
                f"{badge} | {acceptance:.2f}% | {', '.join(topics[:3])} | ✅ |"
            )

            recent.append({
                "title": title,
                "path": problem,
                "solved_at": solved_at
            })

        average_acceptance = round(acceptance_sum / total, 2) if total else 0
        unique_topics = len(topic_counter)

        most_solved_topic = "-"
        if topic_counter:
            most_solved_topic = topic_counter.most_common(1)[0][0]

        total_topic_occurrences = sum(topic_counter.values())
        average_topics = round(total_topic_occurrences / total, 2) if total else 0

        months = len(monthly_activity)
        average_per_month = round(total / months, 2) if months else total

        progress = self._progress_data(total)

        bronze = self._achievement(total, 50)
        silver = self._achievement(total, 100)
        gold = self._achievement(total, 250)
        platinum = self._achievement(total, 500)

        maximum = max(easy, medium, hard)

        easy_bar = self._difficulty_bar(easy, maximum)
        medium_bar = self._difficulty_bar(medium, maximum)
        hard_bar = self._difficulty_bar(hard, maximum)

        top_topics = "\n".join(
            f"- **{topic}** : {count}"
            for topic, count in topic_counter.most_common(5)
        )

        monthly_table = ""
        for month, count in sorted(
            monthly_activity.items(),
            key=lambda x: datetime.strptime(x[0], "%B %Y")
        ):
            monthly_table += f"| {month} | {count} |\n"

        recent.sort(key=lambda x: x["solved_at"], reverse=True)

        recent_markdown = "\n".join(
            f"- 🆕 [{item['title']}](./{item['path']}/README.md)"
            for item in recent[:5]
        )

        return {
            "TOTAL_PROBLEMS": str(total),
            "EASY": str(easy),
            "MEDIUM": str(medium),
            "HARD": str(hard),

            "EASY_BAR": easy_bar,
            "MEDIUM_BAR": medium_bar,
            "HARD_BAR": hard_bar,

            "AVERAGE_ACCEPTANCE": f"{average_acceptance:.2f}",
            "UNIQUE_TOPICS": str(unique_topics),

            "MOST_SOLVED_TOPIC": most_solved_topic,
            "AVERAGE_TOPICS": f"{average_topics:.2f}",
            "AVERAGE_PER_MONTH": f"{average_per_month:.2f}",

            "PROGRESS_BAR": progress["bar"],
            "NEXT_MILESTONE": str(progress["target"]),
            "PROGRESS_PERCENTAGE": str(progress["percentage"]),

            "LAST_UPDATED": last_updated,

            "BRONZE": bronze,
            "SILVER": silver,
            "GOLD": gold,
            "PLATINUM": platinum,

            "TOP_TOPICS": top_topics,
            "RECENT_PROBLEMS": recent_markdown,
            "MONTHLY_ACTIVITY": monthly_table.strip(),
            "PROBLEM_TABLE": "\n".join(table)
        }
