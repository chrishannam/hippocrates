"""
Script for handling graph generation.
"""
import click

from hippocrates.graphing.generator import render_questionnaire


@click.command()
def main():
    """
    Needs updating to allow questionnaire to be selected.
    """
    render_questionnaire()
    print('Done.')


if __name__ == '__main__':
    main()
