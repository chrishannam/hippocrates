from hippocrates.questionnaires.phq9.assessment import PHQ9Assessment


def test_pgq9_assessment():
    phq9_assessment = PHQ9Assessment()
    assert phq9_assessment.question_set
