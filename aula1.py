#Função 2ºgrau: ax² + bx + c

a = float(input('digite o valor de a: '))
b = float(input('digite o valor de b: '))
c = float(input('digite o valor de c: '))

#busca por intervalo

def procuraintervalo(a,b,c):
    def f(a,b,c,x):
        return a*x**2+b*x+c, x 
    x = -10
    funcao1, xis1 = f(a,b,c,x)
    x+=2
    funcao2, xis2 = f(a,b,c,x)
    if funcao1*funcao2 <0:
        return xis1,xis2
    else:
        return ""    
