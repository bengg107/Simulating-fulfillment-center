#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#INMAS Worksop4: Group A: Simulating fulfillment center
# @c: Ben, Issac, Sultan, Vlassis, Yantao
# for 1<=i<=M, the i-th order has length n_i = sum_j n_ij where n_ij means the number of product j in i-th order (1<=j<=N).
# we consider the following setup: (for any i) n_ij ~ Geom(1/(1+|w_j|))-1 where w_j ~ N(0,1). Here we assume n_ij are independent in i

import numpy as np
import random

def generate_orderbook(N, M):
    omega = np.random.normal(0, 1, N)
    omega = abs(omega)
    nij   = np.random.geometric(p=1/(1+omega) ,size=(M,N)) -1

    orderbook = []
    for i in range(M): 
        orderbook.append(np.concatenate([[j]*nij[i,j] for j in range(N)]))
    
    return orderbook


def position_function(N):
    intN = int(N/4)
    a1 =  [ (i+1 , 0) for i in range(intN)]  
    a2 = [ (intN, i+1) for i in range(intN)] 
    a3 = [ (0, i+1) for i in range(intN)]
    a4 = [ (i+1, intN) for i in range(intN-1)]
    a = [*a1, *a2, *a3, *a4]
    return a

def position_random_generator(N):
    positions = position_function(N)
    random.shuffle(positions)
    return positions
