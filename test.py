with open('/Users/victorialemay/Documents/ecole/Genie_industriel/Session_6/SIAD/TP2/inst1.dzn.txt', 'r') as text_file:
    for line in text_file.readlines():
        line = line.strip()
        param_name, param_value = line.split('=')

        param_name = param_name.strip()
        param_value = param_value.strip(';')
        param_value = param_value.strip(']')

        if param_name == 'placedispo':
            placedispo = param_value
            print(placedispo)
        
        elif param_name == 'pers':
            pers = param_value.replace('[', '').split(',')
            pers = [int(p.strip()) for p in pers]
            print(pers)

        #print(line[0:-1])

print()