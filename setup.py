from pathlib import Path

from setuptools import setup, find_packages

with open("./README.md", "r") as ff:
    readme_text = ff.read()

path_doc_reqs = Path("./doc/requirements.txt")
doc_reqs = [
    ii
    for ii in path_doc_reqs.read_text(encoding="utf8").split("\n")
    if ii and not ii.startswith("#") and ii != "."
]
# Parse version
init = Path(__file__).parent.joinpath("sphinx_comments", "__init__.py")
for line in init.read_text().split("\n"):
    if line.startswith("__version__ ="):
        break
version = line.split(" = ")[-1].strip('"')

setup(
    name="sphinx-comments",
    version=version,
    description="Add comments and annotation to your documentation.",
    long_description=readme_text,
    long_description_content_type="text/markdown",
    author="Executable Book Project",
    url="https://github.com/executablebooks/sphinx-comments",
    license="MIT License",
    packages=find_packages(),
    classifiers=["License :: OSI Approved :: MIT License"],
    install_requires=["sphinx>=1.8",],
    extras_require={
        "code_style": ["flake8<3.8.0,>=3.7.0", "black", "pre-commit==1.17.0"],
        "sphinx": doc_reqs,
        "testing": ["beautifulsoup4", "myst-parser", "pytest", "pytest-regressions",]
        + doc_reqs,
    },
)
