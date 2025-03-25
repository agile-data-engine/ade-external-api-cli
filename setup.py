from setuptools import setup

setup(
    name='ade_ext',
    version='0.1.0',
    packages=['utils', 'commands'],
    py_modules=['ade_ext'],
    install_requires=[
        'Click ==8.1.3',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'ade = ade_ext:ade',
        ],
    },
)