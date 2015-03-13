import os
from setuptools import setup, find_packages

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = "farinha",
    version = "0.1",
    author = "Willian Paixao",
    author_email = "willian@ufpa.br",
    packages = find_packages(),
    include_package_data = True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ],
)

