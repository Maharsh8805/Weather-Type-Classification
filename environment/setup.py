

from setuptools import  setup, find_packages

setup(
    name='Project',  # project name
    version='1.0',  # version number
    description='A Synthetic Weather Classification Project',  # description of the project
    packages = find_packages(),  # find all packages
    author='LakhankiyaMaharsh' ,# author of the package
    author_email='patelmaharsh2005@gmail.com', # email of the author
    install_requires=['pandas', 'numpy', 'sklearn', 'matplotlib'],
    # list of the dependencies required by the package
    classifiers=['Programining Language :: python :: 3.12.3']
)