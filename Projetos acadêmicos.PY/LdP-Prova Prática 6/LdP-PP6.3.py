#3.	Use sua criatividade, elabore o problema (o enunciado) de um problema que usa função e resolva o problema proposto,
# ou seja, faça a implementação da função def e da função principal (main).
#A função recebe dois valores inteiros que corresponde ao horário(hora e minuto), faz o cálculo e retorna um valor convertido em segundos.
def converte_segundos(horas, minutos):  
    vl_segundo = (horas * 60 + minutos)*60    
    return vl_segundo                    

if __name__ == '__main__':               
    h = int(input("Horas: "))           
    m = int(input("Minutos: "))
    retorno = converte_segundos(h, m)     
    print("\nHorário convertido em segundos:", retorno) 