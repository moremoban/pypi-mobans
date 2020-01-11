import os

from ruamel.yaml import YAML

from test_utils import get_file_content, get_rendered_file


def test_setup():
    filename = 'setup.py.jj2'
    with open(os.path.join("config", "data.yml"))as f:
        content = f.read()
    yaml = YAML(typ='safe')
    context = yaml.load(content)
    rendered = get_rendered_file(filename, context)
    expected = get_file_content('setup.py.output')
    assert expected == rendered


def test_setup_use_markers_true():
    filename = 'setup.py.jj2'
    with open(os.path.join("tests", "fixtures", "server_use_marker_true.yml"))as f:
        content = f.read()
    yaml = YAML(typ='safe')
    context = yaml.load(content)
    rendered = get_rendered_file(filename, context)
    print(rendered)    
    expected = get_file_content('setup_use_markers_true.py.output')
    assert expected == rendered


def test_setup_use_markers_false():
    filename = 'setup.py.jj2'
    with open(os.path.join("tests", "fixtures", "server_use_marker_false.yml"))as f:
        content = f.read()
    yaml = YAML(typ='safe')
    context = yaml.load(content)
    rendered = get_rendered_file(filename, context)
    expected = get_file_content('setup_use_markers_false.py.output')
    assert expected == rendered
