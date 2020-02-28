from datetime import datetime, timedelta

from hippocrates.data.fetcher import DataPoint
from hippocrates.stats.overview import average_score


def test_monthly_average():
    start_date = datetime.now() - timedelta(days=28)
    end_date = datetime.now() + timedelta(days=20)

    data = {
        'phq9': [
            DataPoint(date=datetime.now(), score=7),
            DataPoint(date=datetime.now(), score=7),
        ]
    }

    average, advice, severity = average_score(
        'phq9', log_entries=data, start_date=start_date, end_date=end_date
    )

    assert average == 7
    assert advice != 'None'
    assert severity != 'None'
