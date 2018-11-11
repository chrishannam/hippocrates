import json

import pytest
from hippocrates.questionnaires.models import create_questions, create_results


@pytest.fixture
def questionnaire_set_json():
    """ Load in fixtures
    """

    with open('tests/fixtures/question_set.json') as json_file:
        question_set_json = json.load(json_file)
    return question_set_json


@pytest.fixture
def questionnaire_set(questionnaire_set_json):
    """ Load in fixtures
    """
    return create_results(question_set_json=questionnaire_set_json), \
        create_questions(questionnaire_set_json)
