import setuptools


about = {}
with open('README.md', 'r') as f:
    readme = f.read()

setuptools.setup(
    name="bajson",

    version="0.0.5",
    author="bakyazi",
    author_email="berkay.akyazi@gmail.com",
    description="library for converting to/from json",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="MIT License",
    url="https://github.com/bakyazi/bajson",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 1 - Planning",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)