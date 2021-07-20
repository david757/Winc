# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

#Part 1: Greet Template
def greet(name, greeting='Hello, '):
    print(f'{greeting}{name}!' )

greet('David')

#part 2: Force
sun	    = 274
jupiter	= round(4.92, 1)
neptune	= round(11.15, 1)
saturn	= round(10.44, 1)
earth	= round(9.798, 1)
uranus	= round(8.87, 1)
venus	= round(8.87, 1)
mars	= round(3.71, 1)
mercury	= round(3.70, 1)
moon	= round(1.62, 1)
pluto	= round(0.58, 1)



def force(mass,  body=earth):
    force = mass * body
    return print(force)

force(1)

#Part 3: Gravity
def pull(m1, m2, d):
    pull = (6.674*10**-11) * ((m1*m2)/d**2)
    return print(pull)

pull(0.1, 5.9*10**24, 6.3*10**6)
