import io
import os
import sys
from subprocess import run, PIPE

from setuptools import setup

NAME = "b0mb3r"
DESCRIPTION = "Открытый и бесплатный СМС бомбер"
URL = "https://github.com/crinny/b0mb3r"
EMAIL = ""
AUTHOR = "crinny"
REQUIRES_PYTHON = ">=3.7.0"
VERSION = "2.5.1"

REQUIRED = ["aiohttp", "phonenumbers", "click", "sentry-sdk"]

if "com.termux" in os.environ.get("PREFIX", ""):  # If device is running Termux
    run(
        [
            "MULTIDICT_NO_EXTENSIONS=1",
            sys.executable,
            "-m",
            "pip",
            "install",
            "multidict",
            "--no-build-isolation",
            "--no-use-pep517",
        ],
        stdout=PIPE,
        encoding="ascii",
    )

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=["b0mb3r"],
    entry_points={
        "console_scripts": ["b0mb3r=b0mb3r.__main__:main", "bomber=b0mb3r.__main__:main",]
    },
    install_requires=REQUIRED,
    extras_require={},
    package_data={"b0mb3r": ["static/*/*", "templates/*", "services/*"]},
    license="Mozilla Public License 2.0",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: Android",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Internet",
        "License :: Free To Use But Restricted",
    ],
)
