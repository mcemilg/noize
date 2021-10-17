import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

README = (HERE/"readme.md").read_text()

setup(
    name="noize",
    version="0.0.1",
    description="A small library and a cli tool for applying noise to images.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/mcemilg/noize",
    author="MCG",
    author_email="mcemilguneyy@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(exclude="tests",),
    include_package_data=True,
    install_requires=["numpy==1.19.4",
                      "Pillow==8.0.1"],
    entry_points={
        "console_scripts": [
            "noize=noize.__main__:main",
        ]
    },
)
