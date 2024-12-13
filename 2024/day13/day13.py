import pathlib
import re

"""
px - x coordinate of prize 
py - y coordinate of prize
ax - a button movement on x
ay - a button movement on y
bx - b button movement on x
by - b button movement on y
ca - presses of a button
cb - presses of b button

start with these two equations:
px = ca*ax + cb*bx
py = ca*ay + cb*by

solve for ca:
px - cb*bx = ca * ax
ca = (px - cb*bx) / ax

solve for cb: 
py = ((px - cb*bx) / ax) * ay + cb*by
px * ax = px*ay - cb*bx*ay + cb*by*ax
cb*bx*ay - cb*by*ax = px*ay - py*ax
cb = (px*ay - py*ax) / (bx*ay - by*ax)

if cb and ca are both integers then we have a working solution
"""

machine_strs = pathlib.Path("data.txt").read_text().split("\n\n")
machines = []
for machine_str in machine_strs:
  matches = re.findall(r"\d+", machine_str)
  machines.append([int(i) for i in matches])

def get_cost(ax, ay, bx, by, px, py, offset=0):
  px += offset
  py += offset
  cb = (px*ay - py*ax) / (bx*ay - by*ax)
  ca = (px - cb*bx) / ax
  if ca.is_integer() and cb.is_integer():
    return int(ca*3) + int(cb)
  return 0

tokens_p1 = sum([get_cost(*m) for m in machines])
tokens_p2 = sum([get_cost(*m, offset=10000000000000) for m in machines])

print(tokens_p1, tokens_p2)