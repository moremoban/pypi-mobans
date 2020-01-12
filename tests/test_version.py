from test_utils import get_rendered_file


def test_version():
    context = {
        "author": "author_name",
        "version": "0.0.1",
        "something_else": "hello world",
    }
    filename = "_version.py.jj2"
    rendered = get_rendered_file(filename, context)
    assert "author_name" in rendered
    assert "0.0.1" in rendered
    assert "hello world" not in rendered
