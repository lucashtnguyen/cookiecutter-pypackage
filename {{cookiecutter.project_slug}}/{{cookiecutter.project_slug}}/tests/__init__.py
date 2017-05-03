from pkg_resources import resource_filename

import pytest

import {{ cookiecutter.project_slug }}

def test(*args):
    options = [resource_filename('{{ cookiecutter.project_slug }}', 'tests')]
    options.extend(list(args))
    return pytest.main(options)
