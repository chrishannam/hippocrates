"""
Main script for handling command line usage.
"""
import click
from hippocrates.questionnaires.base import Assessment


@click.command()
@click.option('--hide', is_flag=True)
@click.option('--log', is_flag=True)
@click.argument('questionnaire')
def main(hide, log, questionnaire):
    """

    :param hide: Doesn't display results at then of the questionnaire.
    :param log: Log to csv to track results over time.
    :param questionnaire: Questionnaire selected.
    :return:
    """
    questionnaire_selected = _select_questionnaire(questionnaire)
    print(f'Taking the {questionnaire_selected.title}')

    # Assessment not found so display help text.
    if not questionnaire_selected:
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
    print('Assessment not found, please choose from:')
    for cls in [cls for cls in Assessment.__subclasses__()]:
        print(f'{cls.name}')
    print('For example: hippocrates phq9')
    exit(1)


def _select_questionnaire(questionnaire):
    for cls in [cls for cls in Assessment.__subclasses__()]:
        if questionnaire == cls.name:
            return cls()
    return _display_help()


if __name__ == '__main__':
    main()
