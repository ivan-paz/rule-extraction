# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 17:33:48 2017

@author: ivan
"""
presets = [
[ 6,         20,  0.6,   'D', 1 ],

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

rules = [
[ 6,         20,  0.6,   'D', 1 ],
((5.504405, 10.203962, 11.354432), 20, 0.6, 'A', 1),
((1.854298, 4.294679, 7.653983, 15.012693), 230, 0.6, 'A', 1),
((20.425354, 21.10586, 24.548191), 260, 0.6, 'B', 1),
(21.10586, (26, 67, 260, 370), 0.6, 'B', 1),
(99.598908, (7.928433, 14.141092), 0.6, 'C', 1),
(55.781054, (1.90927, 7.807612), 0.6, 'C', 1)]


#---------------------------------------------------------
#
#     Function to build set of Inference Rules
#
#----------------------------------------------------------
def inference_rules(presets,rules):
    rules_by_categories = rules_by_classes(rules)
    presets_by_categories = presets_by_classes(presets) 
    for category in rules_by_categories:
        print(category)
        rules = rules_by_categories[category]
        others = presets_other_category(category,presets_by_categories)
        for rule in rules:
            print('rule : ',rule)
            print('others : ')
            for i in others:
                for j in i:print(j)
            #take (rule,others) and create Inference Rules
#----------------------------------------------------------       
inference_rules(presets,rules)


def presets_other_category(category,presets_by_categories):
    presets_other_category = []
    for w in presets_by_categories:
        if w != category:
            presets_other_category.append(presets_by_categories[w])
    return presets_other_category








#------------------------------------------------------------------
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
#-----------------------------------------------------------------
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
#-------------------------------------------------------------------


rules_by_categories = rules_by_classes(rules)
for category in rules_by_categories:print(category)
    
presets_by_categories = presets_by_classes(presets)
for category in presets_by_categories:print(category)

presets_by_categories['A']













