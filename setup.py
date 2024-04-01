import os
from setuptools import setup, find_packages

BUILD_ID = os.environ.get("BUILD_BUILDID", "0")

setup(
    name="py-author",
    version="0.1" + "." + BUILD_ID,
    # Author details
    author="A. Doss",
    # author_email="nielszeilemaker@xebia.com",
    packages=find_packages("requirements.txt"),
    package_dir={"": "py_author"},
    # setup_requires=["pyspark[ml]", "sklearn", "pytest-runner"],
    # tests_require=["pytest", "pytest-nunit", "pytest-cov"],
    # extras_require={"develop": ["pre-commit", "bump2version"]},
)