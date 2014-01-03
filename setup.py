from setuptools import setup, find_packages

setup(
    name='sumologic',
    version = '0.1.1',
    description='Python library for working with the Sumo Logic api.',
    author='Sijis Aviles',
    author_email='sijis.aviles@gmail.com',
    packages = find_packages(),
    install_requires = ['requests'],
    keywords = "sumologic api python",
    url = 'https://github.com/sijis/sumologic-python',
)

