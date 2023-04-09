# Example 1: simple setup.py file for a pacakge called packagename

# Import "setup" method from setuptools
import os
import shutil

from setuptools import setup
from setuptools import find_packages

# setup is the gateway to the package build process.
# The only required components for a package are
# the name, author and contact, and description.
setup(
    name="penet",
    version="0.1.0",
    license="MIT License",
    url="https://github.com/JUGGHM/PENet_ICRA2021",
    packages=find_packages(),
)
