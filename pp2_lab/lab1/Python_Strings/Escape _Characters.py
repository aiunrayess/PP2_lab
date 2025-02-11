#Single quote
txt = 'It\'s alright.'
print(txt) 

#Backslash
txt = "This will insert one \\ (backslash)."
print(txt) 

#New line
txt = "Hello\nWorld!"
print(txt) 

#Carriage return
txt = "Hello\rWorld!"
print(txt) 

#Tab
txt = "Hello\tWorld!"
print(txt) 

#Backspace
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) #Prints HelloWorld!

#Octal Value
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) #Prints "Hello"

#HEX value
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) #Prints Hello
