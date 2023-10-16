def is_valid_pin_codes(pin_codes):
    if len(pin_codes) > 0:
        for char in pin_codes:
            if isinstance(char, str) and len(char) == 4:
                try:
                    char_to_int = int(char)
                except ValueError:
                    print ("not a number")
                    return False
                pin_codes.remove(char)
                if char not in pin_codes:
                    print (100 )
                else:
                    print ("duplicates ", char)
                    return False               
            else:
                print ("invalid pin ", char)
                return False
    else:
        print (444)
        return False  
    print (777)
    return True


print(is_valid_pin_codes(['1101', '9034', '00112']))