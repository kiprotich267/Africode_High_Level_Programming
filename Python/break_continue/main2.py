import time

counter = 0
while counter < 20:
    counter += 1
    if counter == 7:
        print("skipping 7")
        continue
    if counter == 19:
        break
    print(counter)
       