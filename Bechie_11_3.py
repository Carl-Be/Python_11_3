"""
Carl Bechie
CIS 185
ex 11.3
"""

def expo(base, exponent):
    # Write your function here
    answer = base #set the answer to the base first 
   # if the expoinet is 0 or 1 no need to do the loop 
    if exponent == 0:
        return 0
    if exponent == 1:
        return base  
#----------->Big O = O(n) <------------------
    for i in range(1, exponent):
        answer *= base 

    return answer

def main():
    """Tests with powers of 2."""
    print("\n")

    for exponent in range (10):
        print("Exponent: %d Answer: %d \n" % (exponent, expo(2, exponent)))

if __name__ == "__main__":
    main()