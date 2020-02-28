"""
Main script for handling command line usage for stats gathering and display.
"""
from datetime import datetime, timedelta

import click
from tabulate import tabulate

from hippocrates.questionnaires.base import Assessment
from hippocrates.stats.exceptions import NoDataException
from hippocrates.stats.overview import average_score


@click.command()
@click.argument('questionnaire')
def main(questionnaire):
    questionnaire = _select_questionnaire(questionnaire)
    start_date = datetime.now() - timedelta(days=28)
    end_date = datetime.now()

    try:
        average, advice, severity = average_score(
            questionnaire=questionnaire.name, start_date=start_date, end_date=end_date
        )
    except NoDataException:
        print('No data available for calculate summary.')
        exit(1)

    table_data = [['Result', 'Advice', 'Severity'], [average, advice, severity]]
    print('Average for the last 28 days')
    print(tabulate(table_data, tablefmt='fancy_grid'))


def _display_help():
    print('Assessment not found, please choose from:')
    for cls in [cls for cls in Assessment.__subclasses__()]:
        print(f'{cls.name}')
    print('For example: hippocrates-summary phq9')
    exit(1)


def _select_questionnaire(questionnaire):
    for cls in [cls for cls in Assessment.__subclasses__()]:
        if questionnaire == cls.name:
            return cls()
    return _display_help()


if __name__ == '__main__':
    main()
