import jinja2

PATH_TO_TEMPLATES = './templates'


def get_rendered_file(filename, context):
    rendered = jinja2.Environment(
        loader=jinja2.FileSystemLoader(PATH_TO_TEMPLATES),
        trim_blocks=True, lstrip_blocks=True
    ).get_template(filename).render(context)
    return rendered
