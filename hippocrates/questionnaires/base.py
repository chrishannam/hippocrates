"""
Use this to create a parent class all hippocrates can use
"""

import typing as t

from hippocrates.questionnaires.models import Answer, QuestionAnswerSet, Result
from pick2 import pick


class Assessment:

    question_set: t.List = []
    results: t.List = []

    def questions(self):
        return self.question_set

    def ask_question(self, options: t.List[Answer], question_from_set:
                     QuestionAnswerSet):
        option, index = pick(
            options, question_from_set.question.text,
            indicator='=>', default_index=0,
        )
        question_from_set.answer = question_from_set.answer_options[index]

    def take_assessment(self) -> Result:
        for question_from_set in self.question_set:
            options: t.List = []
            for answer in question_from_set.answer_options:
                options.append(answer.text)

            self.ask_question(options, question_from_set)

        return self.result()

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
