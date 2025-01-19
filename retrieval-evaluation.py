def precision(q_jud: list):
    cnt_yes = 0
    for res in q_jud:
        if (res == '1'):
            cnt_yes += 1
    res = cnt_yes / len(q_jud)
    return round(res, 2)

def recall(q_jud: list, R: int):
    cnt_yes = 0
    for res in q_jud:
        if (res == '1'):
            cnt_yes += 1
    res = cnt_yes / R
    return round(res, 2)

def F1(q_jud: list, R: int):
    p = precision( q_jud)
    r = recall(q_jud, R)
    res =  2 * p * r / (p + r)
    
    return round(res, 2)

def AP(q_jud: list, R: int):
    cnt_yes = 0
    ap_score = 0
    for i in range(len(q_jud)):
        if (q_jud[i] == '1'):
            cnt_yes += 1
            ap_score += cnt_yes / (i + 1)
    ap_score *= 1 / R
    return round(ap_score, 2)

R_list = [10, 9, 8, 11, 12, 6, 12, 13, 8, 9, 12, 11, 10, 11, 5]

with open (file='relevance_judgment.txt', mode='r', encoding='utf-8') as file:
    data = file.readlines()
    ap_score = []
    lexical_map = vector_map = 0
    j = 0
    for i in range(len(data)):
        judg_list = data[i].replace('\n', '').split('\t')
        ap = AP(judg_list, R_list[j])
        ap_score.append(ap)
        #print(ap)
        if (i % 2 == 1):
            vector_map += ap
            j += 1
        else:
            lexical_map += ap
    
    print(ap_score)
    print(f"MAP of lexicalSearch: {lexical_map * 2 / len(data)}")
    print(f"MAP of vectorSearch: {vector_map * 2 / len(data)}")
    #print(ap_score)