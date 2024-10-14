from setuptools import setup, find_packages

setup(
    name="myactuator_lib",
    version="2.0.0",
    packages=find_packages(),
    install_requires=[
        'python-can',
        'pymodbus==2.5.2 '
    ],
    author="Nathan Adkins",
    author_email="npa00003@mix.wvu.edu",
    description="Defines classes for controlling myactuator RMD motor",
    license="MIT",
    keywords="actuator robotics",
    url="https://github.com/nate-adkins/myactuator_lib",   # project homepage
)