"""A simple hash function with issues"""

import bogohash

from setuptools import setup, find_packages


def readfile(name):
    with open(name, encoding='utf-8') as f:
        return f.read()


setup(
    name=bogohash.__title__,
    version=bogohash.__version__,
    license=bogohash.__license__,
    author=bogohash.__author__,
    url='https://github.com/jimbao/bogohash/',
    author_email='jimmy.wahlberg@gmail.com',
    description=__doc__,
    long_description='\n\n'.join(map(readfile, ('README.md',))),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    classifiers=[
        #  As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Education',
        'Topic :: Internet',
    ],
    test_suite="bogohash.tests"
)