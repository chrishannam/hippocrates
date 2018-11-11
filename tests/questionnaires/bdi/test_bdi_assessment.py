from hippocrates.questionnaires.bdi.assessment import BDIAssessment


def test_bdi_assessment():
    bdi_assessment = BDIAssessment()
    assert bdi_assessment.question_set
