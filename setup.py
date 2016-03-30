# -*- coding: utf8 -*-
from codecs import open

from setuptools import setup, find_packages

with open("README.rst", "r", "utf-8") as f:
    readme = f.read()

setup(
    name="QuantDigger",
    version="0.4.4",
    description="量化交易Python回测系统",
    long_description=readme,
    author="QuantFans",
    author_email="dingjie.wang@foxmail.com",
    license="MIT",
    url="https://github.com/QuantFans/quantdigger",
    packages=find_packages(exclude=['tests', 'demo', "requirements", "images", "setupscripts"]),
    include_package_data=True,
    install_requires=[
        #"tushare>=0.4.7",
        "logbook>=0.12.5",
        "ta-lib>=0.4.8",
        "progressbar2>=3.6.2",
        "matplotlib>=1.5.1",
        "pandas>=0.17.1",
        "python-dateutil>=2.4.2",
        "numpy==1.10.4",
        #"lxml>=3.5.0",
        #"cython>=0.23.4",
    ],
    classifiers=[
        #'Environment :: Finance',
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        'Topic :: Software Development :: Libraries :: Python Modules',
        "Operating System :: OS Independent",
        'Programming Language :: Python',
        "Programming Language :: Python :: 2.7",
    ],
    zip_safe=False,
)
