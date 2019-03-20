import click
from hippocrates.questionnaires.base import Assessment


@click.command()
@click.option('--hide', is_flag=True)
@click.option('--log', is_flag=True)
@click.argument('assessment')
def main(hide, log, assessment):
    for cls in [cls for cls in Assessment.__subclasses__()]:
        if assessment == cls.name:
            assessment = cls()
            print(f'Taking the {assessment.title}')

    assessment.take_assessment()
    if not hide:
        print('Answers')
        print(assessment.display_answers())
        print('Analysis')
        print(assessment.display_result())
    if log:
        print('Saving results.')
        assessment.save_results()


if __name__ == '__main__':
    main()
