file = open(file="data.txt", mode="r")
print("File information:")
print("" + "-" * 20)
print(file)

print("\nFile Contents:")
print("" + "-" * 20)
contents = file.read()
print(contents)


file.close()

contentList = contents.splitlines()
print("\nFile Contents as List:")
print("" + "-" * 20)
print(contentList)
