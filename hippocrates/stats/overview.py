"""
Generate stats from log data.
"""
from hippocrates.command_line import _select_questionnaire

from hippocrates.data.fetcher import from_log_processed
from datetime import datetime

from hippocrates.stats.exceptions import NoDataException


def average_score(
    questionnaire: str, start_date: datetime, end_date: datetime, log_entries=None
):
    """
    Calculate the average scores for a month
    """

    if not log_entries:
        log_entries = from_log_processed()

    if questionnaire not in log_entries:
        raise NoDataException()

    total, count = _get_average_total(log_entries[questionnaire], start_date, end_date)

    average = int(total / count)
    assessment = _select_questionnaire(questionnaire)
    advice = 'None'
    severity = 'None'

    for result in assessment.results:
        if result.max >= average > result.min:
            advice = result.comment
            severity = result.severity

    return average, advice, severity


def _get_average_total(log_entries, start_date, end_date):
    total = 0
    count = 0

    for data_point in log_entries:
        if end_date > data_point.date > start_date:
            total += data_point.score
            count += 1

    return total, count
