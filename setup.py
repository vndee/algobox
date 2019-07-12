import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name = "algobox",
    version = "1.0.3",
    description = "Modern algorithms implementation with native python",
    long_description = README,
    long_description_content_type = "text/markdown",
    url = "https://github.com/vndee/algobox",
    author = "Duy Huynh",
    author_email = "hvd.huynhduy@gmail.com",
    license = "MIT",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    package = ["algobox"],
    include_package_data = True,
    install_requires = [],
    entry_points = {
        "console_scripts": [
            "vndee=pyalgo.__main__:main"
        ]
    },
)
