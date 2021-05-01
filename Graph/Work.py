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
        return result


num_of_works = int(input())
work = Graph(num_of_works)
work_result = work.run()
print(work_result)
