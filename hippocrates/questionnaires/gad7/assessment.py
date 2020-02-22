"""
Generalized Anxiety Disorder 7 (GAD-7) is a self-reported questionnaire for
screening and severity measuring of generalized anxiety disorder (GAD).
GAD-7 has seven items, which measure severity of various signs of GAD
according to reported response categories with assigned points (see below).
Assessment is indicated by the total score, which made up by adding together
the scores for the scale all seven items.

More information: https://en.wikipedia.org/wiki/Generalized_Anxiety_Disorder_7
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


class GAD7Assessment(Assessment):
    name: str = 'gad7'

    def __init__(self):
        raw_json = import_question_set(path=JSON_QUESTION_SET)
        self.question_set: t.List = question_set
        self.total_questions: int = len(self.question_set)
        self.results: t.List = create_results(question_set_json=raw_json)

    @classmethod
    def length(cls):
        return len(question_set)
