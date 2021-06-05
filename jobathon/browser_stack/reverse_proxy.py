import re


class InternalMachine:
    def __init__(self, ip):
        self.ip = ip
        self.busy = 0
        self.request = []


class ReverseProxy:
    def __init__(self, machines, loc):
        self.loc = loc
        self.machines = machines
        self.curr = 0



if __name__ == '__main__':
    number_of_machines = int(input())
    machine_order = input().split()
    machine_ref = {i: InternalMachine(i) for i in machine_order}


    no_of_reverse_proxy = int(input())
    proxy_reference = dict()

    for i in range(no_of_reverse_proxy):
        url = input()
        _ = input()
        machine = input().split()
        proxy_reference[url] = ReverseProxy(machines=machine, loc=url)

    queries = int(input())

    for i in range(queries):
        query = input()
        url, request = query.split(r'/')[0:2]
        rp = proxy_reference[url]
        if 'machine_down' not in request and 'machine_up' not in request:
            if rp is not None:
                if rp.curr < len(rp.machines):
                    available_machine = machine_ref[rp.machines[rp.curr]]
                    available_machine.request.append(query)
                else:
                    rp.curr = 0
                    available_machine = machine_ref[rp.machines[rp.curr]]
                    available_machine.request.append(query)
                if rp.curr + 1 < len(rp.machines):
                    rp.curr += 1
                else:
                    rp.curr = 0
        else:
            if 'machine_down' in request:
                x = query.split(r'=')[1]
                rp.machines.remove(x)
            else:
                x = query.split(r'=')[1]
                rp.machines.append(x)
                rp.curr += 1


    for i in machine_order:
        print(i)
        for req in machine_ref[i].request:
            print(req)


