import zipfile  # Library used for password encrypted zipped folder/file
import time

# Get the target file path and name from the user
folderpath = input('Path to the file: ')
zipf = zipfile.ZipFile(folderpath)
endtime = 0  # Initialize a PdfFileReader object

if not zipf:  # Checks if the file is password encrypted
    # Notifies if the zipped file/folder is not password encrypted
    print('The zipped file/folder is not password protected! You can successfully open it!')

else:
    starttime = time.time()  # Save the start time
    result = 0  # Intialize a variable result with zero. '0' will indicate Failure, while '1' will idicate Success
    c = 0  # Initialize a variable c to keep the count of passwords tried

    # Build a character array including all numbers,lowercase letter, uppercase letters and special haracters. Total 10+26+26+33 = 95 characters
    characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                  '!', '@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<', '}', '{', '^', '[', ']', ' ', '+', '-', '_', '&', ';', '"', '?', '`', "'", '\\']

    print("Brute Force Started...")

    # Finally, if the password is not found even after appying all possile combination of characters upto 4 character length, notify the user as below, else print congratulations
    if(result == 0):
        print("checking for 4 character password")

        for i in characters:
            for j in characters:
                for k in characters:
                    for l in characters:
                        guess = str(i) + str(j) + str(k) + str(l)
                        password = guess.encode('UTF-8').strip()
                        c += 1
                        print(guess)

                        try:
                            with zipfile.ZipFile(folderpath, 'r') as f:
                                f.extractall(pwd=password)
                                print('Success! password is : ' + guess)

                                endtime = time.time()
                                result = 1

                                break
                        except:
                            duration = endtime - starttime
                            # print("Sorry, password not found. A total of "+str(c)+"+ possible combinations tried in " +
                            #       str(duration)+" seconds. Password is not of 4 characters.")

                    if result == 1:
                        break
                if result == 1:
                    break
            if result == 1:
                break

    else:
        # duration = endtime - starttime
        print('Congratulations!!! Password found after trying ' +
              str(c))
