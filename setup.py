from setuptools import setup, find_packages

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Science/Research",
    "Operating System :: OS Independent",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Programming Language :: Python :: 3",
]

setup(
    name="ioNERDSS",
    version="1.0.36",
    requires=["python (>=3.6)"],
    description="Package for analysing NERDSS inputs and outputs.",
    long_description="A python package for analysing inputs and outputs for NERDSS simulator, including generating input files for Platonic solids and output visualization, etc.",
    url="",
    author="Zixiu (Hugh) Liu",
    author_email="zliu140@jhu.edu",
    license="GPL-3.0",
    classifiers=classifiers,
    keywords="NERDSS Simulation, Analysis Tools",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "tqdm",
        "PyQt6",
        "pyqtgraph",
        "PyOpenGL",
        "biopython",
    ],
)
