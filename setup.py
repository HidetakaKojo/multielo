from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('LICENSE', 'r') as fh:
    license = fh.read()

setup(
    name='multielo',
    version='0.1.0',
    description='ELO rating for multipel player',
    long_description=long_description,
    long_description_context_type='text/markdown',
    license=license,
    url='https://github.com/HidetakaKojo/multielo',
    author='Hidetaka Kojo',
    author_email='hidetaka.kojo@gmail.com',
    install_requires=[],
    extras_require={},
    py_modules=['multielo'],
    test_suite='tests',
    python_requires='~=3.5',
)
