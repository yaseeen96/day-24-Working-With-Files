#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



letter_content = ""
# read file content
with open("Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()

# replace file content
with open("Input/Names/invited_names.txt") as invitees:
    list_names = invitees.readlines()
    for name in list_names:
        updated_name = name.strip("\n")
        with open(f"Output/ReadyToSend/{updated_name}.txt", "w") as new_letter:
            updated_content = letter_content.replace("[name]", updated_name)
            # print(updated_content)
            new_letter.write(updated_content)
        
        

    
