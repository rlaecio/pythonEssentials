'''
    Dado o teste abaixo, desenvolva a função que aprove o teste.
'''

from unittest import TestCase, main 

def palindrome(palavra):
    ## desenvolvimento da função
   return True if palavra == palavra[::-1] else False
    #
    

class Teste(TestCase):
    def test_palindrome(self):
        self.assertEqual(palindrome('ovo'), True)
        self.assertEqual(palindrome('arara'), True)
        self.assertEqual(palindrome('osso'), True)
        self.assertEqual(palindrome('4linux'), False)
        

if __name__ == "__main__":
    main()