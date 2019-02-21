import textwrap

from test_utils import get_rendered_file


def test_manifest():
    filename = 'MANIFEST.in.jj2'
    rendered = get_rendered_file(filename, {})
    expected_manifest = textwrap.dedent("""\
    include README.rst
    include LICENSE
    include CHANGELOG.rst
    recursive-include tests *
    """)
    assert expected_manifest == rendered
