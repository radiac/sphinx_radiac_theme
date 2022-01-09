***********************
Radiac.net Sphinx Theme
***********************

This Sphinx theme is a fork of the official `Read the Docs`_ theme, which adds:

* radiac.net colour scheme
* Top nav

.. _Read the Docs: http://www.readthedocs.org


Using in docs
=============

Install::

    pip install -e https://github.com/radiac/sphinx_radiac_theme.git

Add to ``conf.py``::

    import sphinx_radiac_theme
    extensions = [
        ...
        'sphinx_radiac_theme',
    ]
    html_theme = "sphinx_radiac_theme"

Optional settings for ``conf.py``::

    html_theme_options = {
      "radiac_project": "projectname",
      "radiac_options": [

      ],
    }


Developing
==========

#. Check out the project from git
#. Update ``conf.py`` as above, but add::

      html_theme_path = ["/path/to/sphinx_radiac_theme"]

#. Watch static and open the demo site in a browser::

      nvm install
      nvm use
      npm run dev

The upstream project does not currently use black, so take care to not apply
auto-formatting to files which originate upstream.


Releasing a new version
-----------------------

#. Build static::

      npm run build

#. Update the fork number in the version string in ``setup.py`` and
   ``sphinx_radiac_theme/__init__.py``

#. Commit and push to ``master``.

This project is not on pypi.


Merging from upstream
---------------------

#.  Pull into new branch::

      git remote add upstream https://github.com/readthedocs/sphinx_rtd_theme.git
      git fetch upstream
      git checkout master
      git pull
      git checkout -b merge-upstream
      git merge upstream/master

#.  Resolve any conflicts (ignoring ``sphinx_radiac_theme/static`` - we'll rebuild
    that). In particular, check for changes in these files:

    * ``README.rst`` - keep our version
    * ``setup.*``, ``MANIFEST.in`` - check for new ``sphinx_rtd_theme``
    * ``setup.py`` - update version (add ``.fork0`` to upstream)
    * ``sphinx_radiac_theme/__init__.py`` - update version and check theme name is
      ``sphinx_radiac_theme``
    * ``src/sass/theme.sass`` - make sure ``theme_variables`` is followed by
      ``radiac_variables`` and ``radiac_styles`` is at the bottom
    * ``sphinx_rtd_theme/*`` - move files over to ``sphinx_radiac_theme``

    Test with::

        npm install
        npm run dev

#.  Rebuild and push::

        npm run build
        git add .
        git commit
        git checkout master
        git merge merge-upstream
        git branch -d merge-upstream
        git push


More information
================

See original documentation for:

* Installing_
* Configuring_
* Contributing_

.. _Read the Docs: https://sphinx-rtd-theme.readthedocs.io/en/latest/
.. _Installing: https://sphinx-rtd-theme.readthedocs.io/en/latest/installing.html
.. _Configuring: https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html
.. _Contributing: https://sphinx-rtd-theme.readthedocs.io/en/latest/contributing.html
