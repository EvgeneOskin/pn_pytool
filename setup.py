#!/usr/bin/env python

PROJECT = 'meatool'

# Change docs/sphinx/conf.py too!
VERSION = '0.1.1'

from setuptools import setup, find_packages

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description="App with developer's tools",
    long_description=long_description,

    author='Eugene Oskin',
    author_email='eoskin@crystalnix.com',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=[
        'cliff',
        'pushbullet.py',
        'python-decouple',
    ],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'meatool = meatool.main:main'
        ],
        'meatool.commands': [
            'send_note = meatool.send_note:SendNote',
        ],
    },

    zip_safe=False,
)
