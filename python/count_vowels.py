#count_vowels
def Check_Vow(string, vowels):
    string = string.casefold()
    count = {}.fromkeys(vowels, 0)
    # To count the vowels
    for character in string:
        if character in count:
            count[character] += 1
            return count
# Driver Code
vowels = 'aeiou'
string = "Hi, I love eating ice cream and junk food"
print (Check_Vow(string, vowels)) 

#Output: {'a': 2, 'e':4 , 'i':2 , 'o':3 , 'u':1}