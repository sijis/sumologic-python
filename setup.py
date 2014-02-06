from setuptools import setup, find_packages

setup(
    name='sumologic',
    version = '0.1.2',
    description = 'Python library for working with the Sumo Logic api.',
    long_description = open('README.rst').read(),
    author = 'Sijis Aviles',
    author_email = 'sijis.aviles@gmail.com',
    packages = find_packages(),
    install_requires = ['requests'],
    keywords = "sumologic api python",
    url = 'https://github.com/sijis/sumologic-python',
    download_url = 'https://github.com/sijis/sumologic-python',
    platforms = ['OS Independent'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
    ],
)

