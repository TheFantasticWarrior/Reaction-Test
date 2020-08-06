import time, random

times = [0, 0, 0, 0, 0]
for i in range(5):
    print("\u001b[41;1m" + "\n" * 62 + "\u001b[0m")
    time.sleep(random.uniform(3.5, 5))
    print(u"\u001b[42m" + "\n" * 62 + "\u001b[0m")
    start = time.time()
    input("")
    end = time.time()
    times[i] = (end - start) * 1000
    if times[i] < 0.5:
        print("Cheat detected")
        quit()
    print(round((times[i])))

    input("Press enter to continue")
a = round(sum(times) / len(times))
print("Average: {} ms, {} frames".format(a, round(a*3/50)))
print("Lowest: {} highest: {}".format(round(min(times)), round(max(times))))
