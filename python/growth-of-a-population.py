# Growth of a population.
# this passed all the tests first attempt i suppose it could be better optimised 

def nb_year(p0, percent, aug, p):
    percent = percent / 100.0
    years = 0
    while p0 < p:
        p0 = p0 + (p0 * percent) + aug
        years = years + 1
    return years

print(nb_year(1500, 5, 100, 5000))
print(nb_year(1500000, 2.5, 10000, 2000000))
print(nb_year(1500000, 0.25, 1000, 2000000))