def print_upper_words(list_of_strings, must_start_with={"h","y"}):
    for string in list_of_strings:
        for letter in must_start_with:
            if string[0]==letter:
                print(string.upper())
       
    
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])