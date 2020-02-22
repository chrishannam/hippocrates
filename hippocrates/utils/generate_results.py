#!/usr/bin/env python
"""
Create a results.csv file for GAD7 and PHQ9 tests for the previous year.
"""

import csv
from datetime import datetime, timedelta
from random import randint

from hippocrates.questionnaires.base import DATE_FORMAT


def _generate_random_time_stamp(start_time):
    time_stamp = start_time - timedelta(seconds=randint(0, 200))
    return time_stamp.strftime(DATE_FORMAT)


def main():
    with open('results.csv', 'w', newline='') as csv_file:
        fieldnames = ['Date Taken', 'Assessment Name', 'Score']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        start_time = datetime.now() - timedelta(days=366)
        for _ in range(1, 365):
            start_time = start_time + timedelta(days=1)

            writer.writerow(
                {
                    'Date Taken': _generate_random_time_stamp(start_time),
                    'Assessment Name': 'phq9',
                    'Score': randint(7, 18),
                }
            )
            writer.writerow(
                {
                    'Date Taken': _generate_random_time_stamp(start_time),
                    'Assessment Name': 'gad2',
                    'Score': randint(1, 5),
                }
            )
            writer.writerow(
                {
                    'Date Taken': _generate_random_time_stamp(start_time),
                    'Assessment Name': 'gad7',
                    'Score': randint(4, 15),
                }
            )
            writer.writerow(
                {
                    'Date Taken': _generate_random_time_stamp(start_time),
                    'Assessment Name': 'phq2',
                    'Score': randint(1, 5),
                }
            )
            writer.writerow(
                {
                    'Date Taken': _generate_random_time_stamp(start_time),
                    'Assessment Name': 'beck_depression_index',
                    'Score': randint(5, 40),
                }
            )
            writer.writerow(
                {
                    'Date Taken': _generate_random_time_stamp(start_time),
                    'Assessment Name': 'rosenberg_self_esteem',
                    'Score': randint(6, 23),
                }
            )
            writer.writerow(
                {
                    'Date Taken': _generate_random_time_stamp(start_time),
                    'Assessment Name': 'mood',
                    'Score': randint(2, 7),
                }
            )


if __name__ == '__main__':
    main()
