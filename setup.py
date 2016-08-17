import os.path
from setuptools import setup, find_packages


def descr():
    return 'Visit https://github.com/neuront/pyjhashcode for details please.'

setup(
    name='jhashcode',
    version='0.4',
    author='Neuron Teckid',
    author_email='lene13@gmail.com',
    license='MIT',
    keywords='Java hashCode',
    url='https://github.com/neuront/pyjhashcode',
    description='Python implemented Java `hashCode` methods.',
    packages=['jhashcode'],
    long_description=descr(),
    install_requires=[],
    zip_safe=False,
    test_suite='tests',
    entry_points=dict(
        console_scripts=[],
    ),
)
