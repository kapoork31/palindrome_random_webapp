def palindrome(message):
    """
    returns true if message is a palindrome
    loops from either side and if both indexes meet then palindrome is found
    """
    if len(message) == 1:
        return True
    
    i = 0
    j = len(message)-1

    while i<j:
        if message[i] != message[j]:
            return False

        i +=1
        j -=1
    return True

def gen_random_string(message,rnd_int):
    """
    take in message and random integer
    from the specified message and return the message
    """
    is_palindrome = palindrome(message)
    palindrome_message = 'a'
    if not is_palindrome:
        palindrome_message = 'not a'
    msg_str = 'I would like {} {} please. {} is {} palindrome'.format(rnd_int, message, message, palindrome_message)
    return msg_str