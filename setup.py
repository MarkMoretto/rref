# Classifiers: https://pypi.org/classifiers/
import os.path
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
rm_path = os.path.join(here, "README.md")
with open(rm_path, "r", encoding="utf-8") as rmf:
    long_description = rmf.read()

setup(
    name="rref",
    version="0.3.1",
    author="Mark Moretto",
    author_email="otteromkram@gmail.com",
    description="Package to help transform 2-D matrix into reduced row-echelon form.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Source": "https://github.com/MarkMoretto/rref",
    },
    python_requires=">=3.6.*",
    packages=find_packages(
        exclude=["static", ]
    ),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Other Audience",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Utilities",
    ],
    keywords=[
        "rref",
        "matrix",
        "row reduced echelon form",
        "echelon",
        "Gaussian elimination",
        "linear algebra",
    ],
)
