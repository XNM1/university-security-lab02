import hashlib
import sys

def main():
    hashed_string = sys.argv[1]         #SHA-256 hash
    word_list = sys.argv[2]             #wordlist location

    try:
        words = open(word_list, "r")
    except:
        print("\n File Not Found")
        quit()

    for word in words:
        calculated_hash = hashlib.sha256(word.strip().encode('utf-8')).hexdigest()

        if calculated_hash == hashed_string:
            print('\nPassword Found & Password Is: %s ' % word)
            break

    else:
        print('\nPassword Not Found')
        print('Try Another Wordlist Or Hash')


if __name__ == '__main__':
    main()
