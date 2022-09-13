from setuptools import setup, find_packages

setup(
    name="converter",
    packages=find_packages("app"),
    package_dir={"": "app"},
)