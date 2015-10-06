import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()

setup(
    name='score.html',
    version='0.1',
    description='Renderer for html files for The SCORE Framework',
    long_description=README,
    author='strg.at',
    author_email='score@strg.at',
    url='http://score-framework.org',
    keywords='score framework web html',
    packages=['score.html'],
    install_requires=[
        'score.tpl >= 0.1',
    ],
)