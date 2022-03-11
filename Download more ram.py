import sys
sys.stdin.readline

def inp_arr():
    return list(map(int, input().split()))
def inp_int():
    return int(input())
test = inp_int()
for i in range(test):
    visited = set()
    line1 = inp_arr()
    n = line1[0]
    cur_ram = line1[1]
    softwares = inp_arr()
    permanent_ram = inp_arr()
    ptr = 0
    while ptr < n:
        for s_ware_idx in range(n):
            if s_ware_idx not in visited and softwares[s_ware_idx] <= cur_ram:
                cur_ram += permanent_ram[s_ware_idx]
                visited.add(s_ware_idx)
        ptr += 1
    print(cur_ram)
