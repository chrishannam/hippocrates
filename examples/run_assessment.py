from hippocrates.questionnaires.phq2 import PHQ2Assessment

questionnaire_selected = PHQ2Assessment()
questionnaire_selected.take_assessment()

print(questionnaire_selected.display_answers())
print(questionnaire_selected.display_result())
