from hippocrates.questionnaires.gad7.assessment import GAD7Assessment
import pytest


@pytest.fixture
def assessment() -> GAD7Assessment:
    return GAD7Assessment()


def test_beck_depression_index_assessment(assessment: GAD7Assessment):
    assert assessment.question_set


def test_name(assessment: GAD7Assessment):
    assert assessment.name == 'gad7'


def test_beck_depression_index_questions(assessment: GAD7Assessment):
    assert assessment.questions()


def test_questions_length(assessment: GAD7Assessment):
    assert assessment.length() == 7

