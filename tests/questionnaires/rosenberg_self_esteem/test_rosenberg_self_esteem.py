from hippocrates.questionnaires.rosenberg_self_esteem.assessment import \
    RosenbergSelfEsteemAssessment


def test_bdi_assessment():
    rosenberg_self_esteem_assessment = RosenbergSelfEsteemAssessment()
    assert rosenberg_self_esteem_assessment.question_set
