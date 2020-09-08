def words_occur():
    file_name = input('Input file name: ')
    f=open(file_name,mode='r',encoding='ascii')
    word_list=f.read().split()
    f.close()
    occurs_dict={}
    for word in word_list:
        occurs_dict[word]=occurs_dict.get(word,0)+1
        print("File %s has %d words (%d are unique)" \
           % (file_name3, len(word_list), len(occurs_dict)))
        print(occurs_dict)
    if __name__ == '__main__': 
        words_occur()