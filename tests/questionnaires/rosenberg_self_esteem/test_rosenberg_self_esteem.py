from hippocrates.questionnaires.rosenberg_self_esteem.assessment import (
    RosenbergSelfEsteemAssessment,
)


import pytest


@pytest.fixture
def assessment() -> RosenbergSelfEsteemAssessment:
    return RosenbergSelfEsteemAssessment()


def test_beck_depression_index_assessment(assessment: RosenbergSelfEsteemAssessment):
    assert assessment.question_set


def test_name(assessment: RosenbergSelfEsteemAssessment):
    assert assessment.name == 'rosenberg_self_esteem'


def test_beck_depression_index_questions(assessment: RosenbergSelfEsteemAssessment):
    assert assessment.questions()


def test_questions_length(assessment: RosenbergSelfEsteemAssessment):
    assert assessment.length() == 10
