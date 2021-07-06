#para eventual consulta: 

#somar número de dias numa data no python (import datetime): 
#https://hkotsubo.github.io/blog/2019-04-06/nao-reinvente-a-roda-como-somar-dias-a-uma-data
#https://pt.stackoverflow.com/questions/2843/como-subtrair-duas-datas-usando-python

#ângulo a partir do seno ou do cosseno (import math): 
#https://stackoverflow.com/questions/6745464/inverse-cosine-in-python
 #não há mais de um ângulo com o mesmo cosseno para ângulos menores que 180°, ok! 
 #caso onde uso a lei dos senos (caso 3), há apenas 1 possibilidade de ângulo para ser obtida a partir do seno, e este é
 #necessariamente o primeiro ângulo obtido com aquele seno, então ok também! 

#outra restrição aplicada: teorema da desigualdade triangular
#https://www.mathwarehouse.com/geometry/triangles/triangle-inequality-theorem-rule-explained.php
#https://www.mathwarehouse.com/triangle-calculator/online.php



import math #para cálculos de seno, cosseno e raiz quadrada
import datetime #para input de data
from datetime import date #para formato de data sem horas
from datetime import timedelta #para operações com formato de data

s = 10.81 #distância Vênus-Sol, em quilômetros; o *10^7 (*10**7) está apenas no 'print' final
S = 14.95 #distância Terra-Sol, em quilômetros; o *10^7 (*10**7) está apenas no 'print' final
r = 0 #distância Terra-Vênus, em quilômetros; o *10^7 (*10**7) fica apenas no 'print' final
ψ = 0 #ângulo Sol-Terra-Vênus, em radianos
φ = 0 #ângulo Sol-Vênus-Terra, em radianos
θ = 0 #ângulo Vênus-Sol-Terra, em radianos
p = 0 #fase (área da parte iluminada dividida pela área total do círculo), em km²
b = 0 #brilho, em função de K (constante), como explicitado no 'print' final

#o limite de casas para a entrada de ângulos é de 15 casas decimais, pois os valores de referência foram
#calculados para π = 3.141592653589793

ultimacinf = date(2020, 6, 3) #data da última conjunção inferior de vênus. fonte: https://in-the-sky.org/news.php?id=20200603_11_100
proximacinf = date(2022, 1, 8) #data da próxima conjunção inferior de vênus. fonte: https://in-the-sky.org/news.php?id=20220109_11_100
datacsup = date(2021, 3, 22) #data da conjunção superior entre as duas conjunções inferiores acima (ultimacinf + 292 dias)

#o programa retorna 2 possíveis datas para cada configuração do triângulo formado entre Sol, Terra e Vênus. 
#a 1ª data é calculada pelos dias posteriores à última conjunção inferior, e a 2ª pelos dias anteriores à próxima
t = 0 #número de dias anteriores ou posteriores à conjunção inferior
data1 = 0 #possível data 1, calculada a partir da última conjunção inferior
data2 = 0 #possível data 2, calculada a partir da próxima conjunção inferior
cinf1 = 0 #dias faltantes para a próxima conjunção inferior, referente à data 1
cinf2 = 0 #dias faltantes para a próxima conjunção inferior, referente à data 2
csup1 = 0 #dias faltantes para a próxima conjunção superior, referente à data 1
csup2 = 0 #dias faltantes para a próxima conjunção superior, referente à data 2
cmax1 = 0 #dias faltantes para o próximo brilho máximo, referente à data 1
cmax2 = 0 #dias faltantes para o próximo brilho máximo, referente à data 2

erro = 0 #se diferente de zero, não há o 'print' final, e sim a mensagem correspondente ao erro ou ao caso específico (conjunção)


#entrada inicial: opção de qual valor será a base para o cálculo dos demais valores
info = int(input("De qual informação você dispõe?"
"\n1) distância Terra-Vênus"
"\n2) ângulo Sol-Terra-Vênus"
"\n3) ângulo Sol-Vênus-Terra"
"\n4) ângulo Vênus-Sol-Terra"
"\n5) data - entre a última conjunção inferior (03 de junho de 2020) e a próxima (08 de janeiro de 2022)"
"\nDigite apenas o número correspondente: "))

#1) obtenção dos valores a partir da distância Terra-Vênus
if info == 1: 
    r = float(input("Entre com o valor da distância Terra-Vênus, em quilômetros: "))
    r = (r/(10**7)) #o 10^7 fica apenas no 'print', não sendo usado para os cálculos
    if r == 25.76: #a distância Terra-Vênus é igual à soma das distâncias Terra-Sol e Vênus-Sol, ou seja, há conjunção superior
        erro = "conjsup"
    elif r > 25.76: #a soma de 2 lados de um triângulo deve exceder o 3º lado! logo, r deve ser menor que 10.81+14.95
        erro = 2
    elif r == 4.14: #a distância Terra-Vênus é igual à 'Terra-Sol menos Vênus-Sol', ou seja, há conjunção inferior
        erro = "conjinf"
    elif r < 4.14: #a soma de 2 lados de um triângulo deve exceder o 3º lado! logo, r deve ser maior que 14.95-10.81
        erro = 2
    else: #4.14 < r < 25.76
        ψ = (math.acos((r**2+S**2-s**2)/(2*r*S))) #lei dos cossenos
        φ = (math.acos((r**2+s**2-S**2)/(2*r*s))) #lei dos cossenos
        θ = (math.acos((s**2+S**2-r**2)/(2*s*S))) #lei dos cossenos
        p = (0.5*(1+math.cos(φ)))*100 #fase em função de φ
        b = ((2*s*r+r**2+s**2-S**2)/r**3) #brilho em função de r
        t = (θ/0.010758878950649977) #aplicação da equação t = ((θ)/(2*π/584)); o t inicial é uma conjunção inferior
        t = round(t,0) #t em dias (número de dias anteriores ou posteriores à conjunção inferior)
        data1 = ultimacinf + timedelta(days = t) #possível data 1, calculada a partir da última conjunção inferior
        data2 = proximacinf - timedelta(days = t) #possível data 2, calculada a partir da próxima conjunção inferior
        cinf1 = (584-t)
        cinf2 = (t)
        csup1 = (292-t)
        csup2 = (292+t)
        if t < 36: 
            cmax1 = (36-t)
            cmax2 = (36+t)
            hoje = ""
        elif t > 36: 
            cmax1 = (584-36-36-t) 
            cmax2 = (t-36)
            hoje = ""
        else: #t = 36
            cmax1 = (584-36-36)
            cmax2 = (36+36)
            hoje = "Hoje é dia de brilho máximo! "

#2) obtenção dos valores a partir do ângulo Sol-Terra-Vênus
#neste caso, há duas configurações possíveis, e sua saída ('print') é separada das demais
elif info == 2: 
    ψ = float(input("Entre com o valor do ângulo Sol-Terra-Vênus, em radianos (até"
    "\n15 casas decimais): "))
    if ψ == 0: #há conjunção
        erro = "conj"
    elif ψ == 3.141592653589793: #o ângulo ψ não pode ser igual a 180° (3.141592653589793 rad)
        erro = 3.1
    elif ψ > 3.141592653589793: #o ângulo não pode ser maior que 180° (3.141592653589793 rad)
        erro = 3
    elif ψ > 0.8082463510273271: #a soma de 2 lados de um triângulo deve exceder o 3º lado! não é possível se maior que este valor
        erro = 4
    elif ψ < 0: 
        erro = 3.2
    else:
        #resolvendo equação de 2º grau para obter r via lei dos cossenos: 
        a = 1
        b = -2*S*(math.cos(ψ))
        c = S**2-s**2
        delta = ((b**2) - (4*a*c))
        ra = ((-b + delta**(1/2)) / (2*a)) #raiz 1, primeiro valor possível para r
        rb = ((-b - delta**(1/2)) / (2*a)) #raiz 2, segundo valor possível para r
        #obtenção dos demais valores para ambas as raízes (ra e rb): 
        φa = (math.acos((ra**2+s**2-S**2)/(2*ra*s))) #lei dos cossenos, para ra
        θa = (math.acos((s**2+S**2-ra**2)/(2*s*S))) #lei dos cossenos, para ra
        pa = (0.5*(1+math.cos(φa)))*100 #fase em função de φa
        ba = ((2*s*ra+ra**2+s**2-S**2)/ra**3) #brilho em função de ra
        ta = (θa/0.010758878950649977) #aplicação da equação t = ((θ)/(2*π/584)); o t inicial é uma conjunção inferior
        ta = round(ta,0) #t em dias (número de dias anteriores ou posteriores à conjunção inferior)
        data1a = ultimacinf + timedelta(days = ta) #possível data 1, calculada a partir da última conjunção inferior
        data2a = proximacinf - timedelta(days = ta) #possível data 2, calculada a partir da próxima conjunção inferior
        cinf1a = (584-ta)
        cinf2a = (ta)
        csup1a = (292-ta)
        csup2a = (292+ta)
        if ta < 36: 
            cmax1a = (36-ta)
            cmax2a = (36+ta)
            hojea = ""
        elif ta > 36: 
            cmax1a = (584-36-36-ta) 
            cmax2a = (ta-36)
            hojea = ""
        else: #t = 36
            cmax1a = (584-36-36)
            cmax2a = (36+36)
            hojea = "Hoje é dia de brilho máximo! "
        φb = (math.acos((rb**2+s**2-S**2)/(2*rb*s))) #lei dos cossenos, para rb
        θb = (math.acos((s**2+S**2-rb**2)/(2*s*S))) #lei dos cossenos, para rb
        pb = (0.5*(1+math.cos(φb)))*100 #fase em função de φb
        bb = ((2*s*rb+rb**2+s**2-S**2)/rb**3) #brilho em função de rb
        tb = (θb/0.010758878950649977) #aplicação da equação t = ((θ)/(2*π/584)); o t inicial é uma conjunção inferior
        tb = round(tb,0) #t em dias (número de dias anteriores ou posteriores à conjunção inferior)
        data1b = ultimacinf + timedelta(days = tb) #possível data 1, calculada a partir da última conjunção inferior
        data2b = proximacinf - timedelta(days = tb) #possível data 2, calculada a partir da próxima conjunção inferior
        cinf1b = (584-tb)
        cinf2b = (tb)
        csup1b = (292-tb)
        csup2b = (292+tb)
        if tb < 36: 
            cmax1b = (36-tb)
            cmax2b = (36+tb)
            hojeb = ""
        elif tb > 36: 
            cmax1b = (584-36-36-tb) 
            cmax2b = (tb-36)
            hojeb = ""
        else: #t = 36
            cmax1b = (584-36-36)
            cmax2b = (36+36)
            hojeb = "Hoje é dia de brilho máximo! "
        
#3) obtenção dos valores a partir do ângulo Sol-Vênus-Terra  
elif info == 3: 
    φ = float(input("Entre com o valor do ângulo Sol-Vênus-Terra, em radianos (até"
    "\n15 casas decimais, e 3.141592653589793 para π (180°)): "))
    if φ == 3.141592653589793: #há conjunção inferior
        erro = "conjinf"
    elif φ == 0: #há conjunção superior
        erro = "conjsup"
    elif φ > 3.141592653589793: #o ângulo não pode ser maior que 180° (3.141592653589793 rad)
        erro = 3
    elif φ < 0: 
        erro = 3.2
    else: 
        ψ = (math.asin(((math.sin(φ)*s)/S))) #lei dos senos
        θ = (3.141592653589793-φ-ψ) #terceiro ângulo
        r = ((s*math.sin(θ))/math.sin(ψ)) #lei dos senos
        p = (0.5*(1+math.cos(φ)))*100 #fase em função de φ
        b = ((2*s*r+r**2+s**2-S**2)/r**3) #brilho em função de r
        t = (θ/0.010758878950649977) #aplicação da equação t = ((θ)/(2*π/584)); o t inicial é uma conjunção inferior
        t = round(t,0) #t em dias (número de dias anteriores ou posteriores à conjunção inferior)
        data1 = ultimacinf + timedelta(days = t) #possível data 1, calculada a partir da última conjunção inferior
        data2 = proximacinf - timedelta(days = t) #possível data 2, calculada a partir da próxima conjunção inferior
        cinf1 = (584-t)
        cinf2 = (t)
        csup1 = (292-t)
        csup2 = (292+t)
        if t < 36: 
            cmax1 = (36-t)
            cmax2 = (36+t)
            hoje = ""
        elif t > 36: 
            cmax1 = (584-36-36-t) 
            cmax2 = (t-36)
            hoje = ""
        else: #t = 36
            cmax1 = (584-36-36)
            cmax2 = (36+36)
            hoje = "Hoje é dia de brilho máximo! "
            
#4) obtenção dos valores a partir do ângulo Vênus-Sol-Terra    
elif info == 4: 
    θ = float(input("Entre com o valor do ângulo Vênus-Sol-Terra, em radianos (até"
    "\n15 casas decimais, e 3.141592653589793 para π (180°)): "))
    if θ == 3.141592653589793: #há conjunção superior
        erro = "conjsup"
    elif θ == 0: #há conjunção inferior
        erro = "conjinf"
    elif θ > 3.141592653589793: #o ângulo não pode ser maior que 180° (3.141592653589793 rad)
        erro = 3
    elif θ < 0: 
        erro = 3.2
    else: 
        r = (math.sqrt(s**2+S**2-2*s*S*(math.cos(θ)))) #lei dos cossenos
        ψ = (math.acos((S**2+r**2-s**2)/(2*S*r))) #lei dos cossenos
        φ = (math.acos((r**2+s**2-S**2)/(2*r*s))) #lei dos cossenos
        p = (0.5*(1+math.cos(φ)))*100 #fase em função de φ
        b = ((2*s*r+r**2+s**2-S**2)/r**3) #brilho em função de r
        t = (θ/0.010758878950649977) #aplicação da equação t = ((θ)/(2*π/584)); o t inicial é uma conjunção inferior
        t = round(t,0) #t em dias (número de dias anteriores ou posteriores à conjunção inferior)
        data1 = ultimacinf + timedelta(days = t) #possível data 1, calculada a partir da última conjunção inferior
        data2 = proximacinf - timedelta(days = t) #possível data 2, calculada a partir da próxima conjunção inferior
        cinf1 = (584-t)
        cinf2 = (t)
        csup1 = (292-t)
        csup2 = (292+t)
        if t < 36: 
            cmax1 = (36-t)
            cmax2 = (36+t)
            hoje = ""
        elif t > 36: 
            cmax1 = (584-36-36-t) 
            cmax2 = (t-36)
            hoje = ""
        else: #t = 36
            cmax1 = (584-36-36)
            cmax2 = (36+36)
            hoje = "Hoje é dia de brilho máximo! "

#5) obtenção dos valores a partir de data
elif info==5: 
    userAno = int(input("Insira o ano: "))
    userMes = int(input("Insira o mês: "))
    userDia = int(input("Insira o dia: "))
    userData = datetime.date(userAno, userMes, userDia)
    if userData > proximacinf: 
        erro = 5
    elif userData == proximacinf: 
        erro = "conjinf_prox"
    elif userData < ultimacinf: 
        erro = 5
    elif userData == ultimacinf:
        erro = "conjinf_ult"
    elif userData == datacsup:
        erro = "conjsup_data"
    else: #ultimacinf < userData < proximacinf, exceto pela conjunção superior (caso particular)
        t = userData - ultimacinf
        t = t.days
        if t < 292: 
            dias = t
        else: #t > 292: (o caso onde é igual já foi excluído após o input da data)
            dias = (584-t)
        θ = 0.010758878950649977*dias #aplicação da equação t = ((θ)*(2*π/584))
                          #há alguma diferença, devido ao arredondamento dos dias
                          #o 584 seria alterado para 579 para manter o arredondamento de referência (de 36.3 para 36)
        r = (math.sqrt(s**2+S**2-2*s*S*(math.cos(θ)))) #lei dos cossenos
        ψ = (math.acos((S**2+r**2-s**2)/(2*S*r))) #lei dos cossenos
        φ = (math.acos((r**2+s**2-S**2)/(2*r*s))) #lei dos cossenos
        p = (0.5*(1+math.cos(φ)))*100 #fase em função de φ
        b = ((2*s*r+r**2+s**2-S**2)/r**3) #brilho em função de r
        data = userData
        cinf = (584-t)
        if t < 292: 
            csup = (292-t)
        else: #t > 292 (o caso onde é igual já foi excluído após o input da data)
            csup = (876-t)
        if t == 36: 
            cmax = 512
            hoje = "Hoje é dia de brilho máximo! "
        elif t == 548: 
            cmax = 72
            hoje = "Hoje é dia de brilho máximo! "
        elif t < 36: 
            cmax = (36-t)
            hoje = ""
        else: #t > 36:
            cmax = (584-36-36-t) 
            hoje = ""

else: #número inválido como opção
    erro = 1


#saídas para o usuário: 

if erro == 1:
    print("\n\nOpção inválida! Reinicie o programa")

elif erro == 2: 
    print("\n\nNão é possível criar um triângulo com esta medida combinada às duas medidas conhecidas."
    "\nA soma de 2 lados de um triângulo deve exceder o 3º lado. Reinicie o programa")

elif erro == 3: 
    print("\n\nEntrada inválida! Ângulo não pode ser superior a 180° (3.141592653589793 rad). Reinicie o programa")

elif erro == 3.1: 
    print("\n\nEntrada inválida! O ângulo ψ não pode ser igual a 180° (3.141592653589793 rad). Reinicie o programa")

elif erro == 3.2: 
    print("\n\nEntrada inválida! O ângulo não pode ser negativo. Reinicie o programa")

elif erro == 4: 
    print("\n\nNão é possível criar um triângulo com este ângulo combinado às duas medidas conhecidas."
    "\nA soma de 2 lados de um triângulo deve exceder o 3º lado. Reinicie o programa")

elif erro ==5: 
    print("\n\nData fora do intervalo. Reinicie o programa")
    
elif erro == "conj": 
    print("\n\nVênus está em conjunção. Há dois cenários possíveis: "
    "\n"
    "\nCenário 1: Vênus está em conjunção superior. "
    "\nA distância Vênus-Sol é: ",s,"*10^7 km"
    "\nA distância Terra-Sol é: ",S,"*10^7 km"
    "\nA distância Terra-Vênus é: ",25.76,"*10^7 km"
    "\nOs ângulos são 0 ou π rad (180°), e os cálculos da fase e do brilho não "
    "\nse aplicam (Vênus não está visível nos parâmetros deste modelo)"
    "\n"
    "\nO programa considera apenas datas entre a última conjunção inferior (junho"
    "\nde 2020) e a próxima (janeiro de 2022)."
    "\n- Assim, a única data possível é 2021-03-22 (formato aaaa-mm-dd)"
    "\nFaltam 292 dias para a próxima conjunção inferior."
    "\nFaltam 584 dias para a próxima conjunção superior."
    "\nFaltam 256 dias para o próximo brilho máximo."
    "\n"
    "\nCenário 2: Vênus está em conjunção inferior. "
    "\nA distância Vênus-Sol é: ",s,"*10^7 km"
    "\nA distância Terra-Sol é: ",S,"*10^7 km"
    "\nA distância Terra-Vênus é: ",4.14,"*10^7 km"
    "\nOs ângulos são 0 ou π rad (180°), e os cálculos da fase e do brilho não "
    "\nse aplicam (Vênus não está visível nos parâmetros deste modelo)"
    "\n"
    "\nO programa considera apenas datas entre a última conjunção inferior (junho"
    "\nde 2020) e a próxima (janeiro de 2022)."
    "\n- Assim, as possíveis datas são: 2020-06-03 e 2022-01-08 (formato aaaa-mm-dd)"
    "\nFaltam 584 dias para a próxima conjunção inferior."
    "\nFaltam 292 dias para a próxima conjunção superior."
    "\nFaltam 36 dias para o próximo brilho máximo.",
    sep='')
    
elif erro == "conjsup": 
    print("\n\nVênus está em conjunção superior. "
    "\nA distância Vênus-Sol é: ",s,"*10^7 km"
    "\nA distância Terra-Sol é: ",S,"*10^7 km"
    "\nA distância Terra-Vênus é: ",25.76,"*10^7 km"
    "\nOs ângulos são 0 ou π rad (180°), e os cálculos da fase e do brilho não "
    "\nse aplicam (Vênus não está visível nos parâmetros deste modelo)"
    "\n"
    "\nO programa considera apenas datas entre a última conjunção inferior (junho"
    "\nde 2020) e a próxima (janeiro de 2022)."
    "\n- Assim, a única data possível é 2021-03-22 (formato aaaa-mm-dd)"
    "\nFaltam 292 dias para a próxima conjunção inferior."
    "\nFaltam 584 dias para a próxima conjunção superior."
    "\nFaltam 256 dias para o próximo brilho máximo.",
    sep='')

elif erro == "conjinf": 
    print("\n\nVênus está em conjunção inferior. "
    "\nA distância Vênus-Sol é: ",s,"*10^7 km"
    "\nA distância Terra-Sol é: ",S,"*10^7 km"
    "\nA distância Terra-Vênus é: ",4.14,"*10^7 km"
    "\nOs ângulos são 0 ou π rad (180°), e os cálculos da fase e do brilho não "
    "\nse aplicam (Vênus não está visível nos parâmetros deste modelo)"
    "\n"
    "\nO programa considera apenas datas entre a última conjunção inferior (junho"
    "\nde 2020) e a próxima (janeiro de 2022)."
    "\n- Assim, as possíveis datas são: 2020-06-03 e 2022-01-08 (formato aaaa-mm-dd)"
    "\nFaltam 584 dias para a próxima conjunção inferior."
    "\nFaltam 292 dias para a próxima conjunção superior."
    "\nFaltam 36 dias para o próximo brilho máximo.",
    sep='')

elif erro == "conjinf_prox": 
    print("\n\nVênus está em conjunção inferior. "
    "\nA distância Vênus-Sol é: ",s,"*10^7 km"
    "\nA distância Terra-Sol é: ",S,"*10^7 km"
    "\nA distância Terra-Vênus é: ",4.14,"*10^7 km"
    "\nOs ângulos são 0 ou π rad (180°), e os cálculos da fase e do brilho não "
    "\nse aplicam (Vênus não está visível nos parâmetros deste modelo)"
    "\n"
    "\nO programa considera apenas datas entre a última conjunção inferior (junho"
    "\nde 2020) e a próxima (janeiro de 2022)."
    "\n- Data inserida: 2022-01-08 (formato aaaa-mm-dd)"
    "\nFaltam 584 dias para a próxima conjunção inferior."
    "\nFaltam 292 dias para a próxima conjunção superior."
    "\nFaltam 36 dias para o próximo brilho máximo.",
    sep='')

elif erro == "conjinf_ult": 
    print("\n\nVênus está em conjunção inferior. "
    "\nA distância Vênus-Sol é: ",s,"*10^7 km"
    "\nA distância Terra-Sol é: ",S,"*10^7 km"
    "\nA distância Terra-Vênus é: ",4.14,"*10^7 km"
    "\nOs ângulos são 0 ou π rad (180°), e os cálculos da fase e do brilho não "
    "\nse aplicam (Vênus não está visível nos parâmetros deste modelo)"
    "\n"
    "\nO programa considera apenas datas entre a última conjunção inferior (junho"
    "\nde 2020) e a próxima (janeiro de 2022)."
    "\n- Data inserida: 2020-06-03 (formato aaaa-mm-dd)"
    "\nFaltam 584 dias para a próxima conjunção inferior."
    "\nFaltam 292 dias para a próxima conjunção superior."
    "\nFaltam 36 dias para o próximo brilho máximo.",
    sep='')

elif erro == "conjsup_data": 
    print("\n\nVênus está em conjunção superior. "
    "\nA distância Vênus-Sol é: ",s,"*10^7 km"
    "\nA distância Terra-Sol é: ",S,"*10^7 km"
    "\nA distância Terra-Vênus é: ",25.76,"*10^7 km"
    "\nOs ângulos são 0 ou π rad (180°), e os cálculos da fase e do brilho não "
    "\nse aplicam (Vênus não está visível nos parâmetros deste modelo)"
    "\n"
    "\nO programa considera apenas datas entre a última conjunção inferior (junho"
    "\nde 2020) e a próxima (janeiro de 2022)."
    "\n- Data inserida: 2021-03-22 (formato aaaa-mm-dd)"
    "\nFaltam 292 dias para a próxima conjunção inferior."
    "\nFaltam 584 dias para a próxima conjunção superior."
    "\nFaltam 256 dias para o próximo brilho máximo.",
    sep='')
    
else:  #erro == 0, ou seja, é de fato formado um triângulo
    if info == 5: #apenas uma possibilidade de data, visto que a data foi a informação inserida
        print("\n\nA distância Vênus-Sol é: ",s,"*10^7 km"
        "\nA distância Terra-Sol é: ",S,"*10^7 km"
        "\nA distância Terra-Vênus é: ",r,"*10^7 km"
        "\nO ângulo Sol-Terra-Vênus é: ",ψ," rad (",math.degrees(ψ),"°)"
        "\nO ângulo Sol-Vênus-Terra é: ",φ," rad (",math.degrees(φ),"°)"
        "\nO ângulo Vênus-Sol-Terra é: ",θ," rad (",math.degrees(θ),"°)"
        "\nFase: ",p,"%"
        "\nBrilho: ",b,"*10^(-14)*K, onde K = constante"
        "\n",
        sep='')
        print("O programa considera apenas datas entre a última conjunção inferior (junho"
        "\nde 2020) e a próxima (janeiro de 2022)."
        "\n- A data inserida foi: ", data," (formato aaaa-mm-dd)"
        "\nFaltam ",cinf," dias para a próxima conjunção inferior;"
        "\nFaltam ",csup," dias para a próxima conjunção superior;","\n",
        hoje,"Faltam ",cmax," dias para o próximo brilho máximo."
        "\n",
        sep='')
        
    elif info != 2: #o caso 2 possui duas configurações, e sua saída é separada das demais
        print("\n\nA distância Vênus-Sol é: ",s,"*10^7 km"
        "\nA distância Terra-Sol é: ",S,"*10^7 km"
        "\nA distância Terra-Vênus é: ",r,"*10^7 km"
        "\nO ângulo Sol-Terra-Vênus é: ",ψ," rad (",math.degrees(ψ),"°)"
        "\nO ângulo Sol-Vênus-Terra é: ",φ," rad (",math.degrees(φ),"°)"
        "\nO ângulo Vênus-Sol-Terra é: ",θ," rad (",math.degrees(θ),"°)"
        "\nFase: ",p,"%"
        "\nBrilho: ",b,"*10^(-14)*K, onde K = constante"
        "\n",
        sep='')
        print("O programa considera apenas datas entre a última conjunção inferior (junho"
        "\nde 2020) e a próxima (janeiro de 2022)."
        "\nAssim, há duas possíveis datas com base nessa informação: "
        "\n- Data 1: ",data1," (formato aaaa-mm-dd)"
        "\nFaltam ",cinf1," dias para a próxima conjunção inferior;"
        "\nFaltam ",csup1," dias para a próxima conjunção superior;","\n",
        hoje,"Faltam ",cmax1," dias para o próximo brilho máximo."
        "\n- Data 2: ",data2," (formato aaaa-mm-dd)"
        "\nFaltam ",cinf2," dias para a próxima conjunção inferior;"
        "\nFaltam ",csup2," dias para a próxima conjunção superior;","\n",
        hoje,"Faltam ",cmax2," dias para o próximo brilho máximo."
        "\n",
        sep='')

    else: #info == 2; o caso 2 possui duas configurações, e sua saída é separada das demais
        print("\n\nHá 2 cenários possíveis. "
        "\n"
        "\n Cenário 1: " 
        "\nA distância Vênus-Sol é: ",s,"*10^7 km"
        "\nA distância Terra-Sol é: ",S,"*10^7 km"
        "\nA distância Terra-Vênus é: ",ra,"*10^7 km"
        "\nO ângulo Sol-Terra-Vênus é: ",ψ," rad (",math.degrees(ψ),"°)"
        "\nO ângulo Sol-Vênus-Terra é: ",φa," rad (",math.degrees(φa),"°)"
        "\nO ângulo Vênus-Sol-Terra é: ",θa," rad (",math.degrees(θa),"°)"
        "\nFase: ",pa,"%"
        "\nBrilho: ",ba,"*10^(-14)*K, onde K = constante"
        "\n"
        "\nO programa considera apenas datas entre a última conjunção inferior (junho"
        "\nde 2020) e a próxima (janeiro de 2022)."
        "\nAssim, há duas possíveis datas com base na informação do cenário 1: "
        "\n- Data 1: ",data1a," (formato aaaa-mm-dd)"
        "\nFaltam ",cinf1a," dias para a próxima conjunção inferior;"
        "\nFaltam ",csup1a," dias para a próxima conjunção superior;","\n",
        hojea,"Faltam ",cmax1a," dias para o próximo brilho máximo."
        "\n- Data 2: ",data2a," (formato aaaa-mm-dd)"
        "\nFaltam ",cinf2a," dias para a próxima conjunção inferior;"
        "\nFaltam ",csup2a," dias para a próxima conjunção superior;","\n",
        hojea,"Faltam ",cmax2a," dias para o próximo brilho máximo."
        "\n"
        "\n Cenário 2: "
        "\nA distância Vênus-Sol é: ",s,"*10^7 km"
        "\nA distância Terra-Sol é: ",S,"*10^7 km"
        "\nA distância Terra-Vênus é: ",rb,"*10^7 km"
        "\nO ângulo Sol-Terra-Vênus é: ",ψ," rad (",math.degrees(ψ),"°)"
        "\nO ângulo Sol-Vênus-Terra é: ",φb," rad (",math.degrees(φb),"°)"
        "\nO ângulo Vênus-Sol-Terra é: ",θb," rad (",math.degrees(θb),"°)"
        "\nFase: ",pb,"%"
        "\nBrilho: ",bb,"*10^(-14)*K, onde K = constante"
        "\n"
        "\nO programa considera apenas datas entre a última conjunção inferior (junho"
        "\nde 2020) e a próxima (janeiro de 2022)."
        "\nAssim, há duas possíveis datas com base na informação do cenário 1: "
        "\n- Data 1: ",data1b," (formato aaaa-mm-dd)"
        "\nFaltam ",cinf1b," dias para a próxima conjunção inferior;"
        "\nFaltam ",csup1b," dias para a próxima conjunção superior;","\n",
        hojeb,"Faltam ",cmax1b," dias para o próximo brilho máximo."
        "\n- Data 2: ",data2b," (formato aaaa-mm-dd)"
        "\nFaltam ",cinf2b," dias para a próxima conjunção inferior;"
        "\nFaltam ",csup2b," dias para a próxima conjunção superior;","\n",
        hojeb,"Faltam ",cmax2b," dias para o próximo brilho máximo."
        "\n",
        sep='')
