# -*- coding: utf-8 -*-

import distutils.cmd
import os
import subprocess
from io import open

from setuptools import setup

fork_version_suffix = ".fork1"


class WebpackBuildCommand(distutils.cmd.Command):

    description = "Generate static assets"

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        if not "CI" in os.environ and not "TOX_ENV_NAME" in os.environ:
            subprocess.run(["npm", "install"], check=True)
            subprocess.run(
                ["node_modules/.bin/webpack", "--config", "webpack.prod.js"], check=True
            )


class WebpackDevelopCommand(distutils.cmd.Command):

    description = "Run Webpack dev server"

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        subprocess.run(
            [
                "node_modules/.bin/webpack-dev-server",
                "--open",
                "--config",
                "webpack.dev.js",
            ],
            check=True,
        )


class UpdateTranslationsCommand(distutils.cmd.Command):

    description = "Run all localization commands"

    user_options = []
    sub_commands = [
        ("extract_messages", None),
        ("update_catalog", None),
        ("transifex", None),
        ("compile_catalog", None),
    ]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        for cmd_name in self.get_sub_commands():
            self.run_command(cmd_name)


class TransifexCommand(distutils.cmd.Command):

    description = "Update translation files through Transifex"

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        subprocess.run(["tx", "push", "--source"], check=True)
        subprocess.run(["tx", "pull", "--mode", "onlyreviewed", "-f", "-a"], check=True)


setup(
    name="sphinx_radiac_theme",
    version=f"1.0.1alpha1{fork_version_suffix}",
    url="https://github.com/radiac/sphinx_radiac_theme",
    license="MIT",
    description="Radiac.net theme for Sphinx",
    long_description=open("README.rst", encoding="utf-8").read(),
    cmdclass={
        "update_translations": UpdateTranslationsCommand,
        "transifex": TransifexCommand,
        "build_assets": WebpackBuildCommand,
        "watch": WebpackDevelopCommand,
    },
    zip_safe=False,
    packages=["sphinx_radiac_theme"],
    package_data={
        "sphinx_radiac_theme": [
            "theme.conf",
            "*.html",
            "static/css/*.css",
            "static/css/fonts/*.*",
            "static/js/*.js",
        ]
    },
    include_package_data=True,
    # See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
    entry_points={
        "sphinx.html_themes": [
            "sphinx_radiac_theme = sphinx_radiac_theme",
        ]
    },
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*",
    install_requires=[
        "sphinx>=1.6",
        "docutils<0.18",
    ],
    tests_require=[
        "pytest",
    ],
    extras_require={
        "dev": [
            "transifex-client",
            "sphinxcontrib-httpdomain",
            "bump2version",
        ],
    },
    classifiers=[
        "Framework :: Sphinx",
        "Framework :: Sphinx :: Theme",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
    ],
    project_urls={
        "Source Code": "https://github.com/radiac/sphinx_radiac_theme",
    },
)
