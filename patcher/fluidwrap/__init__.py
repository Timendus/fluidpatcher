"""
Description: ctypes wrapper for fluidsynth library
"""

try:
    from .fluid2x import *
except:
    from .fluid1x import *
