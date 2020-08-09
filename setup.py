import os
from pathlib import Path

from setuptools import setup, find_packages

with open('./README.md', 'r') as ff:
    readme_text = ff.read()

# Parse version
init = Path(__file__).parent.joinpath("sphinx_comments", "__init__.py")
for line in init.read_text().split("\n"):
    if line.startswith("__version__ ="):
        break
version = line.split(" = ")[-1].strip('"')

setup(
    name='sphinx-comments',
    version=version,
    description="Add a hypothes.is overlay to your documentation.",
    long_description=readme_text,
    long_description_content_type='text/markdown',
    author='Executable Book Project',
    url="https://github.com/ExecutableBookProject/sphinx-comments",
    license='MIT License',
    packages=find_packages(),
    classifiers=["License :: OSI Approved :: MIT License"],
    install_requires=[
        "sphinx>=1.8"
    ]
)
