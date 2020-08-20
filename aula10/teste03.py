from unittest import TestCase, main

def eh_impar(num):
    try:
        if int(num) % 2 != 0:
            return True
        else:
            return False    
    except Exception:
        return None
    
    
    


class Impar(TestCase):
    def test_impar(self):
        self.assertEqual(eh_impar(3), True)
        self.assertEqual(eh_impar(12313), True)
        self.assertEqual(eh_impar(3212), False)
        self.assertEqual(eh_impar('21321'), True)
        self.assertEqual(eh_impar('321312'), False)
        self.assertEqual(eh_impar('dadsaw11wa'), None)
        
        

if __name__ == '__main__':
    main()
    
        
    