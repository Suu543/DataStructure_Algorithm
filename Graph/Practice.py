
# # 1. 시간
# # 2. 선행관계 작업 수
# # 3. 선행관계 작업 번호

# N = int(input())
# # 각 작업이 걸리는 시간을 담는 리스트
# times = [0 for i in range(N + 1)]
# # 작업번호 :[선행되어야하는 작업]
# # graph {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
# graph = {i: [] for i in range(1, N + 1)}

# for work in range(1, N + 1):
#     # 작업 정보 입력받기
#     work_info = list(map(int, input().split()))
#     # 작업시간을 기록
#     times[work] = work_info[0]

#     # 선행되어야하는 작업이 없으면 다시 위로 돌아간다.
#     if work_info[1] == 0:
#         continue

#     # 선행되야하는 작업이 있다면
#     for prework in work_info[2:]:
#         # 그래프에 넣어준다.
#         graph[work].append(prework)

# for work in range(1, N + 1):
#     print("graph", graph)
#     print("times", times)
#     time = 0
#     for prework in graph[work]:  # 선행작업을 돌면서
#         # 작업들 중 가장 빠른 시간을 찾기
#         time = max(time, times[prework])
#         print(f"time {time}")
#     times[work] += time  # 그 시간을 현재 작업시간에 더해준다.

# # 이런식으로 전체 리스트를 돌면
# # 가장 큰 값이 전체 리스트를 돌았을 때 걸린 시간
# print(max(times))

from collections import defaultdict


class Graph:
    def __init__(self, num_of_works):
        self.num_of_works = num_of_works
        self.times = [0 for i in range(num_of_works + 1)]
        self.graph = defaultdict(list)

    def getInput(self):
        for work in range(1, self.num_of_works + 1):
            work_info = list(map(int, input().split()))
            self.times[work] = work_info[0]

            if work_info[1] == 0:
                continue

            for prework in work_info[2:]:
                self.graph[work].append(prework)

    def calculateTime(self):
        for work in range(1, self.num_of_works + 1):
            time = 0
            for prework in self.graph[work]:
                time = max(time, self.times[prework])
            self.times[work] += time

        return max(self.times)

    def run(self):
        self.getInput()
        result = self.calculateTime()
        print(result)
        return


num_of_works = int(input())
a = Graph(num_of_works)
a.run()
