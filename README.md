[![Build Status](https://travis-ci.org/danielecook/python-cli-skeleton.svg?branch=master)](https://travis-ci.org/danielecook/python-cli-skeleton) [![Coverage Status](https://coveralls.io/repos/github/danielecook/python-cli-skeleton/badge.svg?branch=master)](https://coveralls.io/github/danielecook/python-cli-skeleton?branch=master)

# python-cli-skeleton

A simple python command line interface skeleton project. Features support for:

* travis-ci
* coveralls
* argparse
* py.test (testing)

__Installation__

```
python setup.py install 
```

For development, use:

```
python setup.py develop
```

...and the program will be installed in-place, allowing you to edit the script files and test them from the command line.

__Usage__

The setup script will install the program as `cli`. You can invoke it using:

```
cli
```

To change the way the program is invoked, edit the `cli/__init__.py` file where you can set the `__version__` and `_program` variables. The `_program` variable sets the commandline command (`cli`), and the program name. You may want to change the names of modules (folders) as well to reflect your program. You should change the entry_point part of the setup script to reflect any changes you make to folders/files:

```
entry_points="""
[console_scripts]
{program} = cli.cli:main
""".format(program = _program),
```

__requirements.txt__

Add any modules you want installed to the `requirements.txt` file. The setup file parses this file before installation. Currently, [`clint`](https://github.com/kennethreitz/clint) is the only requirement. It is a useful module for adding color, indenting, progress bars, and other useful things to command-line based programs.

__travis-ci__

A `.travis.yml` file is included and setup for Python. Testing is performed using Python 2.7 and 3.6. You will need to setup `[travis-ci.org](travis-ci.org)` to perform testing.

__coveralls__

Support for coveralls is build in using `pytest-cov`. Please see [coveralls.io](https://coveralls.io/) for more information. You may want to edit the `.coveragerc` file to fine tune how coverage is calculated.
