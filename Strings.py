# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line


scorer_name_1 = 'Marco van Basten'
goal_1 = '32th'
scorer_name_2 = 'Ruud Gullit'
goal_2 = '54th'


scorers = ( scorer_name_1 + goal_1 ), ( scorer_name_2 + goal_2 )

report =(f'{scorer_name_1} scored in the {goal_1} minute' '\n' f'{scorer_name_2} scored in the {goal_2} minute')

player = 'Ruud Gullit'

first_name = player[0:4]
last_name_len = len(player[5:11])
name_short = (player[:1]) + ('. ') + (player[5:11])

chant = first_name + (last_name_len * '!')

good_chant = chant[12:] != ' '
print(good_chant)
