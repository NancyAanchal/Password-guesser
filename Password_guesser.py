import itertools
import string
import time

def common_guess(word:str):
    with open('common_pwds.txt','r')as words:
        word_list:list[str]=words.read().splitlines()

    for i, match in enumerate(word_list,start=1):
        if match==word:
            return f'Nz: Common match: {match} ({i})'

while True:
    def brute_force(word:str, length:int, lowercase:bool=True, digits:bool=True, symbols:bool=False, uppercase:bool=False):
        chars=''
        
        if lowercase:
            chars=string.ascii_lowercase

        if digits:
            chars+=string.digits

        if symbols:
            chars+=string.punctuation

        if uppercase:
            chars+=string.ascii_uppercase

        attempts:int=0
        for guess in itertools.product(chars,repeat=length):
            attempts+=1
            guess:str=''.join(guess)

            if guess==word:
                return f'Nz: "{word}" was cracked in {attempts:,} guesses.'
            #print(guess,attempts)


    def main():
        password=input("\nNz: Enter a password: ")

        print('Nz: Searching...')

        start_time:float=time.perf_counter()

        if common_match:=common_guess(password):
            print(common_match)
        else:
            if cracked:=brute_force(password, length=len(password),lowercase=True, digits=True, symbols=False, uppercase=False):
                print(cracked)
            else:
                print('Nz: There was no match... Your password is strong.')

        end_time:float=time.perf_counter()
        print(round(end_time-start_time,2),'s')
            

    if __name__=='__main__':
        main()
        
    
