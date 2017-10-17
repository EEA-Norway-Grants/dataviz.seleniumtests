# -*- coding: utf-8 -*-
"""Installer for the dataviz.seleniumtests package."""

from setuptools import find_packages
from setuptools import setup


LONG_DESCRIPTION = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='dataviz.seleniumtests',
    version='1.0a1',
    description="dataviz testing metapackage",
    long_description=LONG_DESCRIPTION,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5.2",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    keywords='Python Plone',
    author='David Bătrânu',
    author_email='david.batranu@eaudeweb.ro',
    url='https://pypi.python.org/pypi/dataviz.seleniumtests',
    license='GPL version 3',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['dataviz'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'edw.seleniumtesting',
    ],
    entry_points={
        'edw.seleniumtesting': [
            'dataviz.seleniumtests.homepage = dataviz.seleniumtests.homepage:suite',
        ]
    }
)
