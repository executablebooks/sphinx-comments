from bs4 import BeautifulSoup
from pathlib import Path
from subprocess import run
from shutil import copytree, rmtree
import pytest


path_tests = Path(__file__).parent.resolve()
# path_base = path_tests.joinpath("sites", "base")


# @pytest.fixture(scope="session")
# def sphinx_build(tmpdir_factory):
#     class SphinxBuild:
#         path_tmp = Path(tmpdir_factory.mktemp("build"))
#         path_book = path_tmp.joinpath("book")
#         path_build = path_book.joinpath("_build")
#         path_html = path_build.joinpath("html")
#         cmd_base =

#         def copy(self, path=None):
#             """Copy the specified book to our tests folder for building."""
#             if path is None:
#                 path = path_base
#             if not self.path_book.exists():
#                 copytree(path, self.path_book)

#         def build(self, cmd=None):
#             """Build the test book"""
#             cmd = [] if cmd is None else cmd
#             run(self.cmd_base + cmd, cwd=self.path_book, check=True)

#         def path(self, *args):
#             return self.path_html.joinpath(*args)

#         def get(self, *args):
#             path_page = self.path(*args)
#             if not path_page.exists():
#                 raise ValueError(f"{path_page} does not exist")
#             return BeautifulSoup(path_page.read_text(), "html.parser")

#         def clean(self):
#             """Clean the _build folder so files don't clash with new tests."""
#             rmtree(self.path_build)

#     return SphinxBuild()

#     def test_build


def test_comments(file_regression, tmpdir_factory):
    path_docs = path_tests.joinpath("..", "doc")
    path_config = path_tests.joinpath("config")
    path_tmp = Path(tmpdir_factory.mktemp("build"))
    path_build = path_tmp.joinpath("_build", "html")

    cmd = ["sphinx-build", path_docs, path_build, "-a", "-W", "-c", path_config]
    run(cmd, check=True)

    # Load the index file to check if libraries are loaded properly
    soup = BeautifulSoup(path_build.joinpath("index.html").read_text(), "html.parser")

    hypothesis = soup.find("script", attrs={"kind": "hypothesis"})
    file_regression.check(
        hypothesis.prettify(), basename="hypothesis", extension=".html"
    )

    dokieli = soup.find("script", attrs={"kind": "dokieli"})
    file_regression.check(dokieli.prettify(), basename="dokieli", extension=".html")

    utterances = soup.find("script", attrs={"kind": "utterances"})
    file_regression.check(
        utterances.prettify(), basename="utterances", extension=".html"
    )
