"""
Use this to create a parent class all hippocrates can use
"""

import typing as t
from pathlib import Path

from hippocrates.questionnaires.base import Assessment
from hippocrates.questionnaires.models import (create_questions,
                                               create_results,
                                               import_question_set)

JSON_QUESTION_SET = version_path = Path(__file__).parent / \
                               'question_set.json'

question_set_json = import_question_set(path=JSON_QUESTION_SET)
question_set = create_questions(question_set_json)


class RosenbergSelfEsteemAssessment(Assessment):

    def __init__(self):
        raw_json = import_question_set(path=JSON_QUESTION_SET)
        self.question_set: t.List = create_questions(raw_json)
        self.total_questions = len(self.question_set)
        self.results: t.List = create_results(question_set_json=raw_json)
