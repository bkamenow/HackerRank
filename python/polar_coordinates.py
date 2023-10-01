import cmath

z = complex(input().strip())

r = abs(z)
theta = cmath.phase(z)

print(round(r, 3))
print(round(theta, 3))
