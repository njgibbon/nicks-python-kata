from setuptools import find_packages
from setuptools import setup

setup(
    name='nicks_py_algs',
    url='https://github.com/njgibbon/nicks-python-kata/tree/master/nicks_py_algs',
    version='0.0.0',
    license='MIT',
    author='Nick Gibbon',
    description="Various algorithms.",
    long_description=open('README.md').read(),
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True
)