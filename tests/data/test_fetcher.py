import os

from hippocrates.data.fetcher import from_log_raw, from_log_processed

from pathlib import Path

ROOT = Path(__file__).parent


def test_from_log_raw():
    filename = os.path.join(ROOT, '../fixtures/results.csv')
    log = from_log_raw(filename)
    assert len(log.keys()) == 7
    # test each questionnaire has the expected results for phq9 and gad7.
    assert len(log[list(log.keys())[0]]) == 364
    assert len(log[list(log.keys())[1]]) == 364


def test_from_log_processed():
    filename = os.path.join(ROOT, '../fixtures/results.csv')
    log = from_log_processed(filename)

    assert len(log['phq9']) == 364
    assert len(log.keys()) == 7
