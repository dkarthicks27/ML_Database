def solve():
    m, n = list(map(int, input().split()))
    inp_str = input()
    for iteration in range(n):
        render_str = ''
        for i in range(len(inp_str)):
            if i == 0:
                if int(inp_str[i+1]) == 1 or int(inp_str[i]) == 1:
                    render_str += '1'
                else:
                    render_str += '0'

            elif i == len(inp_str) - 1:
                if int(inp_str[i - 1]) == 1 or int(inp_str[i]) == 1:
                    render_str += '1'
                else:
                    render_str += '0'

            else:
                if int(inp_str[i-1]) + int(inp_str[i+1]) == 1 or int(inp_str[i]) == 1:
                    render_str += '1'
                else:
                    render_str += '0'
        inp_str = render_str

    print(inp_str)




if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()
