import bitarray

first = bitarray.bitarray()
first.frombytes('this is a test'.encode('utf-8'))

sec = bitarray.bitarray()
sec.frombytes('wokka wokka!!!'.encode('utf-8'))


print(f"{first}\n{sec}")

first ^= sec
print(first)
i = 0
for bit in first:
    i += bit
print(i)