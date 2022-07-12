class Elgamal:
    
    def __init__(self, g, a, p):
        self.g = g
        self.a = a
        self.p = p
        
    def public_key(self):
        A = (self.g ** self.a) % self.p
        return A
    
    def encrypt(self,A, m, k):
        c1 = (self.g ** k) % self.p
        c2 = (m* (A ** k)) % self.p
        return c1, c2
    
    def decrypt(self, c1, c2):
        m = ( ((c1 ** self.a) ** (self.p-2)) * ((c2)) ) % self.p
        return m
    

elgamal = Elgamal(567, 16, 7829)
x, y = elgamal.encrypt(elgamal.public_key(), 22, 18)
print(x + y)
m = elgamal.decrypt(x, y)
print(m)

