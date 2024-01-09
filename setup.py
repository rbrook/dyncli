from setuptools import setup

setup(
    name="dcli",
    version="0.1.1",
    py_modules=["dyncli"],
    entry_points={
        "console_scripts": [
            "dcli=dyncli:client",
        ],
    },
)
