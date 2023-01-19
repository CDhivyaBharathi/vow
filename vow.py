import vowels

n = input("Enter String: ")
print("Are there vowels in the string: ",vowels.isVowel(n))
print("New string: ",vowels.removeVowel(n))
print("The number of vowels: ",vowels.countVowel(n))