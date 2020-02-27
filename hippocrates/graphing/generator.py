"""
Provides basic graphing for results.csv file.
"""


from bokeh.io import output_file, show
from bokeh.layouts import column
from bokeh.plotting import figure

from hippocrates.data.fetcher import from_log

PLOT_WIDTH = 1200
PLOT_HEIGHT = 400
OUTPUT_FILE_NAME = 'hippocrates_results.html'


def format_data():
    """
    {
        'phq9': {
            'dates': [datetime, datetime]
            'scores': [14, 5]
        }
    }
    """

    data = from_log()
    results = {}

    for questionnaire, values in data.items():
        results[questionnaire] = {}
        dates = []
        scores = []

        for value in values:
            dates.append(value['Date Taken'])
            scores.append(int(value['Score']))

        results[questionnaire]['dates'] = dates
        results[questionnaire]['scores'] = scores

    return results


def render_questionnaire():
    output_file(OUTPUT_FILE_NAME)

    columns_to_display = []

    from sys import modules

    this_mod = modules[__name__]

    results = format_data()
    for questionnaire, values in results.items():
        if len(values['scores']) >= 2:
            columns_to_display.append(
                getattr(this_mod, questionnaire)(values['dates'], values['scores'])
            )
    if not columns_to_display:
        print('Not enough data to graph yet. Please complete more questionnaires.')
    else:
        show(column(columns_to_display))


def beck_depression_index(dates, scores):
    column_data = figure(
        title='Beck Depression Index',
        plot_width=PLOT_WIDTH,
        plot_height=PLOT_HEIGHT,
        background_fill_color='#fafafa',
        x_axis_type='datetime',
    )
    column_data.line(
        dates, scores, legend_label='Score', line_width=2, color='#d95b43', alpha=0.8
    )
    return column_data


def gad2(dates, scores):
    column_data = figure(
        title='Generalised Anxiety Disorder Assessment (GAD-2)',
        plot_width=PLOT_WIDTH,
        plot_height=PLOT_HEIGHT,
        background_fill_color='#fafafa',
        x_axis_type='datetime',
    )
    column_data.line(
        dates, scores, legend_label='Score', line_width=2, color='#53777a', alpha=0.8
    )
    return column_data


def gad7(dates, scores):
    column_data = figure(
        title='Generalised Anxiety Disorder Assessment (GAD-7)',
        plot_width=PLOT_WIDTH,
        plot_height=PLOT_HEIGHT,
        background_fill_color='#fafafa',
        x_axis_type='datetime',
    )
    column_data.line(
        dates, scores, legend_label='Score', line_width=2, color='#53777a', alpha=0.8
    )
    return column_data


def phq2(dates, scores):
    column_data = figure(
        title='Patient Health Questionnaire (PHQ-2)',
        plot_width=PLOT_WIDTH,
        plot_height=PLOT_HEIGHT,
        background_fill_color='#fafafa',
        x_axis_type='datetime',
    )
    column_data.line(
        dates, scores, legend_label='Score', line_width=2, color='#d95b43', alpha=0.8
    )
    return column_data


def phq9(dates, scores):
    column_data = figure(
        title='Patient Health Questionnaire (PHQ-9)',
        plot_width=PLOT_WIDTH,
        plot_height=PLOT_HEIGHT,
        background_fill_color='#fafafa',
        x_axis_type='datetime',
    )
    column_data.line(
        dates, scores, legend_label='Score', line_width=2, color='#d95b43', alpha=0.8
    )
    return column_data


def rosenberg_self_esteem(dates, scores):
    column_data = figure(
        title='Rosenberg Self Esteem',
        plot_width=PLOT_WIDTH,
        plot_height=PLOT_HEIGHT,
        background_fill_color='#fafafa',
        x_axis_type='datetime',
    )
    column_data.line(
        dates, scores, legend_label='Score', line_width=2, color='#d95b43', alpha=0.8
    )
    return column_data


def mood(dates, scores):
    column_data = figure(
        title='Mood Tracker',
        plot_width=PLOT_WIDTH,
        plot_height=PLOT_HEIGHT,
        background_fill_color='#fafafa',
        x_axis_type='datetime',
    )
    column_data.line(
        dates, scores, legend_label='Score', line_width=2, color='#d95b43', alpha=0.8
    )
    return column_data
