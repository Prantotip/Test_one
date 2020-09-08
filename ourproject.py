def words_count():
    file_name = input('Input file name: ')
    f = open(file_name, mode='r')
    word_list = f.read().split()
    f.close()
    occurs_dict = {}

    for word in word_list:
        occurs_dict[word] = occurs_dict.get(word, 0) + 1
        print('File {} has {} words ({} are unique)'.format(
            file_name, len(word_list), len(occurs_dict)
        ))
        print(occurs_dict)


if __name__ == '__main__':
    words_count()
