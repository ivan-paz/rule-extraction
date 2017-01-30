# -*- coding: utf-8 -*-
"""
Create Inference Rule from a Strict Rule
Input: rule,others
rule: rule to be extended into inference rule
others: presets_different_class
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


def inference_rule(rule,presets_different_class):
    for i in range(len(rule) -2 ):
        if type(rule[i])==tuple:
            print(rule[i])
            #find if there are identical rules differing
            #in that parameter
inference_rule(rule,others)

# #find if there are identical rules differing
            #in that parameter