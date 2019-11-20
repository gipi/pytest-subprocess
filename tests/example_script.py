"""An example script to test subprocess."""
import sys
import time

print("Stdout line 1")
if "stderr" in sys.argv:
    print("Stderr line 1", file=sys.stderr)
print("Stdout line 2")

if "wait" in sys.argv:
    time.sleep(0.5)

if "non-zero" in sys.argv:
    sys.exit(1)
