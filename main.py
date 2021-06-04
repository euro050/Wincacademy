# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
#Deel 1
def greet(name, greeting = 'Hello, <name>!'):
    greeting = greeting.replace('<name>', name)
    return greeting
#Deel 2
def force(mass, body = 'earth'):
    gravitylist = {
        'sun': 274,
        'jupiter':  24.9,
        'neptune':  11.2,
        'saturn':  10.4,
        'earth': 9.8,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6
    }
    antwoord2 = mass * gravitylist[body]
    return antwoord2
#Deel 3    
def pull(m1, m2, d):
    G = 6.674 * (10**-11)
    antwoord3 = (G * (m1 * m2) / (d**2))
    return antwoord3

greet('Mark')
greet('Mark', 'Gegroet, name!')
force(18.2)
pull(100,200,0.5)
