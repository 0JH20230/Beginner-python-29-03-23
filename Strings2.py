phrase3 = "WE ARE THE CHAMPIONS "
phrase4 = " my friend"
          #01234567890123456789012345678901
          #00000000001111111111222222222233
print(len(phrase3))                                                                                   #"len()" function retrieves the length of characters in the variable @phrase3
print(len(phrase4))                                                                                   #"len()" function retrieves the length of characters in the variable @phrase4
print(len(phrase3),len(phrase4))                                                                      #using 2 "len()" functions retrieves the length of characters in both variables @phrase3 and @phrase4
print(phrase3[0])                                                                                     #squared brackets retrieves the letter at the number with in brackets
print(phrase3.index("CHAMPIONS"))                                                                     #".index()" will retrieve the index where a letter or word known as a parameter is placed within the variable @phrase3
print(phrase4.index("end"))                                                                           #".index()" will retrieve the index where a letter or word known as a parameter is placed within the variable @phrase4
print( phrase3 + phrase4.replace("friend","brother"))                                     #".replace()" function replaces the word "friend" with the new word "brother" @phrase4

print(phrase3.lower() + phrase4.upper())                                                              #using the ".lower()" and the ".upper()" function I have switched the cases in the variables @phrase3 and @phrase4
print(phrase3.isupper())                                                                              #using the ".isupper()" function on the variable @phrase3 the computer assigns it as true value  as the string is fully in caps
print(phrase3.islower())                                                                              #using the ".islower()" function on the variable @phrase3 the computer assigns it as false value as the string is not in caps
print(phrase4.isupper())                                                                              #using the ".isupper()" function on the variable @phrase4 the computer assigns it as false value as the string is in fully in lower case
print(phrase4.islower())                                                                              #using the ".islower()" function on the variavle @phrase4 the computer assigns it as a true value as the string is fully in lower case
print(phrase3.lower().islower())                                                                      #@phrase3 the ".lower()" function runs a previously uppercaps string in lower case and then runs the ".islower()" function to check, which the computer concludes is a true value"
print(phrase4.upper().isupper())                                                                      #@phrase4 the ".upper()" function runs a previously lower caps strings in upper case and the runs the ".isupper()" function to check, which the computer concludes is a true value