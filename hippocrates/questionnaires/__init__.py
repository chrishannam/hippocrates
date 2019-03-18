from .beck_depression_index.assessment import BeckDepressionIndexAssessment
from .gad2.assessment import GAD2Assessment
from .gad7.assessment import GAD7Assessment
from .phq2.assessment import PHQ2Assessment
from .phq9.assessment import PHQ9Assessment
from .rosenberg_self_esteem.assessment import RosenbergSelfEsteemAssessment

registry = {
    BeckDepressionIndexAssessment.name: BeckDepressionIndexAssessment, 
    GAD2Assessment.name: GAD2Assessment, 
    GAD7Assessment.name: GAD2Assessment, 
}
