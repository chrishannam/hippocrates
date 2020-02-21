import typing as t
import csv
from datetime import datetime

from hippocrates.questionnaires.base import DATE_FORMAT
from os.path import expanduser


def from_log(filename: str = None) -> t.Dict:
    """
    Returns the csv log file as dict keyed on questionnaire
    """

    if not filename:
        filename = f'{expanduser("~")}/.hippocrates/results.csv'

    log: t.Dict = {}
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            assessment_name = row['Assessment Name']
            if assessment_name not in log:
                log[assessment_name] = []

            dt = datetime.strptime(row['Date Taken'], DATE_FORMAT)
            row['Date Taken'] = dt  # type: ignore
            log[assessment_name].append(row)

    return log
