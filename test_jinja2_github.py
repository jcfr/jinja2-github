from jinja2 import Environment


def test_github_repo_branch_sha():
    environment = Environment(extensions=["jinja2_github.GitHubRepoBranchShaExtension"], autoescape=True)

    template = environment.from_string("{% github_repo_branch_sha 'jcfr/jinja2-github' %}")

    assert template.render()

    template = environment.from_string("{% github_repo_branch_sha 'jcfr/jinja2-github', 'test-branch' %}")

    assert template.render() == "188aeda35dcab7277ad37e1657e2b2780b6c8777"


def test_github_repo_description():
    environment = Environment(extensions=["jinja2_github.GitHubRepoDescriptionExtension"], autoescape=True)

    template = environment.from_string("{% github_repo_description 'jcfr/jinja2-github' %}")

    assert template.render().startswith("jinja2 extensions for rendering Github project properties")
