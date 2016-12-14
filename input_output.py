# -*- coding: utf-8 -*-
#------------------------------------------------------------
#                   input/output function    
#                         for rulex
#------------------------------------------------------------
#                                                         ---
#                write the rules into a file              ---
#                      with json format                   ---
#------------------------------------------------------------
import json
def output(rules,filename):
    f = open(filename,'w')
    for rule in rules:
        rule = json.dumps(rule)
        f.write(rule)
    f.close
#-------------------------------------------------------------
#     Example  write the presets into a txt file
#-------------------------------------------------------------
presets = (
(1, 1,'A',1),
(2, 1,'A',1),
(1, 3,'A',1),
(1, 4,'B',1),
(1,11,'A',1),
(1,12,'A',1) )
output(presets,'in.json')
#----------------------------------------------------------------
#                                                             ---
#                  read rules or presets form file            ---
#                                                             ---
#----------------------------------------------------------------
def read_input(filename):
    f = open(filename,'r')
    f.readlines()
    print(f)
    f.close
    return presets
#----------------------------------------------------------------    
presets = read_input('in.json')
for i in presets: print(i,type(i))
#----------------------------------------------------------------