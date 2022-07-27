#!/usr/bin/env python3
import pathlib
import re
import sys

from setuptools import find_packages, setup

WORK_DIR = pathlib.Path(__file__).parent
MINIMAL_PY_VERSION = (3, 7)

if sys.version_info < MINIMAL_PY_VERSION:
    raise RuntimeError('rolling_dice works only with Python {}+'.format('.'.join(map(str, MINIMAL_PY_VERSION))))


def get_version() -> str:
    """
    Read version

    :return: str
    """
    txt = (WORK_DIR / 'rolling_dice' / '__init__.py').read_text('utf-8')
    try:
        return re.findall(r"^__version__ = '([^']+)'\r?$", txt, re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')


setup(
    name='rolling_dice',
    version=get_version(),
    packages=find_packages(exclude=('tests', 'tests.*')),
    url='https://github.com/M9SCO/diceroll',
    license='MIT',
    author='Chernov M_9SCO Grigorii',
    author_email='chr.grigorii@gmail.com',
    python_requires='>=3.7',
    description='Is a pretty simple library for rolling dice',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    install_requires=[
        'lark>=1.1.2'
    ],
    include_package_data=False,
)
