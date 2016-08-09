#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.project_slug }}
----------------------------------

Tests for `{{ cookiecutter.project_slug }}` module.
"""

import pandas

{% if cookiecutter.use_pytest == 'y' -%}
import pytest
import pandas.util.testing as pdtest
{% else %}
import sys
import unittest
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'click' %}
from contextlib import contextmanager
from click.testing import CliRunner
{%- endif %}

from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}
{%- if cookiecutter.command_line_interface|lower == 'click' %}
from {{ cookiecutter.project_slug }} import cli
{%- endif %}


@pytest.fixture
def data():
    return pandas.DataFrame({
        'A': [1, 5, 9],
        'B': [2, 6, 0],
        'C': [3, 7, 1],
        'D': [4, 8, 2],
    }, index=list('abc'))


def test_load_example_data(data):
    result = {{ cookiecutter.project_slug }}.load_example_data()
    expected = data.copy()
    pdtest.assert_frame_equal(result, expected)


def test_transpose_square(data):
    result = {{ cookiecutter.project_slug }}.transpose_square(data)
    expected = pandas.DataFrame({
        'a': {'A':  1, 'B':  4, 'C':  9, 'D': 16},
        'b': {'A': 25, 'B': 36, 'C': 49, 'D': 64},
        'c': {'A': 81, 'B':  0, 'C':  1, 'D':  4}
    })
    pdtest.assert_frame_equal(result, expected)


@pytest.mark.parametrize(('value', 'decimal', 'expected'), [
    (0.03010, 2,  '3.01%'), (0.020000, 3,   '2.000%'),
    (0.10000, 2, '10.00%'), (5.000120, 3, '500.012%'),
    ('junk', 2, None),
])
def test_format_as_pct(value, decimal, expected):
    if expected is None:
        with pytest.raises(ValueError):
            {{ cookiecutter.project_slug }}.format_as_pct(value)
    else:
        result = {{ cookiecutter.project_slug }}.format_as_pct(value, decimal=decimal)
        assert result == expected


{% if cookiecutter.use_pytest == 'y' -%}
@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument.
    """
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


{%- if cookiecutter.command_line_interface|lower == 'click' %}
def test_command_line_interface():
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert '{{ cookiecutter.project_slug }}.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output

{%- endif %}
{% else %}
class Test{{ cookiecutter.project_slug|title }}(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass
{% if cookiecutter.command_line_interface|lower == 'click' %}
    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert '{{ cookiecutter.project_slug }}.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

{%- endif %}
{%- endif %}