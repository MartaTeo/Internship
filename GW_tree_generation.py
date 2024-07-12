# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 11:23:05 2024

@author: HP
"""

import random



#first initialise the offspring distribution (zeta): p_0, p_1, ... p_k
def zeta_unspecified(randweight=10, tolerance=10**(-6)):
    T = 1
    p = []
    while T > 0:
        newp = random.random()/randweight
        if T >= newp:
            T = T - newp
            p.append(newp)
        else:
            p.append(T)
            T = 0
    assert(-tolerance <= sum(p) - 1 <= tolerance)
    return p


# a zeta where the expected number of children is 1, this is called a critical GW process
zeta_critical_example1 = [0.4, 0.3, 0.2, 0.1]
zeta_critical_example2 = [0.3, 0.4, 0.3]

##########################################################################################

#next we use the previous code to make a zeta and generate a GW tree of specified size n
def generate_GW(zeta, n):
    kidlist = [i for i in range(len(zeta))]
    edges = set()
    parent=0
    upper=1
    while upper <= n:
        [nchild] = random.choices(kidlist,weights=zeta, k=1)
        #print(nchild)
        for _ in range(nchild):
            edges.add((parent, upper))
            upper += 1
            #print(edges)
            if upper >= n+1:
                return (n, edges)
        if parent+1 >= upper:
            return (n, edges)
        parent += 1










