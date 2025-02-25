### Look into check_key() function in the question file
### we found that they are using hashlib.sha256(username_trial).hexdigest()
import hashlib

def reverse_key():
    key_part_1 = "picoCTF{1n_7h3_|<3y_of_"
    key_part_2 = "xxxxxxxx"
    key_part_3 = "}"
    
    # We know that they use the `username_trial` = b"GOUGH"
    # NOT "GOUGH" but b"GOUGH" !!
    username = b"GOUGH"
    
    # As we can see in the check_key() function, they start with 4 then 5, 3, 6, 2, 7, 1, and 8
    hash_order_list = [4, 5, 3, 6, 2, 7, 1, 8]
    
    # Reset the key_part_2
    key_part_2 = ""    
    
    # Get the hash values from the username
    for i in range(len(hash_order_list)):
        key_part_2 += hashlib.sha256(username).hexdigest()[hash_order_list[i]]
    
    # Combine the key parts    
    flag = key_part_1 + key_part_2 + key_part_3
    
    print(flag)
    
reverse_key() 