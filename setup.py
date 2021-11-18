from setuptools import setup

setup(
    name="Kamyroll-Python",
    version="1.2.3",
    description="Download shows from crunchyroll",
    url="https://github.com/hyugogirubato/Kamyroll-Python",
    author="hyugogirubato",
    license="MIT",
    scripts=["bin/kamyroll"],
    packages=["scripts/python"],
    install_requires=[
        "requests",
        "colorama",
        "termcolor",
        "pyxdg",
        "pysocks",
    ],
    tests_requires=[],
    zip_safe=False,
)
