str = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

key = str[0] ^ ord('c')

print("Flag:")
print(''.join(chr(c ^ key) for c in str))