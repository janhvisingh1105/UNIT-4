def file_operations():
    #opening a file and writing to it
    with open("example.txt", "w") as file:
        file.write("This is the first line of the file.\n")
        print("File written successfully.")
        #opening the file and reading its contents.
        with open("wxample.txt", "r") as file:
            contents = file.read()
            print("\nContents of the file:")
            print(contents)
            #Appending additional content to the file
            with open("exampe.txt", "a") as file:
                file.write("This is the appended line.\n")
                print("\nContent appended successfully")
                #Re-reading the file to show the appended content
                with open("example.txt", "r") as file:
                    updated_contents=file.read()
                    print("\nUpdated contents of the file after appending:")
                    print(updated_contents)
                    if__name__=="__main__":
                    file_operations()
                        