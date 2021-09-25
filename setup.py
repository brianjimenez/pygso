#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from glob import glob
from os.path import basename, splitext
from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand


class NoseTestCommand(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import nose

        nose.run_exit(argv=["nosetests"])


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="pygso",
    version="0.1.1",
    description="Glowworm Swarm Optimization library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Brian Jimenez-Garcia",
    author_email="br.jimenezgarcia@gmail.com",
    url="https://github.com/brianjimenez/pygso",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(i))[0] for i in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    license="MIT License",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords=[
        "gso",
        "glowworm",
        "swarm",
        "swarm intelligence",
        "optimization",
        "glowworm swarm optimization",
    ],
    python_requires=">=3.6",
    setup_requires=["nose"],
    install_requires=[
        "numpy",
    ],
    scripts=[],
    cmdclass={"test": NoseTestCommand},
)
