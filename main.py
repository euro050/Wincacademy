# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#Deel 1
scorer_1 = 'Ruud Gullit'
scorer_2 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = (scorer_1) + ' ' + str(goal_0) + ', ' + (scorer_2) + ' ' + str(goal_1)
print(scorers)

report = (f'{scorer_1} scored in the {goal_0}nd minute\n{scorer_2} scored in the {goal_1}th minute')
print(report)


#Deel 2

player = 'Gerald Vanenburg'
print(player)


spatie = player.find(" ")
print(spatie)

first_name = player[0:spatie]
print(first_name)

first_name_len = len(first_name)
print(first_name_len)

total_len = len(player)
print(total_len)

last_name = player[spatie:total_len]
last_name_len = len(last_name)
print(last_name_len)

name_short = player[0:1] + '.' + last_name
print(name_short)

chant = (first_name + '! ') * first_name_len
chant_len = len(chant)
chant = chant[0:chant_len-1]

print(chant)

good_chant = chant[-1] is ' '
print(good_chant)


