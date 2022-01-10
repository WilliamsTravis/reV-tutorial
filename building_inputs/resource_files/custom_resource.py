# -*- coding: utf-8 -*-
"""Building custom reV-compatible resource files.

Created on Wed Jan  5 13:21:06 2022

@author: twillia2
"""
import h5py
import pandas as pd


PROFILES = "./data/*srw"


def test():
    """Checking what these look like."""
    meta = pd.read_csv(META)
    meta.columns = ["index1", "index2", "latitude", "longitude", "path"]
    profiles = pd.read_csv(PROFILES, skiprows=17)
