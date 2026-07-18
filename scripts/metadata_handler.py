import json
import os


class MetadataHandler:

    @staticmethod
    def metadata_path(problem_folder):
        return os.path.join(problem_folder, "metadata.json")

    @staticmethod
    def exists(problem_folder):
        return os.path.exists(
            MetadataHandler.metadata_path(problem_folder)
        )

    @staticmethod
    def save(problem_folder, metadata):

        with open(
            MetadataHandler.metadata_path(problem_folder),
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                metadata,
                f,
                indent=4
            )

    @staticmethod
    def load(problem_folder):

        with open(
            MetadataHandler.metadata_path(problem_folder),
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)