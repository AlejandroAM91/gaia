from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="gaia",
    version="0.0.0",
    author="Alejandro Alonso Mayo",
    author_email="alejandroalonsomayo@gmail.com",
    description="Project generation",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/AlejandroAM91/gaia",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
    ],
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "gaia = gaia.__main__:main",
        ]
    }
)