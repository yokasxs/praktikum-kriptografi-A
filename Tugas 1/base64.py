import base64

hex = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
byte = bytes.fromhex(hex)
flag = base64.b64encode(byte)

print("Flag:")
print(flag)