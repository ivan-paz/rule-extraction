# -*- coding: utf-8 -*-

#---------------------------------------------------------------
#                              rulex                       -----
#---------------------------------------------------------------
presets = (
(1, 1,'A',1),
(1, 2,'A',1),
(1, 3,'A',1),
(1, 4,'B',1)
)
presets = (
(1, 1,'A',1),
(2, 1,'A',1),
(1, 3,'A',1),
(1, 4,'B',1),
(1,11,'A',1),
(1,12,'A',1) )

# input presets in tuple format -> output -> rules json format
def rulex(presets):
    i = -1
    for preset_1 in presets:
        i = i + 1
        j = -1
        for preset_2 in presets:
            j = j + 1
            if( (preset_1 and preset_2) != None):
                if is_compressible(preset_1,preset_2) != False:
                    dictionary = is_compressible(preset_1,preset_2)
                    #print('dictionary',dictionary)
#################################################################                    
                    if dictionary != None:
                        rule = build_rule(preset_1, dictionary)
                        print(rule)
                        #delete rules preset_1 and preset_2 and app rule
                        lst = list(presets)
                        if rule not in lst:###### aqui voy
                            lst.append(rule)
                            lst[i] = None
                            lst[j] = None
                            presets = tuple(lst)
    #eliminate redundant
    rules = clear_Nones(presets)
    rules = non_redundant(rules)
    rules = clear_Nones(rules)
    print(rules)
    return rules
rulex(presets)

#---------------------------------------------------------------------------
#         is_compressible takes as inputs two presets and if they are   ----
#                 compressible returns a dictionary                     ----
#                        index -> value                                 ----
#     with the index in wich the presets are different and the values   ----
#---------------------------------------------------------------------------
def is_compressible(preset_1, preset_2):
    dictionary = {}
    if preset_1 == preset_2:
        return dictionary
    for i in range( len(preset_1) - 1 ):
        if(preset_1[i] != preset_2[i]):
            dictionary[i] = set( [ preset_1[i], preset_2[i] ] )
    print(dictionary)
    if bool(dictionary):
        if len(dictionary) <= preset_1[-1] and  preset_1[-2]== preset_2[-2]:
            return dictionary
        else:
            return False
#----------------------------------------------------------------------------
#                   tests
# if preset_1 == preset_2 returns empty dictionary
is_compressible( (1, 1,'A',1),(1, 1,'A',1) )
#Out: {}
# return dict with index -> different values
is_compressible( (1, 2,'A',1),(1, 1,'A',1) )
#Out: {1: {1, 2}}
is_compressible( (1, (1,2),'A', 1), (1, 11, 'A', 1) )
#Out: {1: {(1, 2), 11}}
is_compressible( (1, 1,'A',1),(1, 1,'B',1) )
#Out: False
is_compressible( (1, 1,'A',1),(2, 3,'A',1) )
#Out: False
is_compressible( (1, 1,'A',2),(2, 3,'A',1) )
#Out:  {0: {1, 2}, 1: {1, 3}}
#-------------------------------------------------------------------------

def build_rule(preset_1,my_dict):
    my_tuple = ()
    #print('preset',preset_1,'dictionary',my_dict)
    for element in my_dict:
        for value in my_dict[element]:
            #print(type(value))
            if(type(value)==tuple):
                for i in value: my_tuple = my_tuple + (i,)
            else:
                #print(value)
                    my_tuple = my_tuple + (value,)
        temp = []
        for i in my_tuple:
            if i not in temp:
                temp.append(i)
        temp.sort()
        my_tuple = tuple(temp)
        #check for contradictions to create the rule
        lst = list(preset_1)
        lst[element]=my_tuple
        preset_1 = tuple(lst)
    return preset_1
    
#my_dict =  {1: {(1, 2), 11}}     
#build_rule((1,11,'A',1),my_dict)
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
    
    