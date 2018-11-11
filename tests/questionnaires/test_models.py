from hippocrates.questionnaires.models import Questionnaire, create_questions


def test_create_questions(questionnaire_set_json):
    question_set = create_questions(questionnaire_set_json)
    assert len(question_set) == len(questionnaire_set_json['question_set'])


def test_questionnaire_iteration(questionnaire_set_json):
    question_set = create_questions(questionnaire_set_json)
    questionnaire = Questionnaire(question_set)

    for question in questionnaire.questions():
        assert hasattr(question, 'answer_options')
        assert hasattr(question, 'question')
