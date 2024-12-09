import pathlib
import shutil
import argparse
import json

import httpx

input_url = "https://adventofcode.com/{year}/day/{day}/input"
base_dir = pathlib.Path(__file__).resolve().parent

def get_cookies(): 
  config = json.loads((base_dir / "config.json").read_text())
  session = config["cookie"].split("session=")[-1]
  return {"session": session}

def setup_dir(year, day):
  puzzle_dir = base_dir / year / f"day{day}"
  puzzle_dir.mkdir(parents=True, exist_ok=True)
  
  cookies = get_cookies()
  url = input_url.format(year=year, day=day)
  response = httpx.get(url, cookies=cookies)
  response.raise_for_status()
  data = response.text.strip()

  (puzzle_dir / "data.txt").write_text(data)
  (puzzle_dir / "data_test.txt").write_text("")
  shutil.copy(base_dir / "template.py", puzzle_dir / f"day{day}.py")

if __name__ == "__main__":
  parser = argparse.ArgumentParser(
    prog="aoctool",
    description="Downloads puzzle inputs automatically from the Advent of Code website."
  )
  parser.add_argument("year")
  parser.add_argument("day")
  args = parser.parse_args()

  setup_dir(args.year, args.day)
