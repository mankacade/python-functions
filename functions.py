####Function is a block of code that runs only when called

def adding(num1, num2):
    x = num1+num2
    print(x)

adding(2,4)


#####Multiplication

def multiplication():
    num1 =12
    num2 =34
    sum = num2*num1
    print(sum)

multiplication()

##arguments
def courses(*args):
    for subject in args:
        print(subject)
courses('IT', 'Nutririon', 'Math')

def courses(*args):
    for subject in args:
        return subject
        print(courses('IT', 'Nutririon', 'Math'))


##keyword arguments

def cars(**kwargs):
    for key, value in kwargs.items():
        print("{}:{} ". format(key,value))

cars( car1='Subaru\n', car2='Bentley\n', car3='jeep')


##Default parameter value - used when we call the fn without an argument

def shoes(shoe_type = 'Airmax'): ##Airmax is set to be the default argument
    print('\nMy shoe type is ' + shoe_type )

shoes() ##this will print 'My shoetype is Airmax since it is the default parameter'
shoes('fila')
shoes('puma')



###passing a list of arguments

def  muFunction (devices):
    for x in devices:
        print(x)

input_devices = ['Keyboard', 'touchscreen', 'mouse']

muFunction(input_devices)