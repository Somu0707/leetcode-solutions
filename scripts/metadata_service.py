import requests


class MetadataService:

    GRAPHQL_URL = "https://leetcode.com/graphql"

    @staticmethod
    def get_metadata(title_slug):

        query = """
        query getQuestionDetail($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            questionFrontendId
            title
            difficulty
            acRate
            topicTags {
              name
            }
          }
        }
        """

        payload = {
            "query": query,
            "variables": {
                "titleSlug": title_slug
            }
        }

        headers = {
            "Content-Type": "application/json",
            "Referer": "https://leetcode.com",
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.post(
            MetadataService.GRAPHQL_URL,
            json=payload,
            headers=headers,
            timeout=15
        )

        response.raise_for_status()

        question = response.json()["data"]["question"]

        return {
            "id": question["questionFrontendId"],
            "title": question["title"],
            "difficulty": question["difficulty"],
            "acceptance": round(question["acRate"], 2),
            "topics": [
                tag["name"]
                for tag in question["topicTags"]
            ]
        }