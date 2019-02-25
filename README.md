# vocalize

## Setup

To setup the environment, run:

```sh
conda env create -f environment.yml
```

The environment must be active when running the program. Activate it by running:

```sh
source activate vocalize
```

Deactivate it by running `source deactivate`.

## Updating Dependencies

When any new dependencies are installed, committing your work, make sure to run:

```sh
conda env export | grep -v "^prefix: " > environment.yml 
```

This writes the changes to the `environment.yml` file.

To update your env after pulling new changes, run:

```sh
conda env update -f environment.yml
```

You must deactivate your environment first, run the command and then reactivate it for new dependencies to be installed.
