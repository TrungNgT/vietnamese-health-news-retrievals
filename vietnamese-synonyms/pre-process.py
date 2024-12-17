folder_path = './ViData/ViCon/'
files_name = ['400_noun_pairs.txt']
output_name = ['out_n.txt', 'out_v.txt', 'out_a.txt']

def custom_replace(s: str) :
    res = ""
    size = len(s)
    for i in range(size) :
        if (s[i] != ' ' and s[i] != '\t') :
            res += s[i]
        else :
            if (s[i - 1] != ' ' and s[i - 1] != '\t') :
                res += ' '
    return res

for fn in files_name :
    file_path = folder_path + fn
    synomyms = []

    with open(file=file_path, mode="r", encoding='utf-8') as file:
        lines = file.readlines()
        lines_num = len(lines)
        print(lines_num)
        error_line = [1]
        #print(lines[14])
        for i in range (1, lines_num) :
            lines[i] = custom_replace(lines[i])
            #print(lines[i])
            tp = lines[i].split(' ')
            if (len(tp) < 3) :
                error_line.append(i + 1)
                continue
            else :
                tp[0] = tp[0].replace('_', ' ')
                tp[1] = tp[1].replace('_', ' ')
                if (tp[2][0] == 'S') :
                    s = tp[0] + ', ' + tp[1]
                    synomyms.append(s)
    res = '\n'.join(synomyms)
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(res)
print(synomyms)
print(error_line)