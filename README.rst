=============
Jinja2 GitHub
=============

Jinja2 Extensions for rendering GitHub project properties.

Available extensions are the following:

* ``github_repo_branch_sha``: render the last commit SHA associated with
  a GitHub project branch.

* ``github_repo_description``: render the description of a GitHub project.


Installation
------------

**jinja2-github** is available for download from `PyPI`_ via `pip`_::

    $ pip install jinja2-github

It will automatically install `jinja2`_ along with `pygithub`_.

.. _`jinja2`: https://github.com/pallets/jinja
.. _`PyPI`: https://pypi.python.org/pypi
.. _`pygithub`: https://pypi.org/project/PyGithub/
.. _`pip`: https://pypi.python.org/pypi/pip/

Usage
-----

github_repo_branch_sha Tag
--------------------------

The extension comes with a ``github_repo_branch_sha`` tag that allows to
render the last commit SHA associated with a GitHub project branch.

By default, the ``master`` branch is used.

.. code-block:: python

    from jinja2 import Environment

    env = Environment(extensions=['jinja2_github.GitHubRepoBranchShaExtension'])

    # Default branch is master -> "4f5191b50026f7281ca1b1cd180e05fad1d716c6"
    template = env.from_string("{% github_repo_branch_sha 'Slicer/Slicer' %}")

    template.render()

It is also possible to specified a branch (or tag) name:

.. code-block:: python

    from jinja2 import Environment

    env = Environment(extensions=['jinja2_github.GitHubRepoBranchShaExtension'])

    # With an explicit branch name -> "cfe12ceefd761502181660de76a8cc5d40d5f31c"
    template = env.from_string("{% github_repo_branch_sha 'Slicer/Slicer', 'master-48' %}")

    template.render()


github_repo_description
-----------------------

The extension comes with a ``github_repo_description`` tag that allows to
render the description of a GitHub project.

.. code-block:: python

    from jinja2 import Environment

    env = Environment(extensions=['jinja2_github.GitHubRepoDescriptionExtension'])

    # -> "Multi-platform, free open source software for visualization and image computing."
    template = env.from_string("{% github_repo_description 'Slicer/Slicer' %}")

    template.render()


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`file an issue`: https://github.com/jcfr/jinja2-github/issues


Code of Conduct
---------------

Everyone interacting in the jinja2-github project's codebases, issue trackers, chat
rooms, and mailing lists is expected to follow the `PyPA Code of Conduct`_.

.. _`PyPA Code of Conduct`: https://www.pypa.io/en/latest/code-of-conduct/

License
-------

Distributed under the terms of the `Apache 2.0`_ license, jinja2-github is free and open source software

.. image:: https://opensource.org/trademarks/osi-certified/web/osi-certified-120x100.png
   :align: left
   :alt: OSI certified
   :target: https://opensource.org/

.. _`Apache 2.0`: https://opensource.org/licenses/Apache-2.0

