if __name__ == '__main__':
    ref_dict = {"Tetrahedron": 4, "Cube": 6, "Octahedron": 8, "Dodecahedron": 12, "Icosahedron": 20}
    n = int(input())
    count = 0
    for _ in range(n):
        count += ref_dict[input()]

    print(count)