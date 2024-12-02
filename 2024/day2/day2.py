import pathlib

lines = pathlib.Path("data.txt").read_text().split("\n")
lines_split = [line.split() for line in lines]
reports = [[int(r) for r in report] for report in lines_split]

def is_safe(report):
  diffs = [curr - prev for prev, curr in zip(report, report[1:])]
  diffs_abs = [abs(d) for d in diffs]
  same_sign = all(d >= 0 for d in diffs) or all(d < 0 for d in diffs)
  if not same_sign:
    return False
  if min(diffs_abs) < 1:
    return False
  if max(diffs_abs) > 3:
    return False
  return True

safe = sum((is_safe(report) for report in reports))

new_safe = 0
for report in reports:
  maybe_safe = is_safe(report)
  for i in range(len(report)):
    new_report = report[:]
    del new_report[i]
    maybe_safe += is_safe(new_report)
  new_safe += maybe_safe > 0

print(safe, new_safe)