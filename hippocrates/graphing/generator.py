from bokeh.io import output_file, show
from bokeh.layouts import column
from bokeh.plotting import figure

from hippocrates.data.fetcher import from_log


# def render_questionnaire():
#
#     # output to static HTML file
#     output_file("lines.html")
#
#     # create a new plot with a title and axis labels
#     p = figure(title="simple line example", x_axis_label='date', y_axis_label='y',
#                x_axis_type='datetime')
#
#     # add a line renderer with legend and line thickness
#     p.line(x, y, legend_label="Temp.", line_width=2)
#
#     # show the results
#     show(p)
#
#     p = figure(title="simple line example", x_axis_label='date', y_axis_label='y',
#                x_axis_type='datetime')
#
#     # add a line renderer with legend and line thickness
#     p.line(x, y, legend_label="Temp.", line_width=2)


def format_data():
    data = from_log()
    # prepare some data

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


def render_questionnaire_two():
    output_file("layout.html")

    dates, scores = format_data()

    x = dates
    y0 = x
    y1 = [10 - i for i in x]
    y2 = [abs(i - 5) for i in x]

    # create three plots
    s1 = figure(plot_width=250, plot_height=250, background_fill_color="#fafafa")
    s1.circle(x, y0, size=12, color="#53777a", alpha=0.8)

    s2 = figure(plot_width=250, plot_height=250, background_fill_color="#fafafa")
    s2.triangle(x, y1, size=12, color="#c02942", alpha=0.8)

    s3 = figure(plot_width=250, plot_height=250, background_fill_color="#fafafa")
    s3.square(x, y2, size=12, color="#d95b43", alpha=0.8)

    # put the results in a column and show
    show(column(s1, s2, s3))


print(format_data())
