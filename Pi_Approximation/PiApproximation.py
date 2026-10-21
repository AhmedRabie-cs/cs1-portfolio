#PiApproximation.py


"""we are going to approximate pi using the infinite sum pi = 4 - 4/3 + 4/5 -4/7 + ..."""

error = float(input("Input error tolerance:"))

print("Number of Terms \t\tPi Approximation")

terms = 1
pi_approx = 0
PI = 3.14159265358979

while abs(PI - pi_approx) > error:
    pi_end = 4*(-1)**(terms + 1)/ (2* terms -1)
    pi_approx += pi_end
    print(terms, "\t\t\t","\t\t","  ", round(pi_approx,6))
    terms += 1

print(f"After {terms-1} terms, pi is approximately {round(pi_approx,6)}.")
print(f"Our error is {round(abs(PI - pi_approx),6)} which is less than or equal to {round(error,6)} ")
