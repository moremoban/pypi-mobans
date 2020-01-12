import textwrap

from test_utils import get_rendered_file


def test_pipfile():
    context = {
        "dependencies": [
            "dependency",
            "dependency=1.0",
            "dependency==1.0",
            "dependency>1.0",
            "dependency>=1.0",
            "dependency<1.0",
            "dependency<=1.0",
            "dependency~1.0",
            "dependency~=1.0",
        ],
        "dev_dependencies": [
            "dev_dependency",
            "dev_dependency=1.0",
            "dev_dependency==1.0",
            "dev_dependency>1.0",
            "dev_dependency>=1.0",
            "dev_dependency<1.0",
            "dev_dependency<=1.0",
            "dev_dependency~1.0",
            "dev_dependency~=1.0",
        ],
    }
    filename = "Pipfile.jj2"
    rendered = get_rendered_file(filename, context)
    expected_pipfile = textwrap.dedent(
        """\
           [[source]]
           url = 'https://pypi.python.org/simple'
           verify_ssl = true
           name = 'pypi'

           [requires]
           python_version= '3.6'

           [packages]
           dependency = "*"
           dependency = '=1.0'
           dependency = '==1.0'
           dependency = '>1.0'
           dependency = '>=1.0'
           dependency = '<1.0'
           dependency = '<=1.0'
           dependency = '~1.0'
           dependency = '~=1.0'

           [dev-packages]
           nose = "*"
           mock = "*"
           codecov = "*"
           coverage = "*"
           flake8 = "*"
           dev_dependency = "*"
           dev_dependency = '=1.0'
           dev_dependency = '==1.0'
           dev_dependency = '>1.0'
           dev_dependency = '>=1.0'
           dev_dependency = '<1.0'
           dev_dependency = '<=1.0'
           dev_dependency = '~1.0'
           dev_dependency = '~=1.0'
    """
    )
    assert expected_pipfile == rendered
