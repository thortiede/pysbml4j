# coding: utf-8

"""
    sbml4j API

    This is the api for the SBML4j Service   # noqa: E501

    OpenAPI spec version: 1.1.5
    Contact: thorsten.tiede@uni-tuebingen.de
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "python-sbml4j"
VERSION = "1.0.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="sbml4j API",
    author_email="thorsten.tiede@uni-tuebingen.de",
    url="",
    keywords=["Swagger", "sbml4j API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This is the api for the SBML4j Service   # noqa: E501
    """
)
