from math import gcd


if __name__ == '__main__':
    # if k = 25, then 25% of the essence is magic potion 75 % is water

    t = int(input())
    for _ in range(t):
        k = int(input())
        print(100//gcd(k, 100))