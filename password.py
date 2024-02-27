#this is the simple encryption password method
Password="this is a Secret"
print(Password)
Password=Password[::-1]
print(Password)
Password=Password.replace(" ","pwd")
print(Password)
Password="22748"+Password
print(Password)

#now this is the smiple decryption password method
print('\n Decrypting...')

Password = Password[5::]
print(Password)
Password=Password.replace('pwd',' ')
print(Password)
Password=Password[::-1]
print(Password)