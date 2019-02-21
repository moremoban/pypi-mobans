import os
from moban.jinja2.engine import Engine

PATH_TO_TEMPLATES = './templates'


def get_rendered_file(filename, context):
    engine = Engine([PATH_TO_TEMPLATES])
    template = engine.get_template(filename)
    rendered = engine.apply_template(template, context, '')
    return rendered


def get_file_content(filename):
    with open(os.path.join("tests", "fixtures", filename))as f:
        return f.read()
