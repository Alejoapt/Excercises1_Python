#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ejercicio 1 
print ("hello world")


# In[15]:


# Ejercicio 2
variable = ("hello world")
print (hello)


# In[5]:


#Ejercicio 3
type(variable)


# In[11]:


variable = ("hello world")


# In[12]:


#Ejercicio 4
variable = variable[0:5]
print (variable)


# In[21]:


lista= range(0,21)


# In[19]:


def oddNumbers(some_list):
    for i in some_list:
        if((i%2)!=0):
            print (i)
        


# In[22]:


#Ejercicio 5
oddNumbers(lista)


# In[1]:


lista2 = [2,4,6,7,13]


# In[11]:


def exponential(some_list, exp):
    for i in some_list:
        e = i**exp
        print(e)


# In[12]:


#Ejercicio 6
exponential(lista2,2)


# In[15]:


#Ejercicio 7
diccionario = {'variableUno':[1,2,3,4], 'variableDos':["1","a","?"]}
print(diccionario)


# In[20]:


#Ejercicio 8 
word = "Spam"
word = "Z" + word[1:]
print(word)


# In[22]:


#Ejercicio 9
x = float(input("Escribe el ancho del rectangulo "))
y = float(input("Escribe el alto del rectangulo "))
print("El perímetro es: %s"% ((2*x) + (2*y)))


# In[23]:


Lista3 =  list(range(1,101))


# In[25]:


def metodo8(a):
    for i in a:
        if i % 2 == 0:
            print("whiz %s" %i)
        elif  i % 3 == 0:
            print("bang %s" %i)
        else:
            print("")


# In[26]:


#Ejercicio 11
metodo8(Lista3)

