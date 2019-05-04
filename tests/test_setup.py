import os

from ruamel.yaml import YAML

from test_utils import get_file_content, get_rendered_file


def test_setup():
    filename = 'setup.py.jj2'
    with open(os.path.join("config", "data.yml"))as f:
        content = f.read()
    yaml = YAML(typ='safe')
    context = yaml.load(content)
    print(context)
    rendered = get_rendered_file(filename, context)
    expected = get_file_content('setup.py.output')
    assert expected == rendered
