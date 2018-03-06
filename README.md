## How to get started

Requirements:

* Python 3+
* Anaconda: https://anaconda.org/anaconda/python

Clone the repo and enter it:

    $ git clone git@github.com:vijai747/ToDoistDashboard.git
    $ cd ToDoistDashboard

Create an environment:

    $ conda env create -f environment.yml

Activate the environment:

    $ source activate todoist

Navigate to Jupyter Notebook to view analysis

    $ cd code/
    $ jupyter notebook

## Tailor analysis to your ToDoist Profile

You can find out your token from the Todoist Web app, at Todoist Settings -> Account -> API token.

Open data_download_projects.py and insert your token value into the variable 'MyToken'
Open data_download_items.py and insert your token value into the variable 'MyToken'

Run both files to generate a csv file with your personal data:

    $ python data_download_projects.py
    $ python data_download_items.py

Reopen the Jupyter Notebook and re-run the entire kernel to update the tables and graph with your information.

Suggestions for improvement are welcome!
