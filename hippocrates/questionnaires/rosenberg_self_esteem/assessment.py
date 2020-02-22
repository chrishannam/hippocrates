"""
The Rosenberg self-esteem scale (RSES), developed by sociologist Dr. Morris
Rosenberg, is a self-esteem measure widely used in social-science research.
It uses a scale of 0-30 where a score less than 15 may indicate a
problematic low self esteem.

More information: https://en.wikipedia.org/wiki/Rosenberg_self-esteem_scale
"""

import typing as t
from pathlib import Path

from hippocrates.questionnaires.base import Assessment
from hippocrates.questionnaires.models import (
    create_questions,
    create_results,
    import_question_set,
)

JSON_QUESTION_SET = version_path = Path(__file__).parent / 'question_set.json'

question_set_json = import_question_set(path=JSON_QUESTION_SET)
question_set = create_questions(question_set_json)


class RosenbergSelfEsteemAssessment(Assessment):
    name: str = 'rosenberg_self_esteem'

    def __init__(self):
        raw_json = import_question_set(path=JSON_QUESTION_SET)
        self.question_set: t.List = question_set
        self.total_questions = len(self.question_set)
        self.results: t.List = create_results(question_set_json=raw_json)

    @classmethod
    def length(cls):
        return len(question_set)
