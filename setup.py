from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='bisneto-mathlib',
    version='0.0.3',
    url='https://github.com/hbisneto/Mathematics',
    license='MIT License',
    author='Heitor Bisneto',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='heitor.bardemaker@live.com',
    keywords=['bisneto', 'mathlib', 'math', 'lib'],
    description='Math Library',
    packages=['mathlib'],
    install_requires=[''],)