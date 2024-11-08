import sys

from . import load_julia_packages
mtg, _ = load_julia_packages("MultiScaleTreeGraph", "PythonCall")
from juliacall import Main

sys.modules[__name__] = mtg # mutate myself