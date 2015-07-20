import os


here = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
PROJECT_ROOT = os.path.realpath(here("..", ".."))
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
root = lambda *x: os.path.realpath(os.path.join(os.path.abspath(PROJECT_DIR), *x))
