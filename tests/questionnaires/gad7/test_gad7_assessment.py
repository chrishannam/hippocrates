from hippocrates.questionnaires.gad7.assessment import GAD7Assessment


def test_bdi_assessment():
    gad7_assessment = GAD7Assessment()
    assert gad7_assessment.question_set
