from collections import deque


def solve(petrol_pumps):
    pumps = deque()
    for _ in range(petrol_pumps):
        pump = [int(x) for x in input().split()]
        pumps.append(pump)

    fuel = 0
    for i in range(petrol_pumps):
        current = pumps.popleft()
        while pumps:
            fuel += current[0]
            if fuel >= current[1]:

                current = pumps.popleft()
                fuel -= current[1]
            else:
                pumps.append(current)
                break
        fuel = 0
        print(pumps)
        if not pumps:
            print(i)
            break

        pumps.append(current)


solve(int(input()))
