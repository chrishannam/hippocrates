from hippocrates.questionnaires.beck_depression_index.assessment import \
    BeckDepressionIndexAssessment


def test_bdi_assessment():
    bdi_assessment = BeckDepressionIndexAssessment()
    assert bdi_assessment.question_set
