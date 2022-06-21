from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in bizmap/__init__.py
from bizmap import __version__ as version

setup(
	name="bizmap",
	version=version,
	description="Bizmap Customizations",
	author="Bizmap technologies pvt ltd",
	author_email="hello@bizmap.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
