msg= (input(("Enter your message:")))
print("Type 1 for secret language conversion or type 0 for normal language conversion")
inp = input()
if inp == "1":
    def secret_lamguage(msg):
       msg = msg[::-1]
       msg = "jkm"+msg+ "hfj"
       return msg

    print(secret_lamguage(msg))

else:
    def normal_language(msg):
        msg = msg[3:-3]
        msg = msg[::-1]
        return msg
    print(normal_language(msg))


        
