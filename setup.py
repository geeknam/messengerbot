from setuptools import setup

setup(
    name='messengerbot',
    packages=['messengerbot'],
    license='The MIT License (MIT)',
    version='0.1.2',
    description='Python client for FB Messenger Platform Bot',
    long_description=open('README.rst').read(),
    author='Nam Ngo',
    author_email='namngology@gmail.com',
    url='https://github.com/geeknam',
    keywords='bot facebook messenger platform',
    install_requires=['requests']
)

