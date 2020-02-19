from hippocrates.questionnaires.models import (
    Questionnaire,
    Result,
    ResultSet,
    create_questions,
)


def test_create_questions(questionnaire_set_json):
    question_set = create_questions(questionnaire_set_json)
    assert len(question_set) == len(questionnaire_set_json['question_set'])


def test_questionnaire_iteration(questionnaire_set_json):
    question_set = create_questions(questionnaire_set_json)
    questionnaire = Questionnaire(question_set)

    for question in questionnaire.questions():
        assert hasattr(question, 'answer_options')
        assert hasattr(question, 'question')


def test_result_set():
    result = Result(min_score=0, max_score=4, severity='sev', comment='test comment',)
    result_set = ResultSet(results=[result])
    assert result_set
