import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="evalpy",
    version="0.0.1",
    author="David Rother",
    author_email="david@edv-drucksysteme.de",
    description="A lightweight framework to ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DavidRother/evalpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'click>=7.0',
        'pyqt5>=5.9.2',
        'pyqtgraph>=0.10.0',
        'six>=1.12'
    ],
    python_requires='>=3.6',
    entry_points='''
        [console_scripts]
        evalpy=evalpy.cli:cli
    '''
)
