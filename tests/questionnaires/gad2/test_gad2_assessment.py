from hippocrates.questionnaires.gad2.assessment import GAD2Assessment


def test_bdi_assessment():
    gad2_assessment = GAD2Assessment()
    assert gad2_assessment.question_set


def test_bdi_questions():
    gad2_assessment = GAD2Assessment()
    assert gad2_assessment.questions()
