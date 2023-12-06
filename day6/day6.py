import re
import pathlib

lines = pathlib.Path("data.txt").read_text().split("\n")

def day1():
  times_str = lines[0].replace("Time:", "")
  times = [int(s) for s in times_str.split()]

  distance_str = lines[1].replace("Distance:", "")
  distances = [int(s) for s in distance_str.split()]

  total = 1
  for time, record in zip(times, distances):
    record_times = 0
    for i in range(1, time):
      time_moving = time - i
      distance = time_moving * i
      if distance > record:
        record_times += 1
    
    total *= record_times
  
  print(total)

def day2():
  times_str = lines[0].replace("Time:", "").replace(" ", "")
  time = int(times_str)

  distance_str = lines[1].replace("Distance:", "").replace(" ", "")
  record = int(distance_str)

  record_times = 0
  for i in range(1, time):
    time_moving = time - i
    distance = time_moving * i
    if distance > record:
      record_times += 1
  
  print(record_times)


day2()