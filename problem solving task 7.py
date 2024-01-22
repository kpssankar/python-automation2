#program to create text file
# Specify the directory path
file = open("Users/Admin/Desktop/IITMADRASGUVIPythonAutomationtraining/Tasks/sample.txt", "a")

file.write("current timestamp: 16:59:00.\n")
file.write("This is the second line.")

file.close()






#program to disply the content of sample.txt file
file = open(" C:/Users/Admin/Desktop/IITMADRASGUVIPythonAutomationtraining/Tasks/sample.txt", "r")

print(file.read())

file.close()