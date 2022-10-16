from setuptools import setup, find_packages

with open("README.md", "r") as fp:
    long_desc = fp.read()

requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Control-Wrapper",
    version="1.0.0",
    license="MIT",
    description="Python API Wrapper for ControlPanel (https://controlpanel.gg)",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    author="Ferks-FK",
    url="https://github.com/Ferks-FK/Control-Wrapper",
    install_requires=requirements,
    python_requires=">=3.8.0",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 1 - Development/Alpha",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ],
)