# Source: https://stackoverflow.com/questions/458550/standard-way-to-embed-version-into-python-package

# Store the version here so:
#  - we don't load dependencies by storing it in __init__.py
#  - we can import it in setup.py for the same reason
#  - we can import it into your module module
__version__ = '0.12'

# Inside yourpackage/__init__.py:
# from .version import __version__

# Inside setup.py:
# exec(open('yourpackage/version.py').read())
# setup(
#    ...
#    version=__version__,
#    ...
