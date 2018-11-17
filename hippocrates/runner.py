from hippocrates.questionnaires.bdi.assessment import BDIAssessment
from hippocrates.questionnaires.gad7.assessment import GAD7Assessment
from hippocrates.questionnaires.phq9.assessment import PHQ9Assessment
from hippocrates.questionnaires.rosenberg_self_esteem.assessment import \
    RosenbergSelfEsteemAssessment
from pick2 import pick

OPTIONS = {
    'Beck Depression Index': BDIAssessment(),
    'GAD 7': GAD7Assessment(),
    'PHQ 9': PHQ9Assessment(),
    'Rosenberg Self Esteem': RosenbergSelfEsteemAssessment(),
}
PICK_OPTIONS = list(OPTIONS.keys())


def pick_assessment():
    option, index = pick(
        PICK_OPTIONS, 'Please select an assessment from the list:',
        indicator='=>', default_index=0,
    )
    return OPTIONS[option]


if __name__ == '__main__':
    assessment = pick_assessment()
    result = assessment.take_assessment()
    print(result.severity)
