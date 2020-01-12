from test_utils import get_rendered_file


def test_underscore_replacement():
    context = {"name": "dummy-0.0.0"}
    filename = "__init__.py.jj2"
    rendered = get_rendered_file(filename, context)
    assert "dummy_0.0.0" in rendered
    assert "dummy-0.0.0" not in rendered
