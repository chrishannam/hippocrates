"""
Main script for handling command line usage.
"""
import click
from hippocrates.questionnaires.base import Assessment


def _validate_params(list_questionnaires, questionnaire):
    if list_questionnaires or not questionnaire:
        print('Please choose from the available questionnaires:\n')
        _display_help()
        exit()

    questionnaire_selected = _select_questionnaire(questionnaire)
    # Assessment not found so display help text.
    if not questionnaire_selected:
        print('Assessment not found, please choose from:')
        _display_help()

    print(f'Taking the {questionnaire_selected.title}')
    return questionnaire_selected


@click.command()
@click.option('--hide', is_flag=True)
@click.option('-l', '--log', is_flag=True)
@click.option('--list-questionnaires', is_flag=True)
@click.option('-q', '--questionnaire')
def main(hide, log, list_questionnaires, questionnaire):
    """

    :param hide: Doesn't display results at then of the questionnaire.
    :param log: Log to csv to track results over time.
    :param questionnaire: Questionnaire selected.
    :return:
    """

    questionnaire_selected = _validate_params(list_questionnaires, questionnaire)

    # Assessment not found so display help text.
    if not questionnaire_selected:
        print('Assessment not found, please choose from:')
        _display_help()

    questionnaire_selected.take_assessment_interactive()

    # Don't display the table of results at the end.
    if not hide:
        print(questionnaire_selected.display_answers())
        print(questionnaire_selected.display_result())

    # Save results to file.
    if log:
        print('Saving results.')
        questionnaire_selected.save_results()


def _display_help():

    for cls in [cls for cls in Assessment.__subclasses__()]:
        print(f'{cls.name}')
    print('\nFor example: hippocrates -q phq9')
    exit(1)


def _select_questionnaire(questionnaire):
    for cls in [cls for cls in Assessment.__subclasses__()]:
        if questionnaire == cls.name:
            return cls()
    return _display_help()


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(exc)
