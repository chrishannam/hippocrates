import random
from unittest.mock import MagicMock

import pytest
from hippocrates.questionnaires.base import Assessment
from hippocrates.questionnaires.beck_depression_index.assessment import (
    BeckDepressionIndexAssessment,
)
from hippocrates.questionnaires.gad2.assessment import GAD2Assessment
from hippocrates.questionnaires.gad7.assessment import GAD7Assessment
from hippocrates.questionnaires.models import (
    Answer,
    Question,
    QuestionAnswerSet,
    Result,
)
from hippocrates.questionnaires.phq2 import PHQ2Assessment
from hippocrates.questionnaires.phq9 import PHQ9Assessment
from hippocrates.questionnaires.rosenberg_self_esteem.assessment import (
    RosenbergSelfEsteemAssessment,
)

ASSESSMENT_LIST = [
    PHQ2Assessment(),
    PHQ9Assessment(),
    GAD2Assessment(),
    GAD7Assessment(),
    RosenbergSelfEsteemAssessment(),
    BeckDepressionIndexAssessment(),
]


def test_assessment_complete():
    assessment = Assessment()

    question = MagicMock()
    question.answer = True
    assessment.total_questions = 1
    assessment.question_set = [question]
    assert assessment.complete()


def test_assessment_result():
    assessment = Assessment()

    question_one = Question('Do you like chips?')
    question_two = Question('Do you like dip?')

    answer_one = Answer('yes', 10)
    answer_two = Answer('no', 3)

    question_set_one = QuestionAnswerSet(
        question=question_one, answer_options=[answer_one], answer=answer_one
    )
    question_set_two = QuestionAnswerSet(
        question=question_two, answer_options=[answer_two], answer=answer_two
    )

    assessment.total_questions = 1
    assessment.question_set = [question_set_one, question_set_two]

    result_one = Result(min_score=0, max_score=5, severity='good', comment='OK')
    result_two = Result(
        min_score=5, max_score=20, severity='not good', comment='NOT OK'
    )
    assessment.results = [result_one, result_two]
    assert assessment.result() == result_two


def test_result_failure(questionnaire_set):
    assessment = Assessment()
    assessment.total_questions = 5
    assessment.question_set = questionnaire_set[0]

    with pytest.raises(Exception):
        assessment.result()


@pytest.mark.parametrize('assessment', ASSESSMENT_LIST)
def test_take_assessment_code(assessment):
    _take_assessment(assessment)
    assert assessment.result()


def _take_assessment(assessment: Assessment):
    while not assessment.complete():
        question: QuestionAnswerSet = assessment.ask_question()
        question.answer_question(random.choice(question.answer_options))


@pytest.mark.parametrize('assessment', ASSESSMENT_LIST)
def test_get_results(assessment):
    _take_assessment(assessment)
    assert len(assessment.get_results()) == len(assessment.question_set)


@pytest.mark.parametrize('assessment', ASSESSMENT_LIST)
def test_display_results(assessment):
    _take_assessment(assessment)
    table = assessment.display_answers()
    assert len(table.split('\n')) > len(assessment.question_set)


def test_assessment_title():
    assessment = Assessment()
    assessment.name = 'Base Assessment'


def test_take_assessment():
    assessment = Assessment()

    question_one = Question('Do you like chips?')
    answer_one = Answer('yes', 10)

    question_set_one = QuestionAnswerSet(
        question=question_one, answer_options=[answer_one], answer=answer_one
    )
    assessment.total_questions = 1
    assessment.question_set = [question_set_one]

    count = 0

    for _, __ in assessment.take_assessment():
        count += 1

    assert count == 1


def test_save_results():
    assessment = Assessment()
    assessment.total_score = MagicMock()
    assessment.create_log_directory = MagicMock()
    assessment._write_to_file = MagicMock()
    assert assessment.save_results()
