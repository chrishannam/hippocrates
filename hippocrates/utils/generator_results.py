#!/usr/bin/env python
"""
Create a results.csv file for GAD7 and PHQ9 tests for the previous year.
"""

import csv
from datetime import datetime, timedelta
from random import randint

from hippocrates.questionnaires.base import DATE_FORMAT


def main():
    with open('results.csv', 'w', newline='') as csvfile:
        fieldnames = ['Date Taken', 'Assessment Name', 'Score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for day in range(1, 365):
            phq9_date = datetime.now() - timedelta(days=day)
            gad7_date = phq9_date - timedelta(seconds=300)

            phq9_date = phq9_date.strftime(DATE_FORMAT)
            gad7_date = gad7_date.strftime(DATE_FORMAT)
            writer.writerow(
                {
                    'Date Taken': phq9_date,
                    'Assessment Name': 'phq9',
                    'Score': randint(0, 27),
                }
            )
            writer.writerow(
                {
                    'Date Taken': gad7_date,
                    'Assessment Name': 'gad7',
                    'Score': randint(0, 21),
                }
            )


if __name__ == '__main__':
    main()
