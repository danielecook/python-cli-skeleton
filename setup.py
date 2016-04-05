from setuptools import setup
import glob

setup(name='cli-name',
      version='0.0.1',
      packages=['cli'],
      description='Skeleton commandline python project',
      url='https://github.com/danielecook/python-cli-skeleton',
      author='Daniel Cook',
      author_email='danielecook@gmail.com',
      license='MIT',
      entry_points="""
      [console_scripts]
      cli = cli.cli:main
      """,
      install_requires=["docopt", "clint"],
      zip_safe=False)
