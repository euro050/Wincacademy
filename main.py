# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def greet(name, greeting = 'Hello, name!'):
    greeting = greeting.replace('name', name)
    return print(greeting)
    

greet('Bob')
greet('Mark')

def force(mass, body = 'earth'):
    gravitylist = dict([
        ('sun', 274),
        ('jupiter',  24.9),
        ('neptune',  11.2),
        ('saturn',  10.4),
        ('earth', 9.8),
        ('uranus', 8.9),
        ('venus', 8.9),
        ('mars', 3.7),
        ('mercury', 3.7),
        ('moon', 1.6),
        ('pluto', 0.6)
    ])
    print(mass * gravitylist[body])


force(18.2)



#def pull(mass1, mass2, distance):
    
G = 6.674 * (10**-11)

def pull(m1, m2, d):
    print(G * (m1 * m2) / (d**2))
    return


pull(100,200,0.5)








