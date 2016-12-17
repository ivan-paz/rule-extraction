# -*- coding: utf-8 -*-
#------------------------------------------------------------
#                   input/output functions    
#                         for rulex
#------------------------------------------------------------
import json
"""
presets = (
(1, 1,'A',1),
(2, 1,'A',1),
(1, 3,'A',1),
(1, 4,'B',1),
(1,11,'A',1),
(1,12,'A',1) )
"""
#------------------------------------------------------------
#                                                         ---
#                write the presets into a file            ---
#                      with json format                   ---
#     write(variable_name, file_to_save)
#------------------------------------------------------------
# Write presets into file
def write_presets(variable_name, file_to_save = 'presets.json'):
    with open(file_to_save, 'w') as f:
        json.dump(variable_name, f)
        f.close
#------------------------------------------------------------
#                                                         ---
#                     Read presets form file              ---
#                      with json format                   ---
#------------------------------------------------------------
def load_presets(file_to_open = 'presets.json'):
    with open(file_to_open) as f:
        presets = json.load(f)
        f.close
    return presets
#------------------------------------------------------------
#                        Rule extraction
#------------------------------------------------------------
#from rulex_1 import *
#rules = rulex(presets)
#------------------------------------------------------------
#                                                         ---
#                write the rules into a file              ---
#                      with json format                   ---
#------------------------------------------------------------
def write_rules(rules, file_to_save = 'rules.json'):
    with open(file_to_save, 'w') as f:
        json.dump(rules, f)
        f.close
#------------------------------------------------------------
    
    
    
    
    
    
    
    
    
    
    
    
    
    