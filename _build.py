import os
from typing import Any

from setuptools import Extension


def build(setup_kwargs: dict[str, Any]):
    return  # don't build the extension in this file
    setup_kwargs.update(
        ext_modules=[
            Extension(
                "hello",
                sources=["extension.cpp"],
                include_dirs=["include"],
                define_macros=[
                    ("VERSION_INFO", f'"{setup_kwargs["version"]}"')
                ],
                libraries=["libppgbin"],
                library_dirs=[os.path.join(os.getcwd(), "lib")],
            )
        ],
    )
