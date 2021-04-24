
from fractions import Fraction
import numpy as np
from pulp import *
from python_classes.linear_conjecture_class import linear_conjecture
from functions.core_functions import get_data_numpy_arrays, find_sharp_graph_names
from functions.heuristics import Theo


def make_upper_linear_conjecture(data_set, 
                                 target,
                                 other, 
                                 props = None,
                                 w_min = 0.2,
                                 w_max = 4.0,
                                 b_min = -3.0,
                                 b_max = 4.0,
                                 test_index = 1):
    
    conj = linear_conjecture(target,  other, "<=", 0.0, 0.0, properties = props)
    X, Y = get_data_numpy_arrays(data_set, 
                                 target, 
                                 other, 
                                 properties = props)

    X = np.around(X, decimals=2)
    Y = np.around(Y, decimals=2)
    
    # Initialize the LP, say "prob"
    prob = LpProblem("Test_Problem", LpMinimize)
    
    # Initialize the variables for the LP
    w = LpVariable("w", lowBound = w_min)
    b = LpVariable("b", lowBound = b_min)
    
    
    prob += w*X[test_index] + b - Y[test_index]
    #prob += w*np.mean(X) + b - np.mean(Y)
    
    # Define the LP constraints 
    for i in range(len(X)):
        prob += X[i]*w + b >= Y[i]
        prob += X[i]*w - b >= 0

    prob += w <= w_max
    prob += b <= b_max
    
    # Solve the LP
    prob.solve()
    
    conj.m = Fraction(w.varValue).limit_denominator(1000)
    conj.b = Fraction(b.varValue).limit_denominator(1000)
    
    conj.touch = np.sum(Y == conj.m*X + conj.b)
    
    conj.graph_families = find_sharp_graph_names(data_set, conj)
    
    return conj


def make_lower_linear_conjecture(data_set, 
                                 target,
                                 other, 
                                 props = None,
                                 w_min = 0.2,
                                 w_max = 4.0,
                                 b_min = -3.0,
                                 b_max = 4.0, 
                                 ):
    
    conj = linear_conjecture(target,  other, ">=", 0.0, 0.0, properties = props)
    X, Y = get_data_numpy_arrays(data_set, 
                                 target, 
                                 other, 
                                 properties = props)

    X = np.around(X, decimals=2)
    Y = np.around(Y, decimals=2)
    tuples = [x for x in zip(X, Y)]
    # Initialize the LP, say "prob"
    prob = LpProblem("Test_Problem", LpMaximize)
    
    # Initialize the variables for the LP
    w = LpVariable("w", lowBound = w_min)
    b = LpVariable("b", lowBound = b_min)
    
    
    # Initialize the objective function for the LP
    prob += w*np.mean(X) + b - np.mean(Y)
    #prob += lpSum([w*X_unique, + b])

    # Define the LP constraints 
    for i in range(len(X)):
        prob += X[i]*w + b <= Y[i]
        prob += X[i]*w - b >= 0

    prob += w <= w_max
    prob += b <= b_max
    
    # Solve the LP
    prob.solve()
    
    conj.m = Fraction(w.varValue).limit_denominator(1000)
    conj.b = Fraction(b.varValue).limit_denominator(1000)
    
        
    
    conj.touch = np.sum(Y == conj.m*X + conj.b)
    conj.graph_families = find_sharp_graph_names(data_set, conj)
    return conj







def make_conjectures(data_set, targets, invariants, properties):
    conjs = []
    for target in targets:
        invar = [x for x in invariants if x != target]
        for x in invar:
            conjs.append(make_upper_linear_conjecture(data_set, target, x))
            conjs.append(make_lower_linear_conjecture(data_set, target, x))
    
            for p in properties:
                conjs.append(make_upper_linear_conjecture(data_set, target, x, props = p))
                conjs.append(make_lower_linear_conjecture(data_set, target, x, props = p))
            
    return Theo(data_set, conjs)