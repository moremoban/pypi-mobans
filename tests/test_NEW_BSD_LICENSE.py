from test_utils import get_rendered_file


def test_NEW_BSD_LICENSE():
    filename = 'NEW_BSD_LICENSE.jj2'
    context = {
        'copyright_year': '2018',
        'company': 'dummy',
        'name': 'first last',
        'something_else': 'hello world',
    }
    rendered = get_rendered_file(filename, context)
    assert '2018' in rendered
    assert 'dummy' in rendered
    assert 'first last' in rendered
    assert 'hello world' not in rendered
