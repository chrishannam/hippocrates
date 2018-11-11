# Introduction
This module makes available a select of medical questionnaires.

# Example Usage
The ability to take a questionnaires is built in. These are taken using the
[Pick](https://github.com/wong2/pick) library.

Below is an example with output for the PHQ9 questionnaire.
```python
from hippocrates.questionnaires.phq2 import PHQ2Assessment

phq2 = PHQ2Assessment()
result = phq2.take_assessment()
print(f'Severity: {result.severity}')
print(f'Comment: {result.comment}')
```

```
$ PYTHONPATH=. python examples/run_assessment.py

 Little interest or pleasure in doing things

 => More than half the days
    Nearly every day
    Not at all
    Several days

 Feeling down, depressed, or hopeless

 => More than half the days
    Nearly every day
    Not at all
    Several days


Severity: Mild
Comment: Use clinical judgment (symptom duration, functional impairment) to determine necessity of treatment
$
```
