def quadratic_solver(param1,param2,param3):
    #you could define that as a method without input 
    #x = 1
    #while( x==1 ):
        #print('We will solve the equation a*x^2+b*x+c = 0')
    #    while(True):
    #        try:
    a = param1 #int(input('input the first coefficient a \n'))
    b = param2 #int(input('input b \n'))
    c = param3 #int(input('input c \n'))
    #        except ValueError:
    #            print('Please enter an integer')
    #            continue
    #        break
    delta = b**2-4*a*c
    if (delta > 0):
        x_1 = (-b-delta**(1/2))/(2*a)
        x_2 = (-b+delta**(1/2))/(2*a)
        return([x_1, x_2])
        #print('The solutions are:', x_1, ' ', x_2, '\n')
    if(delta  == 0):
        x_0 = (-b)/(2*a)
        return([x_0])
        #print('The only solution is', x_0)
    if(delta < 0 ):
        return(["no solutions"])
        #print('There are no solutions, delta < 0')
        #x = int(input('press 1 if you want to continue solving equations, \n any other number to stop: '))
    #print('bye')

