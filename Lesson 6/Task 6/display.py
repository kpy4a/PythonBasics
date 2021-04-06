import sales
import sys

if len(sys.argv) == 3:
    from_number = int(sys.argv[1]) - 1
    to_number = int(sys.argv[2])
elif len(sys.argv) == 2:
    from_number = int(sys.argv[1]) - 1
    to_number = None
else:
    from_number = 0
    to_number = None

for i, summary in sales.get_summary_for_show(from_number, to_number):
    print(i, summary)