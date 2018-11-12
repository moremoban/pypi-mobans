import textwrap

import jinja2

from test_utils import get_rendered_file


def test_requirements():
    context = {
        'dependencies': [
                'dependency',
                'dependency #with_comment',
                'dependency#with_comment_no_space',
                'dependency#egg=dependency',
                'git+https://github.com/user/repo#egg=repo',
                '# actual comment',
        ]
    }
    filename = 'requirements.txt.jj2'
    rendered = get_rendered_file(filename, context)
    expected_requirements = textwrap.dedent("""\
           dependency
           dependency #with_comment
           dependency#with_comment_no_space
           dependency#egg=dependency
           git+https://github.com/user/repo#egg=repo
           # actual comment
    """)
    assert expected_requirements == rendered
