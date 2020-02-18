"""
Populate log with test data for graphing etc, temporary addition while working
on graphing/prediction.
"""

import csv
from datetime import datetime
from random import randint

# example entry:
# Date Taken,Assessment Name,Score
# 2020-01-31 09:19:22,phq9,18

assessments = {
    'beck': randint(0, 63),
    'gad2': randint(0, 63),
    'gad7': randint(0, 63),
}

results = {
    'Date Taken': datetime.now(),
    'Assessment Name': '',
    'Score': 0
}