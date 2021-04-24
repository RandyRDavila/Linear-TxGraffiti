from pyfiglet import figlet_format
from halo import Halo
import time
from datetime import datetime, timedelta
import pandas as pd
from functions.make_conjectures import make_conjectures



__version__ = 'Linear-TxGraffiti 0.0.1'

invariants = ['domination_number',
              'total_domination_number',
              'connected_domination_number',
              'independence_number',
              'zero_forcing_number',
              'diameter',
              'radius',
              'order',
              'independent_domination_number',
              'chromatic_number',
              'matching_number',
              'min_maximal_matching_number',
              'triameter',
              'min_degree',
              'max_degree',
              'clique_number',
              'residue',
              'annihilation_number',
              'vertex_cover_number',
              'girth',
              'algebraic_connectivity',
              'k-slater-index',
              'k_residual_index',
              'randic_index',
              'augmented_randic_index',
              'harmonic_index',
              'atom_bond_connectivity_index',
              'sum_connectivity_index',
              'first_zagreb_index',
              'second_zagreb_index',
              'slater',
              'sub_total_domination_number',
              'CW_disparity',
              'closed_CW_disparity',
              'inverse_disparity',
              'closed_inverse_disparity',
              'average_vertex_disparity',
              'average_closed_vertex_disparity',
              'irregularity',
              '2-residue',
              'average_degree',
              'paired_domination_number',
              'power_domination_number',
              '2-power_domination_number',
              '2-domination_number',
              '2-forcing_number',
              'total_forcing_number',
              ]


valid_invariants = {i : x for i, x in enumerate(invariants)}


properties = [['is_bipartite'], 
              ['is_eulerian'], 
              ['is_planar'], 
              ['is_regular'],
              ['is_cubic'],
              ['is_triangle_free'],
              ['is_claw_free'],
              ['is_at_free'],
              ['is_sub_cubic'],
              ['is_2_edge_connected'],
              ['is_regular', 'is_not_K_n'],
              ['is_cubic', 'is_not_K_n'],
              ['is_sub_cubic', 'is_not_K_n'],
              ['is_cubic', 'is_claw_free'],
              ['is_cubic', 'is_triangle_free'],
              ['is_regular', 'is_claw_free'],
             ]

graph_properties = {i : [x] for i, x in enumerate(properties)}
graph_properties['all'] = properties


'''
valid_invariants = {1: 'domination_number',
                    2: 'total_domination_number',
                    3: 'connected_domination_number',
                    4: 'independence_number',
                    5: 'independent_domination_number',
                    6: 'zero_forcing_number',
                    7: 'power_domination_number',
                    8: 'matching_number', 
                    9: 'min_maximal_matching_number',
                    10: 'chromatic_number',
                    11: 'clique_number',
                    12: 'triameter', 
                    13: 'atom_bond_connectivity_index'}



graph_properties = {1 : 'is_connected',
                    2 : 'is_regular',
                    3 : 'is_cubic',
                    4 : 'is_planar',
                    5 : 'is_not_K_n',
                    6 : 'is_triangle_free',
                    7 : 'is_eulerian',
                    8 : 'is_distance_regular',
                    9 : 'is_strongly_regular',
                    10: 'is_bipartite'
                    }               
'''


data = pd.read_csv('data/small_graphs_new.csv')

def main():
    print(figlet_format('Linear TxGRAFFITI', font='slant'))
    print('Version ' + __version__)
    print('Copyright ' + u'\u00a9' + ' 2019 Randy Davila')
    print()

    print('The invariants you may conjecture against are: ')
    print('-----------------------------------------------')
    print()
    i = 1


    for x in valid_invariants:
        print(f'{x}. {valid_invariants[x]}')
        print()
    print('-----------------------------------------------')
    print()
    target = valid_invariants[int(input('Invariant: '))]
    print()



    conjectures = make_conjectures(data, [target], invariants, properties)
    for i, c in enumerate(conjectures[:100]):
        print(f'Conjecture {i+1}. {c} (touch = {c.touch})')
        print('')
       
              


if __name__ == '__main__':
    main()
