[![CircleCI](https://circleci.com/gh/chrishannam/hippocrates/tree/master.svg?style=svg)](https://circleci.com/gh/chrishannam/hippocrates/tree/master)

# Hippocrates
A Python library for giving and scoring various health based questionnaires.

Currently the following are supported:
* [Beck Depression Inventory](https://en.wikipedia.org/wiki/Beck_Depression_Inventory)
* [Generalized Anxiety Disorder 2](https://en.wikipedia.org/wiki/Generalized_anxiety_disorder)
* [Generalized Anxiety Disorder 7](https://en.wikipedia.org/wiki/Generalized_Anxiety_Disorder_7)
* [Patient Health Questionnaire 2](https://en.wikipedia.org/wiki/Patient_Health_Questionnaire#2-item_depression_screener)
* [Patient Health Questionnaire 9](https://en.wikipedia.org/wiki/PHQ-9)
* [Rosenberg Self-Esteem Scale](https://en.wikipedia.org/wiki/Rosenberg_self-esteem_scale)

More information about the above tests can be found in [questionnaires](docs/questionnaires.md).

# Installing
## Pip
`pip install hippocrates`

## From Source
```
git clone https://github.com/chrishannam/hippocrates.git
cd hippocrates
python setup.py install
```


# Using the Questionnaires
Once installed the following questionnaire are available:

* `hip-take-beck-depression-index`
* `hip-take-gad2`
* `hip-take-gad7`
* `hip-take-phq2`
* `hip-take-phq9`
* `hip-take-rosenberg-self-esteem`

Run the desired command to take the questionnaire.

## Options

### --hide
Stops results from being displayed once questionnaire is created, default is `off`.

### --log
Logs results to ~/.hippocrates/results.csv, default is `off`.
