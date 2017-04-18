# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 11:21:59 2016

@author: ivan
"""


# Example  1

presets = [
[ 1,         1,  1,   'D', 1 ],

[ 11.354432, 20, 0.6, 'A', 1 ],
[ 10.203962, 20, 0.6, 'A', 1 ],
[ 5.504405,  20, 0.6, 'A', 1 ],

[ 1.854298, 230, 0.6, 'A', 1 ],
[ 7.653983, 230, 0.6, 'A', 1 ],
[ 15.012693, 230, 0.6, 'A', 1 ],
[ 4.294679, 230, 0.6, 'A', 1 ],

[ 20.425354, 260, 0.6, 'B', 1 ],
[ 24.548191, 260, 0.6, 'B', 1 ],
[ 21.10586, 260, 0.6, 'B', 1 ],

[ 21.10586, 67, 0.6, 'B', 1 ],
[ 21.10586, 370, 0.6, 'B', 1 ],
[ 21.10586, 26, 0.6, 'B', 1 ],

[ 99.598908, 7.928433, 0.6, 'C', 1 ],
[ 99.598908, 14.141092, 0.6, 'C', 1 ],

[ 55.781054, 7.807612, 0.6, 'C', 1 ],
[ 55.781054, 1.90927, 0.6, 'C', 1 ] ]


from rulex_1 import *
#Strict Rules
rules = rulex(presets)
for i in rules:print(i)
#-----------------------------------------------------
from inference_rules import *
#Inference Rules from Strict Rules
inference_rules = build_inference_rules(rules,presets)
for i in inference_rules:print(i)


#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------   

#  Example 2

"""
Three concrete examples of rule extraction
to analyze how to manage the interval breaking
""" 
from rulex_1 import *
from inference_rules import *

presets = [
[1, 1, 'A', 1],
[2, 1, 'A', 1],
[3, 1, 'B', 1],
[4, 1, 'A', 1],
[6, 1, 'A', 1]
]
rules = rulex(presets)
rules = rulex(rules)
print(type(rules))
inference_rules = build_inference_rules(rules,presets)



#  Example  3 
presets = [
[1,  4, 'A', 1],
[1,  6, 'A', 1],
[2,  4, 'A', 1],
[2,  6, 'A', 1],
[3,  4, 'A', 1],
[3,  6, 'A', 1],
[8,  4, 'A', 1],
[8,  6, 'A', 1],
[11, 4, 'A', 1],
[11, 6, 'A', 1],
[5,  4, 'B', 1]
]
rules = rulex(presets)
rules = rulex(rules)
inference_rules = build_inference_rules(rules,presets)
"""
current out
((1, 2), (4, 6), 'A')
((2, 3), (4, 6), 'A')
((8, 11), (4, 6), 'A')
(5, 4, 'B')

it should be:
((1,2,3),(4,6), 'A', 1),
((8,11), (4,6), 'A', 1),
(5, 4,'B', 1)
"""

presets = [
[1,  6, 'A', 1],
[3,  6, 'A', 1],
[2,  4, 'A', 1],
[2,  8, 'A', 1]
]
rules = rulex(presets)
rules = rulex(rules)

#-----------------------------------------------------------
# This example shows when the order in rulex matters
presets = [
[ 5, 5, 'D', 1],
[ 2, 7, 'D', 1],
[ 5, 7, 'D', 1]
]
rules = rulex(presets)
rules1 = rulex(rules)

presets = [ ( (2,5), 7, 'D', 1), ( 5, 5, 'D', 1)]
rules = rulex(presets)
rules1 = rulex(rules)
#-----------------------------------------------------------

presets = [
((2, 5), 7, 'D',1), (4, 7, 'D',1)
]
rules = rulex(presets)
rules1 = rulex(rules)



