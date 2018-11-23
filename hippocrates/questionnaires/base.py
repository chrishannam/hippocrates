"""
Use this to create a parent class all hippocrates can use
"""

import typing as t

from hippocrates.questionnaires.models import Answer, QuestionAnswerSet, Result
from pick import pick
from tabulate import tabulate


def ask_question_using_pick(options: t.List[Answer],
                            question_from_set: QuestionAnswerSet):
    option, index = pick(
        options, question_from_set.question.text,
        indicator='=>', default_index=0,
    )
    question_from_set.answer = question_from_set.answer_options[index]


class Assessment:
    question_set: t.List = []
    results: t.List = []
    current_question: int = 0

    def questions(self):
        return self.question_set

    def take_assessment(self, interactive=True):
        for question in self.question_set:  # type: Question
            options: t.List = []
            for answer in question.answer_options:
                options.append(answer.text)

            if interactive:
                ask_question_using_pick(options, question)

    def ask_question(self) -> QuestionAnswerSet:
        question_to_ask = self.question_set[self.current_question]
        self.current_question = self.current_question + 1

        return question_to_ask

    def result(self) -> Result:
        total = 0
        for question in self.question_set:
            if not question.answer:
                # raise exception?
                continue
            total = total + question.answer.value

        for result in self.results:
            if result.min <= total <= result.max:
                return result
        raise Exception

    def complete(self):
        """
        check if all questions have an answer
        :return:
        """
        count = 0
        for question in self.question_set:
            if question.answer:
                count = count + 1

        return True if count == self.total_questions else False

    def get_results(self) -> list:
        if not self.complete():
            raise AssessmentIncomplete()

        answer_detail = []
        for question_answer in self.question_set:  # type Question
            answer_detail.append([question_answer.question.text,
                                 question_answer.answer.text])
        return answer_detail

    def display_answers(self):
        table_data = [
            ['Question', 'Answer'],
        ]
        table_data = table_data + self.get_results()
        return tabulate(table_data, tablefmt='fancy_grid')

    def display_result(self):
        result = self.result()
        table_data = [
            ['Result', 'Severity'],
            [result.comment, result.severity]
        ]
        return tabulate(table_data, tablefmt='fancy_grid')


class AssessmentIncomplete(Exception):
    pass
