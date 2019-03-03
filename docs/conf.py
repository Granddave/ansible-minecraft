#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import os
import shlex
import sys

extensions = ["sphinx.ext.todo", "sphinx.ext.githubpages", "m2r"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Ansible Minecraft Role"
version = "4.3.2"


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [".tox", "_build"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

todo_include_todos = True

html_theme = "sphinx_rtd_theme"
htmlhelp_basename = "ansible-minecraft-doc"
# HTML options
html_theme = "sphinx_rtd_theme"
html_short_title = "ansible-minecraft"
html_use_index = True
html_show_sourcelink = False
html_static_path = ["_static"]
