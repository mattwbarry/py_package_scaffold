import pip
from setuptools import setup, find_packages

APP_NAME = 'py_package_scaffold'
VERSION = '0.0.1'

REQUIRED = [
    str(ir.req)
    for ir
    in pip.req.parse_requirements(
        'requirements.txt', session=pip.download.PipSession()
    )
]

SETTINGS = {
    'name': APP_NAME,
    'version': VERSION,
    'author': 'Matt Barry',
    'author_email': 'mattwbarry@gmail.com',
    'packages': find_packages(exclude=['tests']),
    'include_package_data': True,
    'url': 'https://github.com/essessinc/py_package_scaffold.git',
    'license': 'None',
    'description': 'Scaffold your Python packages.',
    'long_description': open('README.md').read(),
    'install_requires': REQUIRED,
    'classifiers': [
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    'entry_points': {
        'console_scripts': [
        ],
    }
}
setup(**SETTINGS)
