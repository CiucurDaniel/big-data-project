import pandas as pd
import numpy as np
from itertools import combinations

# ## Fisierul de input (format)
# 
# Fiserul este un **csv** cu urmatorul format:
# 
# ```
# item1, item2, item3, ... so on
#  , t, ...
# t, t, t,...
# t, t, ...
# ... so on...```

# Cititul datelor si pre-procesarea acestora
df = pd.read_csv("test_data.csv", low_memory=False)

#df.head()
#display(df)


# Indexam fiecare item din header-ul fisierului cu date.

item_list = list(df.columns)
item_dict = dict()

for i, item in enumerate(item_list):
    item_dict[item] = i + 1

item_dict


# Extragem tranzactiile din data set.

transactions = list()

for i, row in df.iterrows():
    transaction = set()
    
    for item in item_dict:
        if row[item] == 't':
            transaction.add(item_dict[item])
    transactions.append(transaction)
    
transactions


# ## Functii utility

# **get_support** functie care calculeaza valoarea support pentru un anumit set. Ca input avem set-ul pe care il verifcam si numarul de tranzactii.

def get_support(transactions, item_set):
    match_count = 0
    for transaction in transactions:
        if item_set.issubset(transaction):
            match_count += 1
            
    return float(match_count/len(transactions))


# **self_join** efectueaza un self-join in ultimul nivel de de valid sets. Face un join intre seturi prin uniune. Daca lungimea este mai mare decat nivelul curent, facem discard acestui set.

def self_join(frequent_item_sets_per_level, level):
    current_level_candidates = list()
    last_level_items = frequent_item_sets_per_level[level - 1]
    
    if len(last_level_items) == 0:
        return current_level_candidates
    
    for i in range(len(last_level_items)):
        for j in range(i+1, len(last_level_items)):
            itemset_i = last_level_items[i][0]
            itemset_j = last_level_items[j][0]
            union_set = itemset_i.union(itemset_j)
            
            if union_set not in current_level_candidates and len(union_set) == level:
                current_level_candidates.append(union_set)
                
    return current_level_candidates


def get_single_drop_subsets(item_set):
    single_drop_subsets = list()
    for item in item_set:
        temp = item_set.copy()
        temp.remove(item)
        single_drop_subsets.append(temp)
        
    return single_drop_subsets

def is_valid_set(item_set, prev_level_sets):
    single_drop_subsets = get_single_drop_subsets(item_set)
    
    for single_drop_set in single_drop_subsets:
        if single_drop_set not in prev_level_sets:
            return False
    return True


# **prunning** functie care executa pasul "pruning" asupra unor candidate sets dupa ce pasul de self-join s-a efectuat. Gaseste toate subset-urile unui set si verificat daca acel subset a fost prezent in nivelul anterior sau nu. Daca un subset nu a fost prezent in nivelul anterior atunci setul curent nu este valid si nu trebuie folosit --> "prune set".

def pruning(frequent_item_sets_per_level, level, candidate_set):
    post_pruning_set = list()
    if len(candidate_set) == 0:
        return post_pruning_set
    
    prev_level_sets = list()
    for item_set, _ in frequent_item_sets_per_level[level - 1]:
        prev_level_sets.append(item_set)
        
    for item_set in candidate_set:
        if is_valid_set(item_set, prev_level_sets):
            post_pruning_set.append(item_set)
            
    return post_pruning_set


# ## Apriori Algorithm

from collections import defaultdict

def apriori(min_support):
    frequent_item_sets_per_level = defaultdict(list)
    print("level : 1", end = " ")
    
    for item in range(1, len(item_list) + 1):
        support = get_support(transactions, {item})
        if support >= min_support:
            frequent_item_sets_per_level[1].append(({item}, support))
        
    for level in range(2, len(item_list) + 1):
        print(level, end = " ")
        current_level_candidates = self_join(frequent_item_sets_per_level, level)

        post_pruning_candidates = pruning(frequent_item_sets_per_level, level, current_level_candidates)
        if len(post_pruning_candidates) == 0:
            break

        for item_set in post_pruning_candidates:
            support = get_support(transactions, item_set)
            if support >= min_support:
                frequent_item_sets_per_level[level].append((item_set, support))
                
    return frequent_item_sets_per_level


# ### Specificam valoarea **minimum support** 

min_support = 0.005
frequent_item_sets_per_level = apriori(min_support)


# Debug print statement pentru a verifica numarul de frequent itemset pe fiecare nivel.

for level in frequent_item_sets_per_level:
    print(len(frequent_item_sets_per_level[level]))


# Printam frequent itemsets per nivel.

for level in frequent_item_sets_per_level:
    print("Frequent items sets on level: ", level)
    print(frequent_item_sets_per_level[level])
    print()



# ## Generarea regulilor de asociere

# Prepare input : Cream un dictionar al fiecarui frequent itemset si valoarea support a sa

# %%
item_support_dict = dict()
item_list = list()

key_list = list(item_dict.keys())
val_list = list(item_dict.values())

for level in frequent_item_sets_per_level:
    for set_support_pair in frequent_item_sets_per_level[level]:
        for i in set_support_pair[0]:
            item_list.append(key_list[val_list.index(i)])
        item_support_dict[frozenset(item_list)] = set_support_pair[1]
        item_list = list()


# Debug statement to check the values in the dictionary created.
# item_support_dict


# **find_subset** gaseste toate subset-urile unui set.

def find_subset(item, item_length):
    combs = []
    for i in range(1, item_length + 1):
        combs.append(list(combinations(item, i)))
        
    subsets = []
    for comb in combs:
        for elt in comb:
            subsets.append(elt)
            
    return subsets


# **association_rules** genereaza regulile de asociere pe baza valorii *minimum confidence* si a dictionarului cu itemset-uri si valorea lor support. 
# Pentru fiecare itemset gasim subset-urile sale. Consideram fiecare subset A, si calculam B=itemset - A.  Daca B nu este empty, calculam valoarea confidence si daca este mai mare sau egala decat min_confidence atunci regula A -> este adaugata listei de reguli.


def association_rules(min_confidence, support_dict):
    rules = list()
    for item, support in support_dict.items():
        item_length = len(item)
       
        if item_length > 1:
            subsets = find_subset(item, item_length)
           
            for A in subsets:
                B = item.difference(A)
               
                if B:
                    A = frozenset(A)
                    
                    AB = A | B
                    
                    confidence = support_dict[AB] / support_dict[A]
                    if confidence >= min_confidence:
                        rules.append((A, B, confidence))
    
    return rules


#  Specificam valorile pentru minimum confidence aici

association_rules = association_rules(min_confidence = 0.6, support_dict = item_support_dict)



# Print la output intr-un format mai prietenos

print("Number of rules: ", len(association_rules), "\n")

for rule in association_rules:
    print('{0} -> {1} <confidence: {2}>'.format(set(rule[0]), set(rule[1]), rule[2]))

