


def Dalmation(conjs):
    new_conjs = [conjs[0]]
    observed_graphs = set(conjs[0].graph_families)
    for i in range(1, len(conjs)):
        if set(conjs[i].graph_families) - observed_graphs != set():
            observed_graphs = observed_graphs.union(set(conjs[i].graph_families))
            new_conjs.append(conjs[i])
    return new_conjs




def Theo(data_set, conjectures):
    C = []
    expressions = set([c.get_expression() for c in conjectures])
    for expr in expressions:
        temp_conjs = [c for c in conjectures if c.get_expression() == expr]
        temp_conjs.sort(reverse = True, key = lambda c : c.touch) 
        temp_conjs = Dalmation(temp_conjs)
        for c in temp_conjs:
            C.append(c)
        #temp_expressions.sort(key = lambda c: len(find_hypothesis_graph_names(data_set, c)))
        #C.append(temp_expressions[-1])

    C.sort(reverse=True, key=lambda x: x.touch)
    
    return C