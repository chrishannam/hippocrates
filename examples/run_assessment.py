from hippocrates.questionnaires.phq2 import PHQ2Assessment

phq2 = PHQ2Assessment()
result = phq2.take_assessment()
print(f'Severity: {result.severity}')
print(f'Comment: {result.comment}')
