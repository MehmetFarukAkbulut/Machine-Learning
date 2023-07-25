import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veriler=pd.read_csv('veriler.csv')


print(veriler)

boy = veriler[['boy']]
print(boy)
boykilo = veriler[['boy','kilo']]
print(boykilo)

x=10

class insan:
    boy=180
    def kosmak(self,b):
        return b+x
    
ali = insan()
print(ali.boy)
print(ali.kosmak(90))
