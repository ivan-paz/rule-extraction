# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 20:35:08 2016

@author: ivan
"""

presets = (
(1, 1,'A',1),
(2, 1,'A',1),
(1, 3,'A',1),
(1, 4,'B',1),
(1,11,'A',1),
(1,12,'A',1) )

rules = [(1, 4, 'B', 1), ((1, 2), 1, 'A', 1), (1, (1, 3, 11, 12), 'A', 1)]

def build_inference_rules(rules,presets):
    inf_rules = []
    _rules_by_classes = rules_by_classes(rules)
    presets = presets_by_classes(presets)
    for key in _rules_by_classes:
        for rule in _rules_by_classes[key]:
            print(inference_rule(rule,presets))
            
build_inference_rules(rules,presets)

def inference_rule(rule,presets_by_classes):
    inference_dict = {}
    for i in range( len(rule) - 2 ): #Change if format changes
        if type(rule[i]) == tuple:
            _class = rule[-2]  # Change this if the format changes
            different_keys = []
            for key in presets_by_classes:
                if key!= _class:
                    different_keys.append(presets_by_classes[key])
            new_interval = modify_interval(rule[i],i,different_keys )
            inference_dict[i]= new_interval
        else:
            inference_dict[i]=rule[i]
    return inference_dict
    
    
import itertools                   
def combine(template, options):
    products = [dict(zip(options, values)) for values in itertools.product(*options.values())]
    return [template.format(**p) for p in products]
pattern = '{name} likes {animal}s'
options = {'name': ['Alex', 'Sarah', 'Bob'], 'animal': ['cat', 'dog']}    
    
combine(pattern,options)


def modify_interval(interval, i, different_keys):
    new_interval = []
    temp_interval = []
    for j in range(len(interval) - 1 ):
        a = interval[j]
        b = interval[j + 1]
        #print(a,b)
        temporal = set()
        for dictionary in different_keys:
            for preset in dictionary:
               # print(preset[i])
                if not (a < preset[i] < b):
                    temporal.add(a)
                    temporal.add(b)
        if temporal!= set():
            temp_interval.append(temporal)
    for i in temp_interval: new_interval.append(tuple(i))
    return new_interval

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
