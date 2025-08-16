from ascii_art import cc
print(cc)

alphhabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                  'n','o','p','q','r','s','t','u','v','w','x','y','z']


def enc(mssg,shift):
    encoded = ""
    for i in mssg:
        if i in alphhabet_list:
            actual_shift = alphhabet_list.index(i) + shift
            actual_shift %= len(alphhabet_list)
            encoded += alphhabet_list[actual_shift]
        else :
            encoded += i
    return encoded

def dec(mssg,shift):
    decoded = ""
    for i in mssg:
        if i in alphhabet_list:
            actual_shift = alphhabet_list.index(i) - shift
            actual_shift %= len(alphhabet_list)
            decoded += alphhabet_list[actual_shift]
        else:
            decoded += i
    return decoded


game_on = True
while game_on :
    enc_or_dec =  input("Type 'e' to encrypt, type 'd' to decrypt: \n").lower()
    message = input("Type your message:\n").lower()
    shift_num = int(input("Type the shift number:\n"))
    if enc_or_dec == 'e':
        print(f"Here is your enoded message :\n{enc(message,shift_num)}")
    if enc_or_dec == 'd':
        print(f"Here is your decoded message :\n{dec(message,shift_num)}")
    cont = input("Type 'Yes' if you want to go again. Otherwise type 'No'.\n").lower()
    if cont == 'yes' :
        game_on = True
    elif cont == 'no':
        game_on = False
    
    



