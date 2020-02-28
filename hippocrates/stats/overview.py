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

    total = 0
    count = 0

    if questionnaire not in log_entries:
        raise NoDataException()

    for data_point in log_entries[questionnaire]:
        if end_date > data_point.date > start_date:
            total += data_point.score
            count += 1

    average = int(total / count)
    assessment = _select_questionnaire(questionnaire)
    advice = 'None'
    severity = 'None'

    for result in assessment.results:
        if result.max >= average > result.min:
            advice = result.comment
            severity = result.severity

    return average, advice, severity
