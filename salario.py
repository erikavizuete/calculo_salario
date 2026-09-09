def calcular_salario_semanal(horas, pago):
    salario = horas * pago
    return salario

if __name__== "__main__":
   horas_trabajadas = 40
   pago_hora = 3.01
   resultado = calcular_salario_semanal(horas_trabajadas, pago_hora)
   print ("El salario semanal es:", resultado)