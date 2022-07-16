
try:
    def isvowel(str):
        countvowels = 0
        for i in range(str):
            if(i=='a',i=='A',i=='e',i=='E',i=='o',i=='O',i=='u',i=='U',i=='i',i=='I'):
                countvowels+=1

        print(countvowels)

if __name__ == '__main__':

    str = input("Enter any String :")
    isvowel(str)

except:
    print("'str' object cannot be interpreted as an integer")