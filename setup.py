from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.0'
PACKAGE_NAME = 'jsonMojo'
AUTHOR = 'Jiena Gu McLellan'
AUTHOR_EMAIL = 'jienagu90@gmail.com'
URL = 'https://github.com/jienagu/jsonMojo'
LICENSE = 'Apache License 2.0'
DESCRIPTION = 'A series of utility functions to help with tidy json via python dictionary.'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = ['json']

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )