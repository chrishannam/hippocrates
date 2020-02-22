"""
The PHQ-2 inquires about the frequency of depressed mood and anhedonia over
the past two weeks. The PHQ-2 includes the first two items of the PHQ-9.

More information: https://www.hiv.uw.edu/page/mental-health-screening/phq-2
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


class PHQ2Assessment(Assessment):
    name: str = 'phq2'

    def __init__(self):
        raw_json = import_question_set(path=JSON_QUESTION_SET)
        self.question_set: t.List = question_set
        self.total_questions = len(self.question_set)
        self.results: t.List = create_results(question_set_json=raw_json)

    @classmethod
    def length(cls):
        return len(question_set)
