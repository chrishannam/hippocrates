from hippocrates.questionnaires.gad2.assessment import GAD2Assessment
import pytest


@pytest.fixture
def assessment() -> GAD2Assessment:
    return GAD2Assessment()


def test_beck_depression_index_assessment(assessment: GAD2Assessment):
    assert assessment.question_set


def test_name(assessment: GAD2Assessment):
    assert assessment.name == 'gad2'


def test_beck_depression_index_questions(assessment: GAD2Assessment):
    assert assessment.questions()


def test_questions_length(assessment: GAD2Assessment):
    assert assessment.length() == 2
