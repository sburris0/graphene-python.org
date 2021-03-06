"""Sphinx Graphene theme.
From https://github.com/graphql-python/graphene-python.org.
"""
import os
import time

__version__ = '0.1.{}'.format(str(time.mktime(time.gmtime())))
__version_full__ = __version__


def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return cur_dir
