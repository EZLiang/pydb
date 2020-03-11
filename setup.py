import setuptools

long_description = open("README.md", "r").read()

setuptools.setup(
    name="pydb",
    version="0.0.1",
    description="A database system for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EZLiang/pydb",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
