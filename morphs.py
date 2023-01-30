import pandas as pd
import re
from konlpy.tag import Okt

okt = Okt()

# result = open('data/mp.txt','w',encoding='utf-8')
morphs = False

if morphs:
    with open('data/rawcorpus.txt',encoding='utf-8') as f:
        all = []
        sentence = []
        nouns = []
        for l in f:
            l = l.strip()
            

            mps = okt.pos(l)
            noun = [ data[0] if data[1] == 'Noun' else '' for data in mps]

            noun = ' '.join(noun)
            noun = re.sub(' +',' ',noun).strip()
            if noun.strip() == '':
                continue

            nouns.append(noun)

            mp = ['/'.join(data) for data in mps]
            mp = ' '.join(mp) #+ '\t' + l

            all.append(mp)        
            sentence.append(l)
        
        datas = pd.DataFrame({'noun':nouns,'morps_pos':all,'sentence':sentence})
        datas.to_csv('data/train.csv')
            # result.write(mp+'\n')

    # result.close()
else:
    from collections import defaultdict
    import matplotlib.pyplot as plt
    n_length = 0
    s_length = 0
    count = 0
    datas = pd.read_csv('data/train.csv')
    # print(datas[['noun','sentence']])
    graph_data_n = defaultdict(int)
    graph_data_s = defaultdict(int)
    for n in datas[['noun','sentence']].itertuples():#.iloc[:,:]:
        # print(n)
        noun = n[1].split()
        sentence = list(n[2])
        n_length += len(noun)
        s_length += len(sentence)
        count += 1
        graph_data_n[len(noun)] += 1
        graph_data_s[len(sentence)] += 1

    print('n:',n_length/count,'s:',s_length/count)
        # print(n)
    max_x = 30
    max_y = 0
    x = graph_data_s.keys()
    
    y = graph_data_s.values()

    plt.bar(x,y)
    plt.xticks()

    plt.show()