# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# Part 1
scorer_name_0 = 'Marco van Basten'
goal_0 = 32
scorer_name_1 = 'Ruud Gullit'
goal_1 = 54


scorers = (str(scorer_name_0) + ' ' + str(goal_0) + 'nd')+', '+ (str(scorer_name_1) +' ' + str(goal_1) + 'th')
print(scorers)

report =(f'{scorer_name_0} scored in the {goal_0}nd minute \n{scorer_name_1} scored in the {goal_1}th minute')
print(report)

# Part 2
player = 'Ruud Gullit'

first_name = player[0:player.find(' ')]
last_name_len = len(player[player.find(' ')+1 :])

name_short = (player[:1]) + ('. ') + (player[player.find(' ')+1:])

chant = (first_name + '!') * len(first_name)
print(chant)

good_chant = chant[-1:] != ' '
print(good_chant)
