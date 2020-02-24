from hippocrates.questionnaires.phq9.assessment import PHQ9Assessment
import pytest


@pytest.fixture
def assessment() -> PHQ9Assessment:
    return PHQ9Assessment()


def test_beck_depression_index_assessment(assessment: PHQ9Assessment):
    assert assessment.question_set


def test_name(assessment: PHQ9Assessment):
    assert assessment.name == 'phq9'


def test_beck_depression_index_questions(assessment: PHQ9Assessment):
    assert assessment.questions()


def test_questions_length(assessment: PHQ9Assessment):
    assert assessment.length() == 9
