# TODO: update docstrings

import os

from jinja2 import Environment, PackageLoader


def create_package(location, name, template_args):
    """
    Create a Python package scaffold on the filesystem.

    :return: None
    """
    create_modules(location, name)
    create_files(location, name, template_args)


def create_modules(location, name):
    """
    Create Python package scaffold base and test modules.

    :return: None
    """
    scaffold_path = os.path.join(location, name)

    os.mkdir(scaffold_path)

    for module_name in [name, 'tests']:
        code_module_path = os.path.join(scaffold_path, module_name)
        os.mkdir(code_module_path)
        with open(os.path.join(code_module_path, '__init__.py'), 'w'):
            pass


def create_files(location, name, template_kwargs):
    """
    Create Python package scaffold setup and dependency files.

    :return: None
    """
    env = Environment(
        loader=PackageLoader('py_package_scaffold', 'templates'),
    )
    filenames = [
        '.gitignore',
        'MANIFEST.in',
        'pytest.ini',
        'README.md',
        'requirements.txt',
        'requirements_dev.txt',
        'run_tests',
        'setup',
        'setup.py',
    ]

    for filename in filenames:
        template = env.get_template(filename.replace('.', '_'))
        template_string = template.render(
            **template_kwargs
        )
        with open(os.path.join(location, name, filename), 'w') as scaffold_file:
            scaffold_file.write(template_string)
