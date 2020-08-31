import math
import cmath

def calculate_roots(coef):

    a_2 = coef[0]
    a_1 = coef[1]
    a_0 = coef[2]
    r_1 = -a_1/(2*a_2) + cmath.sqrt((a_1)**2-4*a_2*a_0)/(2*a_2)
    r_2 = -a_1/(2*a_2) - cmath.sqrt((a_1)**2-4*a_2*a_0)/(2*a_2)

    return r_1, r_2


    

def compute_factorial(n):

    factorial = 1
    number = 1

    for number in range(1,n+1,1):

        factorial = factorial*number
        number = number + 1

    return factorial 

def sum_factorial(n):

    fact = 1
    added = 0
    num = 1

    for num in range(1,n+1,1):

        fact = fact*num
        num = num + 1
        added = added + fact

    return added

    
def f_x(x):

    return math.exp(-3*x) * math.cos(math.pi*x)

def left_riemann(delta_x, lb, ub):

    summ = 0
    x = lb

    while x < ub:

        summ += delta_x * f_x(x)
        x += delta_x

    return summ

def right_riemann(delta_x, lb, ub):

    summ = 0
    x = lb

    while x < ub:

        x += delta_x
        summ += delta_x * f_x(x) 

    return summ
    

def midpoint_riemann(delta_x, lb, ub):

    summ = 0
    x = lb + (delta_x/2)

    while x < ub:

        x += delta_x
        summ += delta_x * f_x(x)

    return summ

    
def trap_riemann(delta_x, lb, ub):

    return(left_riemann(delta_x, lb, ub) + right_riemann(delta_x, lb, ub))
    
def main():

    ##############################################################
    # Part 1
    ##############################################################
    print("Part 1 Results")
    
    coef = [2, 4, 0]
    roots = calculate_roots(coef)
    print("roots 1:")
    print(roots)

    coef = [1, 4, 4]
    roots = calculate_roots(coef)
    print("roots 2:")
    print(roots)
    
    coef = [1, 0, 9]
    roots = calculate_roots(coef)
    print("roots 3:")
    print(roots)

    coef = [2, 8, 26]
    roots = calculate_roots(coef)
    print("roots 4:")
    print(roots)

    ##############################################################
    # Part 2
    ##############################################################
    print("\n")
    print("Part 2 Results")
    
    for n in [4, 10, 16]:
        output_factorial = compute_factorial(n)
        print("computed factorial for n=%i is: %i" %
              (n, output_factorial))

    ##############################################################
    # Part 3
    ##############################################################
    print("\n")
    print("Part 3 Results")
    
    for n in [3, 5, 6]:
        output_summation = sum_factorial(n)
        print("computed factorial summation for n=%i is: %i" %
              (n, output_summation))
        
    ##############################################################
    # Part 4
    ##############################################################
    print("\n")
    print("Part 4 Results")
    
    lb = 0
    ub = 10
    
    print("calculating left Riemann sum")
    for delta_x in [1, 0.1, 0.01, 0.0001]:
        summation = left_riemann(delta_x, lb, ub)
        print("\tdelta_x=%f, summation=%f" % (delta_x, summation))

    print("calculating right Riemann sum")
    for delta_x in [1, 0.1, 0.01, 0.0001]:
        summation = right_riemann(delta_x, lb, ub)
        print("\tdelta_x=%f, summation=%f" % (delta_x, summation))

    print("calculating midpoint Riemann sum")
    for delta_x in [1, 0.1, 0.01, 0.0001]:
        summation = midpoint_riemann(delta_x, lb, ub)
        print("\tdelta_x=%f, summation=%f" % (delta_x, summation))

    print("calculating trapezoid Riemann sum")
    for delta_x in [1, 0.1, 0.01, 0.0001]:
        summation = trap_riemann(delta_x, lb, ub)
        print("\tdelta_x=%f, summation=%f" % (delta_x, summation))

        
if __name__ == "__main__":
    main()