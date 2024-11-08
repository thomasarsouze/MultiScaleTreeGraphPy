# MultiScaleTreeGraphPy

[![Actions Status][actions-badge]][actions-link]
[![Documentation Status][rtd-badge]][rtd-link]

[![PyPI version][pypi-version]][pypi-link]
[![Conda-Forge][conda-badge]][conda-link]
[![PyPI platforms][pypi-platforms]][pypi-link]

[![GitHub Discussion][github-discussions-badge]][github-discussions-link]

<!-- SPHINX-START -->
This `Python` package is a wrapper around the `Julia` package `MultiScaleTreeGraph.jl` available [here](https://github.com/VEZY/MultiScaleTreeGraph.jl) (documentation [here](https://vezy.github.io/MultiScaleTreeGraph.jl/stable/))which is a package for reading, writting, analysing and ploting MTG (Multi-scale Tree Graph) files. The package is designed to be used in the context of plant architecture analysis.

> **Note**
>
> This package is still in development and should be used with caution. It is meant to be a proof of concept !

> **Note**
>
> This package is based on the implmentation of the `diffeqpy` package available [here](https://github.com/SciML/diffeqpy/tree/master)

## Installation
Builld yourself a dedicated `conda` environment. Although it relies on `Julia`, it is not mandatory to have `Julia` installed on your machine. The package will download the `Julia` binaries for you if it can't find it.
```bash
conda create -n MultiScaleTreeGraphPy python=3.10
conda activate MultiScaleTreeGraphPy
conda add -c conda-forge xxx xxx (julia) ... # if you want to install a local version of julia in the environment
git clone https://github.com/thomasarsouze/MultiScaleTreeGraphPy.git
cd MultiScaleTreeGraphPy
pip install -e .
```

Then you're ready to go ! (First time you run the package, it will download the `Julia` binaries and dependancies, and pre-compile the packages, so it might take a while)
```python
from multiscaletreegraphpy import mtg
my_mtg = mtg.read_mtg("path/to/mtg/file.mtg")
df = mtg.DataFrame(my_mtg)
df
mtg.node_attributes(my_mtg)
...
```

<!-- prettier-ignore-start -->
[actions-badge]:            https://github.com/thomasarsouze/MultiScaleTreeGraphPy/workflows/CI/badge.svg
[actions-link]:             https://github.com/thomasarsouze/MultiScaleTreeGraphPy/actions
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/MultiScaleTreeGraphPy
[conda-link]:               https://github.com/conda-forge/MultiScaleTreeGraphPy-feedstock
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  https://github.com/thomasarsouze/MultiScaleTreeGraphPy/discussions
[pypi-link]:                https://pypi.org/project/MultiScaleTreeGraphPy/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/MultiScaleTreeGraphPy
[pypi-version]:             https://img.shields.io/pypi/v/MultiScaleTreeGraphPy
[rtd-badge]:                https://readthedocs.org/projects/MultiScaleTreeGraphPy/badge/?version=latest
[rtd-link]:                 https://MultiScaleTreeGraphPy.readthedocs.io/en/latest/?badge=latest

<!-- prettier-ignore-end -->
