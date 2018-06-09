import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ckan2blockchain",
    version="1.0.0",

    author="Milan Pikula, Lukas Balazik",
    author_email="milan.pikula@nases.gov.sk",
    description="Push CKAN dataset hashes to Ethereum blockchain",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/milankowww/ckan2blockchain",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_scripts': [
            'ckan2blockchain = ckan2blockchain.main:main'
        ],
    },
)

# vim: ai ts=4 sts=4 et sw=4 ft=python
