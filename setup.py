from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in self_made/__init__.py
from self_made import __version__ as version

setup(
	name="self_made",
	version=version,
	description="Self made module for testing",
	author="Omar Habeeb",
	author_email="omar@dlisaudi.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
