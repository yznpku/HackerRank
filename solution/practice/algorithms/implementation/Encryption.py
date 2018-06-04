s = input().strip()
    length = len(s)
    columns = int(math.ceil(math.sqrt(length)))
    
    encrypted_string = ""
    
    for j in range(columns):
        for i in range(columns):
            if j + i * columns < length:
                encrypted_string += s[j + i * columns]
        encrypted_string += " "
        
print(encrypted_string)
