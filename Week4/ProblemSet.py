#Question 1
#an attacker intercepts the following ciphertext (hex encoded): 
#20814804c1767293b99f1d9cab3bc3e7 ac1e37bfb15599e5f40eef805488281d
#he knows that the plaintext is the ascii encoding of the message "pay bob 100$" (excluding the quotes).    
#he also knows that the cipher used is cbc encryption with a random iv using aes as the underlying block cipher.
#show that the attacker can change the ciphertext so that it will decrypt to "pay bob 500$".  
##what is the resulting ciphertext (hex encoded)?
#this shows that cbc provides no integrity.


