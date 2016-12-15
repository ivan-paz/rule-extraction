# -*- coding: utf-8 -*-
#------------------------------------------------------------
#                   input/output functions    
#                         for rulex
#------------------------------------------------------------
import json

presets = (
(1, 1,'A',1),
(2, 1,'A',1),
(1, 3,'A',1),
(1, 4,'B',1),
(1,11,'A',1),
(1,12,'A',1) )
#------------------------------------------------------------
#                                                         ---
#                write the presets into a file            ---
#                      with json format                   ---
#------------------------------------------------------------
# Write presets into file
def write_presets():
    with open('presets.json', 'w') as f:
        json.dump(presets, f)
        f.close

write_presets()

#------------------------------------------------------------
#                                                         ---
#                     Read presets form file              ---
#                      with json format                   ---
#------------------------------------------------------------
def load_presets():
    with open('presets.json') as f:
        presets = json.load(f)
        f.close
    return presets

presets = load_presets()


#------------------------------------------------------------
#                        Rule extraction
#------------------------------------------------------------
from rulex_1 import *
rules = rulex(presets)

#------------------------------------------------------------
#                                                         ---
#                write the rules into a file              ---
#                      with json format                   ---
#------------------------------------------------------------
def write_rules():
    with open('rules.json', 'w') as f:
        json.dump(rules, f)
        f.close

write_rules()  








    
    
    
    
    
    
    
    
    
    
    
    
    
    
    