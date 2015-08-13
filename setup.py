try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='passkeyring',
    version='0.1',
    author='Ozan Safi',
    author_email='ozansafi@gmail.com',
    py_modules = ['passkeyring'],
    description='A python-keyring backend for the pass password manager.',
    install_requires=[
        "keyring>=5.4"
    ],
)

