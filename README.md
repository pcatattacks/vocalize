# vocalize

## Setup

Make sure you have [pip](https://pip.pypa.io/en/stable/installing/) installed. Make sure you're using Python 2.7.

It's best to set up a virtual environment before installing dependencies to run the program. To do so, run:

```sh
virtualenv venv
```

If you want to specify the path to your Python 2.7 interpreter, do:

```sh
virtualenv -p <path_to_python_interpreter> venv
#                eg. usr/bin/python2.7
```

The virtual environment must be active when running the program. Activate it by running:

```sh
source venv/bin/activate
```

Deactivate it by simply running: `deactivate`.

When starting a new jupyter notebook that will use the melodia vamp plugin, make sure you execute this code in the top cell:

```python
import os
os.environ["VAMP_PATH"] = "./melodia_plugins/"
```

This sets the path of the melodia plugins to the local folder, so you don't have to download them.

## Updating Dependencies

When any new dependencies are installed, **before committing your work, make sure to run**:

```sh
pip freeze > requirements.txt
```

This writes the changes to the `requirements.txt` file.

To update your virtual environment after pulling new changes, run:

```sh
pip install -r requirements.txt
```

Make sure your environment is activated when installing new dependencies!
