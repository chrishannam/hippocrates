from hippocrates.questionnaires.phq2.assessment import PHQ2Assessment


def test_bdi_assessment():
    gad2_assessment = PHQ2Assessment()
    assert gad2_assessment.question_set
