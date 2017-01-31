# -*- coding: utf-8 -*-
"""
Create Inference Rule from a Strict Rule
Input: rule,others
rule: rule to be extended into inference rule
others: presets_different_class
"""
presets = [
[1,4,'A',1],
[1,6,'A',1],
[2,4,'A',1],
[2,6,'A',1],
[3,4,'A',1],
[3,6,'A',1],
[8,4,'A',1],
[8,6,'A',1],
[11,4,'A',1],
[11,6,'A',1],
[5,4,'B',1]
]
from rulex_1 import *
rules = rulex(presets)
rules = rulex(rules)
rules = [[5, 4, 'B', 1], ((1, 2, 3, 8, 11), (4, 6), 'A', 1)]


"""
rule =  ((5.504405, 10.203962, 11.354432), 20, 0.6, 'A', 1)
others = [
[6, 20, 0.6, 'D', 1],
[99.598908, 7.928433, 0.6, 'C', 1],
[99.598908, 14.141092, 0.6, 'C', 1],
[55.781054, 7.807612, 0.6, 'C', 1],
[55.781054, 1.90927, 0.6, 'C', 1],
[20.425354, 260, 0.6, 'B', 1],
[24.548191, 260, 0.6, 'B', 1],
[21.10586, 260, 0.6, 'B', 1],
[21.10586, 67, 0.6, 'B', 1],
[21.10586, 370, 0.6, 'B', 1],
[21.10586, 26, 0.6, 'B', 1]
]
"""
rule = ((1, 2, 3, 8, 11), (4, 6), 'A', 1)
presets_different_class = [[5,4,'B',1]]

def find_contradictions(rule,presets_different_class):
    for i in range(len(rule) -2 ):
        if type(rule[i])==tuple:
            print(rule[i])
            #COMPARE
            #find if there are identical rules differing
            #in that parameter
find_contradictions(rule,presets_different_class)


#find if there are identical presets differin in that parameter
def compare_with_presets(i,rule,presets_different_class):
    rule = cut_rule(i,rule)
    for preset in presets_different_class:
        preset = cut_preset(i,preset)
        print(rule, preset)
        #pairwise comparison

compare_with_presets(0,((1, 2, 3, 8, 11), (4, 6), 'A', 1),[[5,4,'B',1]])


def cut_rule(i,rule):
    rule = list(rule)
    rule = rule[:-2]
    del rule[i]
    return rule
cut_rule(0,((1, 2, 3, 8, 11), (4, 6), 'A', 1))

def cut_preset(i,preset):
    preset = preset[:-2] #Change this if format changes
    del preset[i]
    return preset
cut_preset(0,[5,4,'B',1])



