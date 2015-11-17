class persona:
   nombre = ""
   apellido = ""
   edad = 0
   
   def dormir(self):  
       print "zzz"  
       
   def sumar(self,num1, num2):
       resultado = num1 + num2
       return resultado
   
   
juan = persona()
juan.nombre = "Juan"
print juan.nombre
juan.dormir()
print juan.sumar(1,6)
   
