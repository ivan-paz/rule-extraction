# -*- coding: utf-8 -*-
"""
Building rules by looking at contradictions
Created on Wed Dec  7 17:53:19 2016
@author: ivan
"""
presets = (
(1, 1,'A',1),
(1, 2,'A',1),
(1, 3,'A',1),
(1, 4,'B',1)
)
#presets = (
#(1, 1,'A',1),
#(2, 1,'A',1),
#(1, 3,'A',1),
#(1, 4,'B',1),
#(1,11,'A',1),
#(1,12,'A',1) )

def rulex(presets):
    i=-1
    for preset_1 in presets:
        i = i+1
        j = -1
        for preset_2 in presets:
            j = j+1
            if( (preset_1 and preset_2) != None):
                if is_compressible(preset_1,preset_2) != False:
                    dictionary = is_compressible(preset_1,preset_2)
                    if dictionary != None:
                        rule = build_rule(preset_1,dictionary)
                        lst = list(presets)
                        if rule not in lst:
                            lst.append(rule)
                            lst[i] = None
                            lst[j] = None
                            presets = tuple(lst)
    # Eliminate redundant rules
    rules = clear_Nones(presets)
    rules = non_redundant(rules)
    rules = clear_Nones(rules)
    print(rules)
#rulex(presets)

def is_compressible(preset_1,preset_2):
    dictionary = {}
    for i in range(len(preset_1) - 1):
        if(preset_1[i]!=preset_2[i]):
            dictionary[i]=set([preset_1[i],preset_2[i]])
    if bool(dictionary):
        if(len(dictionary) == preset_1[-1]):
            return dictionary
    else:
        return False
#is_compressible( (1,11,'A',1),(1,12,'A',1) )
#is_compressible( (1, (1,2),'A', 1), (1, 11, 'A', 1) )

def build_rule(preset_1,my_dict):
    my_tuple = ()
    for element in my_dict:
        for value in my_dict[element]:
            if(type(value)==tuple):
                for i in value: my_tuple = my_tuple + (i,)
            else:
                    my_tuple = my_tuple + (value,)
        temp = []
        for i in my_tuple:
            if i not in temp:
                temp.append(i)
        temp.sort()
        my_tuple = tuple(temp)
        lst = list(preset_1)
        lst[element]=my_tuple
        preset_1 = tuple(lst)
    return preset_1
    
def clear_Nones(tuple_type):
    temp = []
    for i in tuple_type:
        if i!=None:
            temp.append(i)
    return temp
    
def non_redundant(rules):
    counter = -1
    for rule1 in rules:
        counter = counter + 1
        for rule2 in rules:
            if rule2 != None:
                bolean = [(rule1 == rule2) for rule1, rule2 in zip(rule1,rule2)]
                for i in range(len(bolean)):
                    if bolean[i] == False:
                        if type(rule1[i])==type(rule2[i])==tuple:
                            a = [j in rule2[i] for j in rule1[i]]
                            count = 0
                            for entrance in a:
                                if entrance == True:
                                    count = count + 1
                                    if count == len(a):
                                        rules[counter]=None  
    return rules

#non_redundant([(1, 4, 'B', 1), (1, (1, 2), 'A', 1), (1, (1, 2, 3), 'A', 1)])
rulex(presets)

    
    
    
    
