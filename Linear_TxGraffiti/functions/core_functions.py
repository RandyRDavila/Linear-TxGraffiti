
        
import matplotlib.pyplot as plt
import numpy as np



def get_data_numpy_arrays(data_set, invar1, invar2, properties = None):
    
    if properties == None:
        X = np.array(data_set[invar2])
        Y = np.array(data_set[invar1])
        return X, Y
    
    elif len(properties) == 1:
        data_points = [x for x in zip(data_set[invar2], data_set[invar1], data_set[properties[0]])]
        X = np.array([x[0] for x in data_points if x[2] == True])
        Y = np.array([x[1] for x in data_points if x[2] == True])
        return X, Y
    
    elif len(properties) == 2:
        data_points = [x for x in zip(data_set[invar2], data_set[invar1], data_set[properties[0]], data_set[properties[1]])]
        X = np.array([x[0] for x in data_points if x[2] == True and x[3] == True])
        Y = np.array([x[1] for x in data_points if x[2] == True and x[3] == True])
        return X, Y




def conjecture_plot(data_set, conjecture):
        X, Y = get_data_numpy_arrays(data_set, 
                                     conjecture.target, 
                                     conjecture.other, 
                                     properties = conjecture.hypothesis_properties)
        plt.scatter(X, Y, color = 'blue')
        plt.plot(X, X*conjecture.m + conjecture.b, color = 'red')
        plt.xlabel(conjecture.other)
        plt.ylabel(conjecture.target)
        plt.title(f'{conjecture.hypothesis_properties}')
        


   

def find_hypothesis_graph_names(data_set, conjecture):
    if conjecture.hypothesis_properties == None:
        return set([x for x in data_set['name']])
    
    elif len(conjecture.hypothesis_properties) == 1:
        return set([x[1] for x in zip(data_set[conjecture.hypothesis_properties[0]], data_set['name'])
                if x[0] == True])
    
    else:
        return set([x[2] for x in zip(data_set[conjecture.hypothesis_properties[0]],
                                           data_set[conjecture.hypothesis_properties[1]], 
                                           data_set['name']) 
                                            if x[0] == True and x[1] == True])
    




def find_sharp_graph_names(data_set, conjecture):
    data_points = [x for x in zip(data_set[conjecture.target], data_set[conjecture.other], data_set['name'])]
    names = []
    for x in data_points:
        if x[0] == conjecture.m*x[1] + conjecture.b:
            names.append(x[2])
            
    return names