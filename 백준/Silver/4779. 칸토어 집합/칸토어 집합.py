import sys

Ns = []
for line in sys.stdin.read().splitlines():
    line = line.strip()
    if line == "":
        continue
    Ns.append(int(line))
    
if not Ns:
    sys.exit(0)
    
maxN = max(Ns)

levels = ["-"]
for _ in range(maxN):
    prev = levels[-1]
    levels.append(prev + (" " * len(prev)) + prev)
    
out_lines = [levels[n] for n in Ns]
sys.stdout.write("\n".join(out_lines))
    