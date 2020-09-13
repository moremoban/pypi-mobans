# flake8: noqa
import os

import moban_ansible.tests.files
import moban_ansible.engines.line_in_file
from moban.plugins.jinja2.engine import Engine
from moban.externals import file_system

PATH_TO_TEMPLATES = "./templates"


def get_rendered_file(filename, context):
    engine = Engine(file_system.get_multi_fs([PATH_TO_TEMPLATES]))
    template = engine.get_template(filename)
    rendered = engine.apply_template(template, context, "")
    return rendered


def get_file_content(filename):
    with open(os.path.join("tests", "fixtures", filename)) as f:
        return f.read()
