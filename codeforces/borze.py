if __name__ == '__main__':
    code = input()
    x = code.replace('--', '2')
    y = x.replace('-.', '1')
    z = y.replace('.', '0')
    print(z)
