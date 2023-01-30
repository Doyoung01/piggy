import pandas as pd

class journal:
    def __init__(self, index, title, content, imoji):
        self.index = index # int
        self.title = title # string
        self.content = content # string
        self.imoji = imoji # int
        self.often = 0

    '''
    length = 0
    
    def get_len():
        return journal.length
    
    def plus_len():
        journal.length += 1

    def minus_len():
        journal.length -= 1
    '''

    # 사진, 발행일자 안 넣음

def write(title, content, imoji):
    global df
    len = df.shape[0]
    print(df)
    print(len)


    # l = journal.get_len()
    # print(l)
    tmp = journal(len, title, content, imoji)

    print(tmp.title, tmp.content, tmp.imoji, tmp.index, tmp.often)

    data = {
        'index': [tmp.index],
        'title': [tmp.title],
        'content': [tmp.content],
        'imoji': [tmp.imoji],
        'often': [tmp.often]
    }
    tmp_df = pd.DataFrame(data)
    df = pd.concat([df, tmp_df])
    df.to_csv('./test_file.csv', index=False)


def pick(idx):
    return df.iloc[idx]

def get_length():
    len = df.shape[0]
    
    return len

df = pd.read_csv('./test_file.csv')
while(1):
    title, content, imoji = input().split()
    write(title,content, imoji)
    print(df)
    print("=============")