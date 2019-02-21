from test_utils import get_rendered_file, get_file_content


def test_setup():
    filename = 'setup.py.jj2'
    context = dict(
        description="test"
    )
    rendered = get_rendered_file(filename, context)
    expected_requirements = get_file_content('setup.py.output')
    assert expected_requirements == rendered
