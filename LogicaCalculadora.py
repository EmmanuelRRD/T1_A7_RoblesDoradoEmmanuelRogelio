'''
Created on 17 mar 2024

@author: emanuel
'''
class Calculadora:
    
    def __init__(self, primerNumero = 0, operacion="", segundoNumero=0):
        self.primerNumero = 0.0
        self.operacion = operacion
        self.segundoNumero = 0.0
    
    def sumar(self):
        return float(self.primerNumero) + float(self.segundoNumero)
    def restar(self):
        return float(self.primerNumero) - float(self.segundoNumero)
    def multiplicar(self):
        return float(self.primerNumero) * float(self.segundoNumero)
    def dividir(self):
        return float(self.primerNumero) / float(self.segundoNumero)
    
    def indicarOperacion_Numero(self, num, op):
        self.primerNumero = num
        self.operacion = op
        print(self.primerNumero)
        print(self.operacion)
    
    def indicarSegundoNumero(self, num):
        self.segundoNumero = num
        print(self.segundoNumero)
        
    def realizarOperacion(self):
        if(self.operacion=="+"):
            return self.sumar()
        elif(self.operacion=="-"):
            return self.restar()
        elif(self.operacion=="*"):
            return self.multiplicar()
        elif(self.operacion=="/"):
            return self.dividir()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        