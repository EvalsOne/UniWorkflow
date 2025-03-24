from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="uniworkflow",
    version="0.1.8",
    author="Quentin",
    author_email="tagriver@gmail.com",
    description="A Python library for integrating with various workflow providers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EvalsOne/uniworkflow",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.25.1",
    ],
)
