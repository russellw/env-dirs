import argparse
import glob
import os
import re

parser = argparse.ArgumentParser()
parser.add_argument("filenames", nargs="*")
args = parser.parse_args()
filenames = args.filenames

direx = re.compile(r"^[C-Zc-z]:\\.+")

rs = []
for k, v in os.environ.items():
    if v.startswith(";"):
        v = v[1:]
    if not direx.match(v):
        continue
    v = v.split(";")
    r = [k]
    for d in v:
        if not direx.match(d):
            continue
        if not filenames:
            r.append(d)
            continue
        for filename in filenames:
            if list(glob.glob(d + "/" + filename)):
                r.append(d)
                break
    if len(r) > 1:
        rs.append(r)

for r in rs:
    print(f"{r[0]:40} {r[1]}")
    for d in r[2:]:
        print(f"{'':40} {d}")
