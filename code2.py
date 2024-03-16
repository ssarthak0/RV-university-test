from fractions import Fraction

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def simplify_fraction(numerator, denominator):
    divisor = gcd(numerator, denominator)
    return numerator // divisor, denominator // divisor

def sum_egyptian_fractions(unit_fractions):
    sum_fraction = Fraction(0)
    for fraction in unit_fractions:
        sum_fraction += Fraction(1, fraction)
    return sum_fraction

def main():
    num_instances = int(input())
    for _ in range(num_instances):
        num_fractions = int(input())
        fractions_list = list(map(int, input().split()))
        sum_fraction = sum_egyptian_fractions(fractions_list)
        simplified_fraction = simplify_fraction(sum_fraction.numerator, sum_fraction.denominator)
        print(' + '.join([f'1/{fraction}' for fraction in fractions_list]), end=' = ')
        print(f'{simplified_fraction[0]}/{simplified_fraction[1]}')

if __name__ == "__main__":
    main()
