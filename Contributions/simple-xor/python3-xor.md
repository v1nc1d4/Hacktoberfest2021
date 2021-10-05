###  Simple One 
**note : you can do it in 2 lines**
  `pip3 install pwntools`
  
  
  ```python
  from pwn  import *
  key="pj"
  xor(key,"secret").decode()
  '\x03\x0f\x13\x18\x15\x1e'
  #encrypted=\x03\x0f\x13\x18\x15\x1e
  #to decrypt
  xor(key,"\x03\x0f\x13\x18\x15\x1e").decode()
  'secret'
  ```
  
  **we got the secret** 
  
  **its simple in python3**

