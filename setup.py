from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in compliance_management/__init__.py
from compliance_management import __version__ as version

setup(
	name="compliance_management",
	version=version,
	description="This is the app to manage the compliance documents",
	author="ITAthena",
	author_email="chd3.novo@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
