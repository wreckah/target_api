from setuptools import setup, find_packages

setup(
    name='target-api-client',
    version='0.1',
    description='Target@Mail.Ru API\'s client',
    long_description='',
    author='Alexander Pokatilov',
    author_email='wreckah@ya.ru',
    packages = find_packages(),
    install_requires = ['requests >= 2.5.0'],
)
