from collections import deque

dec = deque(["ab", "bc", "dm", "tm"])
while dec:
    el = dec.popleft()
    if el == "bc":
        break
print(dec)