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
        start_time = datetime.now() - timedelta(days=366)
        for _ in range(1, 365):
            start_time = start_time + timedelta(days=1)

            # random time take
            gad7_date = start_time - timedelta(seconds=randint(0, 200))
            gad2_date = start_time - timedelta(seconds=randint(0, 200))
            phq9_date = start_time - timedelta(seconds=randint(0, 200))
            phq2_date = start_time - timedelta(seconds=randint(0, 200))
            beck_date = start_time - timedelta(seconds=randint(0, 200))
            rosen_date = start_time - timedelta(seconds=randint(0, 200))

            gad7_date = gad7_date.strftime(DATE_FORMAT)
            gad2_date = gad2_date.strftime(DATE_FORMAT)
            phq9_date = phq9_date.strftime(DATE_FORMAT)
            phq2_date = phq2_date.strftime(DATE_FORMAT)
            beck_date = beck_date.strftime(DATE_FORMAT)
            rosen_date = rosen_date.strftime(DATE_FORMAT)

            writer.writerow(
                {
                    'Date Taken': phq9_date,
                    'Assessment Name': 'phq9',
                    'Score': randint(5, 20),
                }
            )
            writer.writerow(
                {
                    'Date Taken': gad2_date,
                    'Assessment Name': 'gad2',
                    'Score': randint(1, 5),
                }
            )
            writer.writerow(
                {
                    'Date Taken': gad7_date,
                    'Assessment Name': 'gad7',
                    'Score': randint(3, 17),
                }
            )
            writer.writerow(
                {
                    'Date Taken': phq2_date,
                    'Assessment Name': 'phq2',
                    'Score': randint(1, 5),
                }
            )
            writer.writerow(
                {
                    'Date Taken': beck_date,
                    'Assessment Name': 'beck_depression_index',
                    'Score': randint(5, 55),
                }
            )
            writer.writerow(
                {
                    'Date Taken': rosen_date,
                    'Assessment Name': 'rosenberg_self_esteem',
                    'Score': randint(3, 23),
                }
            )


if __name__ == '__main__':
    main()
