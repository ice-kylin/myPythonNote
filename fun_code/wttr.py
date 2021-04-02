import os
import sys

try:
    address = sys.argv[1]
except IndexError:
    address = 'Beijing'

command = f'curl -s wttr.in/{address} | head -n -2'
rst = os.popen(command).read().strip()
print(rst)
