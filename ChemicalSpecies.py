#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 08:31:40 2023

basically just a data storing enumeration

@author: sebas
"""

class ChemicalSpecies:
    
    def __init__(self, name, MolarMass):
        self.Name = name
        self.MolarMass = MolarMass