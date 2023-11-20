#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 09:01:02 2023

assume all concentrations in molarity
assume solvent is water, but all properties easily changible



@author: sebas
"""

class Solution:
    
    def __init__(self, Volume, Species, Concentrations):
        self.Volume = Volume
        self.Species = Species
        self.Concentrations = Concentrations