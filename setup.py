from setuptools import setup

VERSION = '0.0.1'
AUTHOR = 'Alejandro Alonso Mayo'
AUTHOR_EMAIL = 'alejandroalonsomayo@gmail.com'
URL = 'https://github.com/AlejandroAM91/gaia'
DOWNLOAD_URL = f'https://github.com/AlejandroAM91/gaia/archive/v{VERSION}.tar.gz'
CLASSIFIERS = [
    "Programming Language :: Python :: 3.8",
    "License :: OSI Approved :: MIT License",
],

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = [
]

setup(
    name='am91-gaia',
    version = VERSION,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    description='Project generator',
    long_description = readme,
    long_description_content_type = 'text/markdown',
    url = URL,
    download_url = DOWNLOAD_URL,
    classifiers = list(CLASSIFIERS),
    install_requires = requirements + ['jinja2'],
    package_dir={'': 'src'},
    packages=['am91.gaia'],
    entry_points={
        'console_scripts': 'gaia = am91.gaia.cli:main',
    }
)

setup(
    name = 'am91-gaia-template-base',
    version = VERSION,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    description = 'Basic project template for gaia project generator',
    long_description = readme,
    long_description_content_type = 'text/markdown',
    url = URL,
    download_url = DOWNLOAD_URL,
    classifiers = list(CLASSIFIERS),
    install_requires = requirements + ['am91-gaia'],
    package_dir = {'': 'src'},
    packages = ['am91.gaia_template_base'],
    package_data = {
        'am91.gaia_template_base': [
            'templates/*.jinja',
            'templates/.*.jinja',
            'templates/**/*.jinja'
        ]
    },
    entry_points={
        'am91.gaia.template': 'base = am91.gaia_template_base',
    },
)
