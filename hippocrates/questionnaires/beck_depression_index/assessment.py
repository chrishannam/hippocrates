"""
The Beck Depression Inventory (BDI, BDI-1A, BDI-II), created by Aaron T.
Beck, is a 21-question multiple-choice self-report inventory, one of the
most widely used psychometric tests for measuring the severity of
depression. Its development marked a shift among mental health
professionals, who had until then, viewed depression from a psychodynamic
perspective, instead of it being rooted in the patient's own thoughts.

More information: https://en.wikipedia.org/wiki/Beck_Depression_Inventory
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


class BeckDepressionIndexAssessment(Assessment):
    name: str = 'beck_depression_index'

    def __init__(self):
        raw_json = import_question_set(path=JSON_QUESTION_SET)
        self.question_set: t.List = question_set
        self.total_questions: int = len(self.question_set)
        self.results: t.List = create_results(question_set_json=raw_json)

    @classmethod
    def length(cls):
        return len(question_set)
