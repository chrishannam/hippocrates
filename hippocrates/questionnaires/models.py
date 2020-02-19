import json
import typing as t
from pathlib import Path
from uuid import uuid4


class Question:
    def __init__(self, text: str,) -> None:
        self.text = text
        self.key = uuid4()


class Answer:
    def __init__(self, text: str, value: int,) -> None:
        self.text = text
        self.value = value


class Result:
    def __init__(
        self, min_score: int, max_score: int, severity: str, comment: str,
    ) -> None:
        self.min = min_score
        self.max = max_score
        self.severity = severity
        self.comment = comment


class ResultSet:
    def __init__(self, results: t.List[Result]) -> None:
        self.results = results


class QuestionAnswerSet:
    def __init__(
        self, question: Question, answer_options: t.List[Answer], answer=None,
    ) -> None:
        self.question = question
        self.answer_options = answer_options
        self.answer = answer

    def answer_question(self, answer: Answer):
        self.answer = answer


class Questionnaire:
    def __init__(self, question_answer_set: t.List[QuestionAnswerSet]) -> None:
        self.question_answer_set = question_answer_set

    def questions(self):
        return iter(self.question_answer_set)


def import_question_set(path: Path) -> t.Dict:
    with open(path) as json_file:
        question_set_json = json.load(json_file)
    return question_set_json


def create_questions(question_set_json):
    """
    Convert Questions and Answers from the raw json
    :param question_set_json:
    :return:
    """
    questionnaire = []
    for order_key, question_answer in question_set_json['question_set'].items():
        question = Question(question_answer['question'])
        answers = _build_answers(question_answer['answers'])
        question_answer_set = QuestionAnswerSet(
            question=question, answer_options=answers, answer=None,
        )
        questionnaire.append(question_answer_set)
    return questionnaire


def create_results(question_set_json):
    """
    Convert Questions and Answers from the raw json
    :param question_set_json:
    :return:
    """
    results = []
    for result_json in question_set_json['results']:
        results.append(
            Result(
                min_score=result_json['min'],
                max_score=result_json['max'],
                comment=result_json['comment'],
                severity=result_json['severity'],
            ),
        )
    return results


def _build_answers(answers):
    answers_set = []
    for answer, value in answers.items():
        answers_set.append(Answer(text=answer, value=value))

    return answers_set
