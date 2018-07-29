from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
"attrs==17.4.0",
"cycler==0.10.0",
"matplotlib==2.1.2",
"numpy==1.14.1",
"parameterized==0.6.1",
"pluggy==0.6.0",
"py==1.5.2",
"pyparsing==2.2.0",
"pytest==3.4.2",
"python-dateutil==2.6.1",
"pytz==2018.3",
"scipy==1.0.0",
"six==1.11.0",
"spectrum==0.7.3"
]

setup(
    name='trainer',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='My trainer application package.'
)
