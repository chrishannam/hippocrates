from hippocrates.questionnaires.beck_depression_index.assessment import \
    BeckDepressionIndexAssessment
from hippocrates.questionnaires.gad2.assessment import GAD2Assessment
from hippocrates.questionnaires.gad7.assessment import GAD7Assessment
from hippocrates.questionnaires.phq2 import PHQ2Assessment
from hippocrates.questionnaires.phq9.assessment import PHQ9Assessment
from hippocrates.questionnaires.rosenberg_self_esteem.assessment import \
    RosenbergSelfEsteemAssessment
from pick import pick

OPTIONS = {
    f'Beck Depression Index {len(BeckDepressionIndexAssessment.question_set)}':
        BeckDepressionIndexAssessment(),
    'GAD 2': GAD2Assessment(),
    'GAD 7': GAD7Assessment(),
    'PHQ 2': PHQ2Assessment(),
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


def display_results():
    pass


if __name__ == '__main__':
    assessment = pick_assessment()
    assessment.take_assessment()
    print('Answers')
    print(assessment.display_answers())
    result = assessment.result()
    print('Analysis')
    print(assessment.display_result())
