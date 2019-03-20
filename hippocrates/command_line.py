import click


@click.command()
@click.option('--hide', is_flag=True)
@click.option('--log', is_flag=True)
@click.argument('assessment')
def main(hide, log, assessment):
    print(f'HI! {assessment}')


if __name__ == '__main__':
    main()
