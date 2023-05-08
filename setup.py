from setuptools import setup, find_packages

setup(
    name="MARS",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add your project's dependencies here
    ],
    entry_points={
        "console_scripts": [
            "MARS=MARS.main:main",
        ],
    },
)