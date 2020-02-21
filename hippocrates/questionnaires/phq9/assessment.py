"""
The PHQ-9 (DEP-9 in some sources)is a 9-question instrument given to
patients in a primary care setting to screen for the presence and severity
of depression. It is the 9-question depression scale from the Patient Health
Questionnaire (PHQ). The results of the PHQ-9 may be used to make a depression
diagnosis according to DSM-IV criteria and takes less than 3 minutes to
complete. The total of all 9 responses from the PHQ-9 aims to predict the
presence and severity of depression. Primary care providers frequently use
the PHQ-9 to screen for depression in patients.

More information: https://en.wikipedia.org/wiki/PHQ-9
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


class PHQ9Assessment(Assessment):
    name: str = 'phq9'

    def __init__(self):
        raw_json = import_question_set(path=JSON_QUESTION_SET)
        self.question_set: t.List = question_set
        self.total_questions = len(self.question_set)
        self.results: t.List = create_results(question_set_json=raw_json)

    @classmethod
    def length(cls):
        return len(question_set)
