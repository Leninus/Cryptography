import encrypt as ec
import decrypt as dc

running = True
while running == True:
    mode = int(input("Input [1] to encrypt, [2] to decrypt, [3] to exit: "))
    while mode == 1:
        ec.main()
        if input("Input text if you wish to change mode, leave empty if you wish to continue encrypting: ") == True:
            pass
        else:
            mode = 0
    while mode == 2:
        dc.main()
        if input("Input text if you wish to change mode, leave empty if you wish to contunue decrypting") == True:
            pass
        else:
            mode = 0
    while mode == 3:
        running = False
        print("Exitting")
        mode = 0