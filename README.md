# Implementation: Feature Engineering on the ML Model

The machine learning model used in this program is the RandomForest Tree model, and it is deployed through the SciKit Learn model. The goal of this implementation step is to increase the performance of the ML Model for predicting whether or not a student will be "qualified" based on his/her G3 (final) grade. A G3 score of 15 or above (the range is 0-20) means that the student is qualified. The model outputs a binary response that indicates whether or not the student is "qualified". 

Below, the performance is quantified using the f1_score, which is the harmonic mean of precision and recall. This essentially measures the accuracy of the model.

## Default Model

The default RandomForest model has a **f1_score = 0.54293**. 

The model achieves this f1_score by using the following features:
- `age` (range from 15-22)
- `health` (range from 1-5)
- `absences` (range from 0-93)

## New Model After Feature Selection and Engineering

Team Otters wanted to significantly increase the f1_score of the new model, and added more useful features into the model. The team chose features that give insight to the student's access to resources and academic habits.

The chosen features are:
- `age` (range from 15-22)
- `health` (range from 1-5)
- `absences` (range from 0-93)
- `higher` (whether student wants to pursue higher education - yes/no)
- `paid` (whether student received extra paid classes - yes/no)
- `failures` (number of past class failures - range from 1-4)
- `dalc` (workday alcohol consumption - range from 1-5)
- `internet` (whether student has access to internet - yes/no)
- `studytime` (quantified thru range from 1-4)
- `address` (rural (R) or urban (U))

To successfully run the RandomForest model, the features `paid`, `higher`, `internet`, and `address` are transformed into 1/0 responses rather than the strings that they currently are.

The engineered features are:
- `paid_int` (yes = 1, no = 0)
- `higher_int` (yes = 1, no = 0)
- `internet_int` (yes = 1, no = 0)
- `address_int` (Urban = 1, Rural = 0)

When the ML Model is trained using the chosen and engineered features, the **f1_score = 0.92198**. This is significantly better than the default f1_score = 0.54293. 

| x | Default Model | New Model |
| --- | --- | --- |
| f1_score | 0.54293  | 0.92198 |
| # of features  | 3 | 10 |

# HW4 Starter Code and Instructions

Please consult the [homework assignment](https://cmu-313.github.io//assignments/hw4) for additional context and instructions for this code.

## pipenv

[pipenv](https://pipenv.pypa.io/en/latest) is a packaging tool for Python that solves some common problems associated with the typical workflow using pip, virtualenv, and the good old requirements.txt.

### Installation

#### Prereqs

- The version of Python you and your team will be using (version greater than 3.8)
- pip package manager is updated to latest version
- For additional resources, check out [this link](https://pipenv-fork.readthedocs.io/en/latest/install.html#installing-pipenv)

#### Mac OS

To install pipenv from the command line, execute the following:

```terminal
sudo -H pip install -U pipenv
```

#### Windows OS

The same instructions for Mac OS **should** work for windows, but if it doesn't, follow the instructions [here](https://www.pythontutorial.net/python-basics/install-pipenv-windows).

### Usage

#### Downloading Packages

The repository contains `Pipfile` that declares which packages are necessary to run the `model_build.ipnyb`.
To install packages declared by the Pipfile, run `pipenv install` in the command line from the root directory.

You might want to use additional packages throughout the assignment.
To do so, run `pipenv install [PACKAGE_NAME]`, as you would install python packages using pip.
This should also update `Pipfile` and add the downloaded package under `[packages]`.
Note that `Pipfile.lock` will also be updated with the specific versions of the dependencies that were installed.
Any changes to `Pipfile.lock` should also be committed to your Git repository to ensure that all of your team is using the same dependency versions.

#### Virtual Environment

Working in teams can be a hassle since different team members might be using different versions of Python.
To avoid this issue, you can create a python virtual environment, so you and your team will be working with the same version of Python and PyPi packages.
Run `pipenv shell` in your command line to activate this project's virtual environment.
If you have more than one version of Python installed on your machine, you can use pipenv's `--python` option to specify which version of Python should be used to create the virtual environment.
If you want to learn more about virtual environments, read [this article](https://docs.python-guide.org/dev/virtualenvs/#using-installed-packages).
You can also specify which version of python you and your team should use under the `[requires]` section in `Pipfile`.

## Jupyter Notebook

You should run your notebook in the virtual environment from pipenv.
To do, you should run the following command from the root of your repository:

```terminal
pipenv run jupyter notebook
```

## API Endpoints

You should also use pipenv to run your Flask API server.
To do so, execute the following commands from the `app` directory in the pip venv shell.


Set an environment variable for FLASK_APP.
For Mac and Linux:
```terminal
export FLASK_APP=app.py
```

For Windows:
```terminal
set FLASK_APP=app
```

To run:
```terminal
pipenv run flask run
```

Or if you're in the pipenv shell, run:
```terminal
flask run
```

You can alter the port number that is used by the Flask server by changing the following line in `app/app.py`:

```python
app.run(host="0.0.0.0", debug=True, port=80)
```

## Testing

To run tests, execute the following command from the `app` directory:

```terminal
pytest
```

If you're not in the Pipenv shell, then execute the following command from the `app` directory:

```terminal
pipenv run pytest
```
