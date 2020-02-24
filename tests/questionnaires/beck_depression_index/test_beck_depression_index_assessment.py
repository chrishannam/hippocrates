from hippocrates.questionnaires.beck_depression_index.assessment import (
    BeckDepressionIndexAssessment,
)

import pytest


@pytest.fixture
def assessment() -> BeckDepressionIndexAssessment:
    return BeckDepressionIndexAssessment()


def test_beck_depression_index_assessment(assessment):
    assert assessment.question_set


def test_name(assessment: BeckDepressionIndexAssessment):
    assert assessment.name == 'beck_depression_index'


def test_beck_depression_index_questions(assessment: BeckDepressionIndexAssessment):
    assert assessment.questions()


def test_questions_length(assessment: BeckDepressionIndexAssessment):
    assert assessment.length() == 21
