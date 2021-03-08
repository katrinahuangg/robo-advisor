# "Robo Advisor" Project

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository](https://github.com/katrinahuangg/robo-advisor) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd ~/Desktop/robo-advisor
```

## Environment Setup

It is possible to complete this project using the "base" Anaconda environment, because the basic requirements don't require any third-party packages. However if you eventually end up tackling bonus challenges that require third-party packages, then you'll want to create and activate a new Anaconda virtual environment, and use a "requirements.txt" file approach to installing your packages:

```sh
# IF USING THIRD-PARTY PACKAGES, USE A NEW ENV:
conda create -n stocks-env python=3.8 
conda activate stocks-env
pip install -r requirements.txt # (after specifying desired packages inside)
```

### Obtaining Your API Key

Obtain your [AlphaVantage API KEY](https://www.alphavantage.co).
Then set an environment variable called `ALPHAVANTAGE_API_KEY` in a .env file, and the program should read the API Key from this environment variable at run-time.

Within an active virtual environment of choice ("base" or project-specific), demonstrate your ability to run the Python script from the command-line:

```sh
python app/robo-advisor.py
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above)

#### Data Setup

The provided code includes a variable called `products` which facilitates management of the products inventory from within the application's source code.

> NOTE: If you'd like to use an alternative storage mechanism for the products inventory, like a CSV file or a Google Sheet document, reference the respective [further exploration challenges](challenges.md).

