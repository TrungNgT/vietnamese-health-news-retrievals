
def txt2arr(file_path: str) :
    syn_arr = []
    with open(file=file_path, mode='r', encoding='utf-8') as file :
        lines = file.readlines()
        for l in lines :
            new_l = l.split("\n")
            syn_arr.append(new_l[0])

    #print(syn_arr)
    return syn_arr

#txt2arr('./out_n.txt')