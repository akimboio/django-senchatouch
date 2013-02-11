import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "senchatouch",
    version = "0.1",
    packages = find_packages(),
    url = "https://github.com/akimboio/django-senchatouch",
    description = read('README.md'),
    include_package_data = True,
    install_requires = [
        "django>=1.4",
    ],
    zip_safe = False
)
