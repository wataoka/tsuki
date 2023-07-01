from setuptools import setup, find_packages

setup(
    name='tsuki',
    version='0.1',
    packages=find_packages(),
    install_requires=['numpy', 'pillow', 'emoji'],
    author='wataoka',
    author_email='wataoka.koki@gmail.com',
    description='Package to draw images with moon emoji',
    url='https://github.com/wataoka/tsuki',
)
