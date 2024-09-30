from pathlib import Path
import random

txt_file = open("new_every_day.txt", "r+", encoding="utf8")
data = txt_file.readlines()

random_num = random.randint(0, len(data))

if random_num >= len(data):
    print("You have done everything from list. Congratulations!")
    exit()

thing_to_do = data[random_num]
print(thing_to_do)
txt_file.seek(0)
for line in data:
    if thing_to_do not in line:
        txt_file.write(line)
txt_file.truncate()

f = open("done_new_every_day.txt", "a")
f.write(thing_to_do + "\n")
f.close()

txt_file.close()

