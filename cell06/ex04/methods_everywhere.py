
import sys
def shrink(text):
    print(text[:8])
def enlarge(text):
    print(text.ljust(8, 'Z'))
if len(sys.argv) < 2:
    print("none")
else:
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)