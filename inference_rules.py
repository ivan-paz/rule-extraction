# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 20:35:08 2016

@author: ivan
"""

"""
presets = (
(1, 1,'A',1),
(2, 1,'A',1),
(1, 3,'A',1),
(1, 4,'B',1),
(1,11,'A',1),
(1,12,'A',1) )
rules = [(1, 4, 'B', 1), ((1, 2), 1, 'A', 1), (1, (1, 3, 11, 12), 'A', 1)]
#-----------------------------------------------------------------------------------
presets = (
(1, 1, 1, 'A', 1),
(1, 2, 1, 'A', 1),
(1, 4, 1, 'A', 1),
(2, 1, 1, 'A', 1),
(1, 3, 1, 'B', 1) )
rules =  [(1, 3, 1, 'B', 1), ((1, 2), 1, 1, 'A', 1), (1, (1, 2, 4), 1, 'A', 1)]
"""
def build_inference_rules(rules,presets):
    inference_rules = []
    _rules_by_classes = rules_by_classes(rules)
    presets = presets_by_classes(presets)
    for key in _rules_by_classes:
        for rule in _rules_by_classes[key]:
            #print(key,rule)
            tmp = build_rules( inference_dict( rule, presets ) )
            for rule in tmp: inference_rules.append(rule)
    return inference_rules   
#build_inference_rules(rules,presets)

import itertools
def build_rules(inference_dict):
    inference_rules = []
    a = inference_dict.items()
    items = []
    for i in a:
        if type(i[1]) == int:
            items.append([i[1]])
        else:
            tmp = []
            for j in i[1]:
                tmp.append(list(j))
            items.append(tmp)
    a = list(itertools.product(*items))
    for i in a:
        rule = ()
        for j in i:
            if type(j) == int:
                rule = rule + (j,)
            elif (type(j)== list and type(j[0])==str):
                    rule = rule + ( j[0] ,)
            else:
                rule = rule + (tuple(j),)  
        print(rule)
        inference_rules.append(rule)
    return inference_rules
    
#build_rules({0: [(1, 2)], 1: 1})
#build_rules({0: 1, 1: [(1, 3), (11, 12)]})
#inference_dict((1, (1, 2, 4), 1, 'A', 1), pbc)
#3pbc = presets_by_classes(presets)

def inference_dict(rule,presets_by_classes):
    inference_dict = {}
    for i in range( len(rule) - 1 ): #Change if format changes
        if type(rule[i]) == tuple:
            _class = rule[-2]  # Change this if the format changes
            different_keys = []
            for key in presets_by_classes:
                if key != _class:
                    different_keys.append(presets_by_classes[key])
            new_interval = modify_interval( rule[i],i, different_keys )
            inference_dict[i]= new_interval
        else:
            inference_dict[i]=rule[i]
    return inference_dict

def modify_interval(interval, i, different_keys):
    new_interval = []
    temp_interval = []
    for j in range( len(interval) - 1 ):
        a = interval[j]
        b = interval[j + 1]
        #print(a,b)
        temporal = set()
        for dictionary in different_keys:
            for preset in dictionary:
                if not (a < preset[i] < b):
                    temporal.add(a)
                    temporal.add(b)
                elif ( a < preset[i] < b ) and (j == len(interval) - 2):
                    temporal.add(b)
        if temporal != set():
            temp_interval.append(temporal)
    for i in temp_interval: new_interval.append(tuple(i))
    return new_interval
    
#-------------------------------------------------------------------------------
def rules_by_classes(rules):
    rules_by_classes = {}
    for rule in rules:
        _class = rule[-2] # Change this if the format changes
        if _class not in rules_by_classes:
            rules_by_classes[_class] = list()
            rules_by_classes[_class].append(rule)
        else:
            rules_by_classes[_class].append(rule)
    return rules_by_classes
#rules_by_classes(rules)
def presets_by_classes(presets):
    presets_by_classes = {}
    for preset in presets:
        _class = preset[-2] # Change this if the format changes
        if _class not in presets_by_classes:
            presets_by_classes[_class]= list()
            presets_by_classes[_class].append(preset)
        else:
            presets_by_classes[_class].append(preset)
    return  presets_by_classes
#presets_by_classes(presets)