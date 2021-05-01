num_of_works = int(input())
times = [0 for i in range(num_of_works + 1)]
graph = {i: [] for i in range(1, num_of_works + 1)}

for work in range(1, num_of_works + 1):
    work_info = list(map(int, input().split()))
    times[work] = work_info[0]

    if work_info[1] == 0:
        continue

    for prework in work_info[2:]:
        graph[work].append(prework)

for work in range(1, num_of_works + 1):
    time = 0
    for prework in graph[work]:
        time = max(time, times[prework])
    
    times[work] += time

print(max(times))