import os

from hippocrates.data.fetcher import from_log

ROOT = os.path.dirname(os.path.abspath(__file__))


def test_from_log():
    filename = os.path.join(ROOT, '../fixtures/results.csv')
    log = from_log(filename)
    assert len(log.keys()) == 7
    # test each questionnaire has the expected results for phq9 and gad7.
    assert len(log[list(log.keys())[0]]) == 364
    assert len(log[list(log.keys())[1]]) == 364
