from setuptools import setup, find_packages

setup(
    name='sumologic',
    version = '0.1.4',
    description = 'Python library for working with the Sumo Logic api.',
    long_description = open('README.rst').read(),
    author = 'Sijis Aviles',
    author_email = 'sijis.aviles@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires = ['requests'],
    keywords = "sumologic api python",
    url = 'https://github.com/sijis/sumologic-python',
    download_url = 'https://github.com/sijis/sumologic-python',
    platforms = ['OS Independent'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent',
    ],
)
