# python-cli-skeleton

A simple python command line interface skeleton project. Uses argparse and can be installed and invoked using setuptools.

__Installation__

```
python setup.py install 
```

For development, use:

```
python setup.py develop
```

...and the program will be installed in-place, allowing you to edit the script files and test them immediately.

__Usage__

The setup script will install the program as `cli`. You can invoke it using:

```
cli
```

You probably want to change this. Check the cli/__init__.py file where you can set the `__version__` and `_program` variables. The `_program` variable sets the commandline command (`cli`), and the program name. You may want to change the names of modules (folders) as well to reflect your program. You should change the entry_point part of the setup script to reflect any changes you make to folders/files:

```
entry_points="""
[console_scripts]
{program} = cli.cli:main
""".format(program = program),

__requirements__

Add requirements to the `requirements.txt` file. The setup file parses this file before installation. Currently, `clint` is added as a requirement as it is a particularly useful module for writing command-line based utilities.

__travis-ci__

A `.travis.yml` file is included and setup for Python. You need to configure this further, however, at `[travis-ci.org](travis-ci.org)`.