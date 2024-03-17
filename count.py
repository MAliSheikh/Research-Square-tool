
filename = "kws.txt"

with open(filename, 'r') as f:
    data_lines = f.readlines()
    
    kws = []
    
    for line in data_lines:
        if line:
            q, n = line.split(': ')
            
            if int(n) < 1000:
                kws.append(f'{q}: {n}')
    
    with open('keywords.txt', 'w') as f:
        for kw in kws:
            f.write(f'{kw}')
    