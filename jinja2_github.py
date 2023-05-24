
"""Jinja2 Extension for rendering GitHub project properties"""

__version__ = '0.1.1'

from github import Github
from jinja2 import nodes
from jinja2.ext import Extension


class GitHubRepoBranchShaExtension(Extension):
    """A jinja2 extension for rendering the last commit SHA of a GitHub project branch.
    """
    tags = {'github_repo_branch_sha'}

    def __init__(self, environment):
        super().__init__(environment)

        # add the defaults to the environment
        environment.extend(repo_branch='master')

    def _head(self, repo, repo_branch):
        if repo_branch is None:
             repo_branch = self.environment.repo_branch
        return Github().get_repo(repo).get_branch(repo_branch).commit.sha

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        repo = parser.parse_expression()

        if parser.stream.skip_if('comma'):
            repo_branch = parser.parse_expression()
        else:
            repo_branch = nodes.Const(None)

        call_method = self.call_method(
              '_head',
              [repo, repo_branch],
              lineno=lineno,
          )
        return nodes.Output([call_method], lineno=lineno)


class GitHubRepoDescriptionExtension(Extension):
    """A jinja2 extension for rendering GitHub project description.
    """
    tags = {'github_repo_description'}

    def __init__(self, environment):
        super().__init__(environment)

    def _description(self, repo):
        return Github().get_repo(repo).description

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        repo = parser.parse_expression()

        call_method = self.call_method(
              '_description',
              [repo],
              lineno=lineno,
          )
        return nodes.Output([call_method], lineno=lineno)
