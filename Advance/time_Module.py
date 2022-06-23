import time

s = time.time()
for i in range(100):
    continue
n = time.time()
print(f"Total time : {n-s}")


time.sleep(5)
print("After sleeping for 5 seconds")

localtime = time.asctime(time.localtime(time.time())) #.        It returns local time
print(localtime)
