def find_intersection(ranges_count):
    longest_intersection = []

    for _ in range(ranges_count):
        string = input()
        (a, b) = string.split("-")
        (first_start, first_end) = map(int, a.split(","))
        (second_start, second_end) = map(int, b.split(","))
        first_list = set([x for x in range(first_start, first_end + 1)])
        second_list = set([y for y in range(second_start, second_end + 1)])
        intersection = list(first_list.intersection(second_list))
        if len(intersection) > len(longest_intersection):
            longest_intersection = intersection

    return longest_intersection


def print_result(result):
    print(f"Longest intersection is {result} with length {len(result)}")


print_result(find_intersection(int(input())))

