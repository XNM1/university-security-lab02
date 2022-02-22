import hashlib
import sys
import multiprocessing


def main():
    hashed_string = sys.argv[1]         #SHA-256 hash
    word_list = sys.argv[2]             #wordlist location
    threads_count = int(sys.argv[3])    #count of processes

    try:
        words = open(word_list, "r")
    except:
        print("\n File Not Found")
        quit()

    pool_obj = multiprocessing.Pool(processes=threads_count)

    word = pool_obj.map(lambda i: search_hash(hashed_string, words, threads_count, i), range(0, threads_count))
    if word:
        print('\nPassword Found & Password Is: %s ' % word)
    else:
        print('\nPassword Not Found')
        print('Try Another Wordlist Or Hash')


def search_hash(hashed_string, words, threads_count, value):
    count_words = len(words)/threads_count

    for word in words[value:value+count_words]:
        calculated_hash = hashlib.sha256(word.strip().encode('utf-8')).hexdigest()
        if calculated_hash == hashed_string:
            return word
        
    return None
        
if __name__ == '__main__':
    main()
