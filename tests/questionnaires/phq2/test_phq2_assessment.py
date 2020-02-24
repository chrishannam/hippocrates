from hippocrates.questionnaires.phq2.assessment import PHQ2Assessment
import pytest


@pytest.fixture
def assessment() -> PHQ2Assessment:
    return PHQ2Assessment()


def test_beck_depression_index_assessment(assessment: PHQ2Assessment):
    assert assessment.question_set


def test_name(assessment: PHQ2Assessment):
    assert assessment.name == 'phq2'


def test_beck_depression_index_questions(assessment: PHQ2Assessment):
    assert assessment.questions()


def test_questions_length(assessment: PHQ2Assessment):
    assert assessment.length() == 2
