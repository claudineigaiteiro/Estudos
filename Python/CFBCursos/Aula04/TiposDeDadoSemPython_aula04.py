x = 1 #int
x = "CFB Cursos" #string 
x = 15.6 #float
x = False #bool
n1 = 5; n2 = 2; i = complex(n1, n2) #complexo 

x = ["Carro", "Avião", "Navio", 1, 58.3, True] #list / array
x = ("Carro", "Avião", "Navio", 1, 58.3, True) #tupla
#x[0] = "Onibus" Quando tupla não posso alterar os itens da lista

x = range(0,100,1) #list
x={ #dicty
    "canal":"CFB Cursos",
    "curso":"Curso de Python",
    "nome":"Claudinei"    
}

x = {5,7,4,5,7,4,8} #set #não repete valores
x = frozenset({5,7,4,5,7,4,8}) #set #vai congelar os valores

print(i.real)
print(i.imag)

#print("Valor " + str(x[0])) #impresão das listas 
#print("Valor: " + x["curso"]) #impresão do dicty
print("Valor: " + str(x))
print("Tipo: " + str(type(x)))