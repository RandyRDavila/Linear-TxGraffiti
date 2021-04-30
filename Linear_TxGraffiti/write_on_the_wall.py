from pyfiglet import figlet_format
from halo import Halo
import time
from datetime import datetime, timedelta
import pandas as pd
from functions.make_conjectures import make_conjectures
#from functions.heuristics import Dalmation



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
              ['is_tree'],
              ['is_chordal'],
              ['is_semieulerian'],
              ['is_bull_free'],
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
#graph_properties['all'] = properties



data = pd.read_csv('data/order_1_to_6_plus.csv')

def main():
    print(figlet_format('Linear TxGRAFFITI', font='slant'))
    print('Version ' + __version__)
    print('Copyright ' + u'\u00a9' + ' 2019 Randy Davila')
    print()

    print('The invariants you may conjecture against are: ')
    print('-----------------------------------------------')
    print()


    for x in valid_invariants:
        print(f'{x}. {valid_invariants[x]}')
        print()
    print('-----------------------------------------------')
    print()
    target = valid_invariants[int(input('Invariant: '))]
    print()

    conjectures = make_conjectures(data, [target], invariants, properties)


    print(figlet_format('Linear TxGRAFFITI', font='slant'))
    print('Version ' + __version__)
    print('Copyright ' + u'\u00a9' + ' 2021 Randy Davila')
    print()
    print(f'Please limit the number of conjectures presented')
    print()
    limit = int(input(f'Enter a integer between {0} and {len(conjectures)}: '))
    print('-----------------------------------------------')
    print()

    #conjectures = Dalmation(conjectures)
    print('')
    print(figlet_format('Linear TxGRAFFITI', font='slant'))
    print('Version ' + __version__)
    print('Copyright ' + u'\u00a9' + ' 2021 Randy Davila')
    print('')

    print(f'TxGraffiti Conjectures: {target} ')
    print('-----------------------------------------------')
    print('')
    for i, c in enumerate(conjectures[:limit]):
        print(f'Conjecture {i+1}. {c} (touch = {c.touch})')
        print('')
       
              


if __name__ == '__main__':
    main()
