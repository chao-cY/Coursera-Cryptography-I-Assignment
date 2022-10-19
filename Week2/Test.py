def split_hex(h, dtype='int'):
    '''
    :stuck_out_tongue_winking_eye:aram h: A hex string. Example: "315c4eea". Its length should be an even number.
    :return: A list of integer corresponding to every two letters in h
    '''
    if dtype == 'int':
        split = [int(h[2 * i:2 * i + 2], 16) for i in range(len(h) // 2)]
    elif dtype == 'str' or 'string':
        split = [h[2 * i:2 * i + 2] for i in range(len(h) // 2)]
    else:
        split = [int(h[2 * i:2 * i + 2], 16) for i in range(len(h) // 2)] 
    return split



raw = 'hello world!!'
length = len(raw)
print(['=']*length)


ciphertext="32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904"
print(len(ciphertext))

cipher = [chr(x) for x in split_hex(ciphertext)]
print(len(cipher))

print(cipher)