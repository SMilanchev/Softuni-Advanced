from collections import deque


def solve():
    green_light_duration = int(input())
    free_window_duration = int(input())
    cars_queue = deque()
    passed_cars = []
    is_crash = False

    command = input()
    while command != "END":
        if command == "green":
            green_light = green_light_duration
            free_light = free_window_duration
            while cars_queue:
                current_car = cars_queue.popleft()
                length_car = len(current_car)
                green_light -= length_car
                if green_light > 0:
                    passed_cars.append(current_car)
                    continue
                if green_light + free_light >= 0:
                    passed_cars.append(current_car)
                    break
                else:
                    crash_point = green_light + free_light
                    print("A crash happened!")
                    print(f"{current_car} was hit at {current_car[crash_point]}.")
                    is_crash = True
        else:
            cars_queue.append(command)
        if is_crash:
            break
        command = input()
    if not is_crash:
        print("Everyone is safe.")
        print(f"{len(passed_cars)} total cars passed the crossroads.")


solve()