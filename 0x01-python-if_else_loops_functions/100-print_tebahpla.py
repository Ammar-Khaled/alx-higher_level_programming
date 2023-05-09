#!/usr/bin/python3
lower = True
for i in range(26):
	if lower:
		print(chr(ord('z') - i), end='')
	else:
		print(chr(ord('z') - i - 32), end='')
	lower = not lower
