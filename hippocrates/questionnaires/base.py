"""
Use this to create a parent class all hippocrates can use
"""

import typing as t
from datetime import datetime
from os import mkdir, path

from hippocrates.questionnaires.models import Answer, QuestionAnswerSet, Result
from pick import pick
from tabulate import tabulate

HOME_DIRECTORY = path.expanduser('~')
STORAGE_DIRECTORY_NAME = '.hippocrates'
STORAGE_FILE_PATH = path.join(HOME_DIRECTORY, STORAGE_DIRECTORY_NAME)
STORAGE_FILE = path.join(STORAGE_FILE_PATH, 'results.csv')


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
    name: str = ''

    @property
    def title(self):
        return self.name.replace('_', ' ').title()

    def questions(self):
        return self.question_set

    def take_assessment(self, interactive=True):
        for question in self.question_set:
            options: t.List = []
            for answer in question.answer_options:
                options.append(answer.text)

            if interactive:
                ask_question_using_pick(options, question)

    def ask_question(self) -> QuestionAnswerSet:
        question_to_ask = self.question_set[self.current_question]
        self.current_question = self.current_question + 1

        return question_to_ask

    def total_score(self):
        total = 0
        for question in self.question_set:
            if not question.answer:
                # raise exception?
                continue
            total = total + question.answer.value
        return total

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

    def check_directory_exists(self):
        if path.isdir(STORAGE_FILE_PATH):
            return True
        mkdir(STORAGE_FILE_PATH)
        return False

    def _write_to_file(self, write_header, score):
        # dir exists but the file might have been deleted
        if not path.isfile(STORAGE_FILE):
            write_header = True

        with open(STORAGE_FILE, 'a') as storage_file:
            if write_header:
                storage_file.write(f'Date Taken,Assessment Name,Score\n')
            storage_file.write(
                f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")},'
                f'{self.name},{score}\n')

    def save_results(self):
        score = self.total_score()
        write_header = False
        try:
            # create dir and print the headers for the csv file
            if not self.check_directory_exists():
                write_header = True

            self._write_to_file(write_header=write_header, score=score)

        except OSError:
            print(f'Creation of the directory {STORAGE_FILE_PATH} failed')


class AssessmentIncomplete(Exception):
    pass
