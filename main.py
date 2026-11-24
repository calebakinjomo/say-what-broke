#!/usr/bin/env python3
"""Say What Actually Broke — one line of brutally honest error copy.

Prints the entry exactly once, with nothing else on stdout.
The line's angle: the save didn't fail for one reason — it failed three
ways at once (full disk, failed backup, absent autosave), and the fix it
offers is the only honest one: free space, then retry.
"""

LINE = "Your file didn't save \u2014 the disk is full, the backup failed first, and autosave was on its lunch break. Delete something, then try again."

print(LINE)
