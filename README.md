# Description

WordleBot app

---

# Development

Developed using Python

---

## Developer Notes

Please always use `pipenv install` instead of `pip3 install` when adding dependencies.

Also ensure to keep the `requirements.txt` up-to-date by runnging the following command wheneve dependencies are added/removed.

`$ pipenv lock -r > requirements.txt`

---

## Environment & Application setup

Step 1: Download & install Python 3 -

The easiest way to setup a Python Environment on Windows is to download Anaconda - https://www.anaconda.com/download/

If on macOS, you can use `brew`

To setup homebrew, open the terminal and run the command

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`

Then install Python by running the following command

`$ brew install python`

Step 2: Install Pipenv

To setup & use isolated Virtual Environments, install pipenv

`$ pip3 install pipenv`

Step 3: Open the terminal & cd into project directory -

`$ cd /path/to/project`

Step 4: Activate/Create Virtual Environment

`$ pipenv shell`

Step 5: Run the following command to install all the dependencies -

`$ pipenv install`

Alternatively, you can run -

`$ pip3 install -r requirements.txt`

Step 6: Done!

---

## Run Locally:

Step 1: Open the terminal & cd into project directory -

`$ cd /path/to/project`

Step 2: Run the following command to run the application -

`$ python <project path>`

Done!

---

## TO-DO

- Add While Loop for classic_wordle & Repeat
