from __future__ import annotations

import importlib.metadata

import multiscaletreegraphpy as m


def test_version():
    assert importlib.metadata.version("multiscaletreegraphpy") == m.__version__
