#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 08:51:35 2023

also basically just a data storage enumeration

@author: sebas
"""

class Reaction:
    
    def __init__(self, reactants, products, EquilibriumConst, Enthalpy):
        self.Reactants = reactants
        self.Products = products
        self.EquilibriumConst = EquilibriumConst
        self.Enthalpy = Enthalpy