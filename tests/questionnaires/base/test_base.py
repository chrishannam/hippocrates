import random
from unittest.mock import MagicMock

import pytest
from hippocrates.questionnaires.base import Assessment
from hippocrates.questionnaires.models import (Answer, Question,
                                               QuestionAnswerSet, Result)
from hippocrates.questionnaires.phq2 import PHQ2Assessment


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

    question_set_one = QuestionAnswerSet(question=question_one,
                                         answer_options=[answer_one],
                                         answer=answer_one)
    question_set_two = QuestionAnswerSet(question=question_two,
                                         answer_options=[answer_two],
                                         answer=answer_two)

    assessment.total_questions = 1
    assessment.question_set = [question_set_one, question_set_two]

    result_one = Result(min_score=0, max_score=5, severity='good',
                        comment='OK')
    result_two = Result(min_score=5, max_score=20, severity='not good',
                        comment='NOT OK')
    assessment.results = [result_one, result_two]
    assert assessment.result() == result_two

    # question_set_one = QuestionAnswerSet(question=question_one,
    #                                      answer_options=[answer_one])
    # question_set_two = QuestionAnswerSet(question=question_two,
    #                                      answer_options=[answer_two])


def test_take_assessment(questionnaire_set):
    assessment = Assessment()
    assessment.total_questions = 2
    assessment.results = questionnaire_set[0]
    assessment.question_set = questionnaire_set[1]

    def ask_question(options, question):
        question.answer = question.answer_options[0]

    assessment.ask_question = ask_question
    assessment.take_assessment()
    assert assessment.complete()


def test_result_failure(questionnaire_set):
    assessment = Assessment()
    assessment.total_questions = 5
    # assessment.results = questionnaire_set[0]
    assessment.question_set = questionnaire_set[1]

    # def ask_question(options, question):
    #     question.answer = question.answer_options[0]
    #
    # assessment.ask_question = ask_question
    # assessment.take_assessment()
    with pytest.raises(Exception):
        assessment.result()


@pytest.mark.parametrize(
    'assessment',
    [PHQ2Assessment()]
)
def test_take_assessment_code(assessment):

    while not assessment.complete():
        question: Question = assessment.ask_question()
        question.answer_question(random.choice(question.answer_options))

    assessment.display_results()


@pytest.mark.parametrize(
    'assessment',
    [PHQ2Assessment]
)
def test_display_results(assessment):
    pass
