import math
import datetime
from datetime import date
from datetime import timedelta

s = 10.81
S = 14.95
r = 0
ψ = 0
φ = 0
θ = 0
p = 0
b = 0

ultimacinf = date(2020, 6, 3) 
proximacinf = date(2022, 1, 8)
datacsup = date(2021, 3, 22)

t = 0
data1 = 0
data2 = 0
cinf1 = 0
cinf2 = 0
csup1 = 0
csup2 = 0
cmax1 = 0
cmax2 = 0

erro = 0

info = int(input("De qual informação você dispõe?"
"\n1) distância Terra-Vênus"
"\n2) ângulo Sol-Terra-Vênus"
"\n3) ângulo Sol-Vênus-Terra"
"\n4) ângulo Vênus-Sol-Terra"
"\n5) data - entre a última conjunção inferior (03 de junho de 2020) e a próxima (08 de janeiro de 2022)"
"\nDigite apenas o número correspondente: "))

if info == 1: 
    r = float(input("Entre com o valor da distância Terra-Vênus, em quilômetros: "))
    r = (r/(10**7))
    if r == 25.76:
        erro = "conjsup"
    elif r > 25.76:
        erro = 2
    elif r == 4.14:
        erro = "conjinf"
    elif r < 4.14:
        erro = 2
    else:
        ψ = (math.acos((r**2+S**2-s**2)/(2*r*S)))
        φ = (math.acos((r**2+s**2-S**2)/(2*r*s)))
        θ = (math.acos((s**2+S**2-r**2)/(2*s*S)))
        p = (0.5*(1+math.cos(φ)))*100
        b = ((2*s*r+r**2+s**2-S**2)/r**3)
        t = (θ/0.010758878950649977)
        t = round(t,0) 
        data1 = ultimacinf + timedelta(days = t)
        data2 = proximacinf - timedelta(days = t)
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

elif info == 2: 
    ψ = float(input("Entre com o valor do ângulo Sol-Terra-Vênus, em radianos (até"
    "\n15 casas decimais): "))
    if ψ == 0:
        erro = "conj"
    elif ψ == 3.141592653589793:
        erro = 3.1
    elif ψ > 3.141592653589793:
        erro = 3
    elif ψ > 0.8082463510273271:
        erro = 4
    elif ψ < 0: 
        erro = 3.2
    else:
        a = 1
        b = -2*S*(math.cos(ψ))
        c = S**2-s**2
        delta = ((b**2) - (4*a*c))
        ra = ((-b + delta**(1/2)) / (2*a))
        rb = ((-b - delta**(1/2)) / (2*a))
        φa = (math.acos((ra**2+s**2-S**2)/(2*ra*s)))
        θa = (math.acos((s**2+S**2-ra**2)/(2*s*S)))
        pa = (0.5*(1+math.cos(φa)))*100
        ba = ((2*s*ra+ra**2+s**2-S**2)/ra**3)
        ta = (θa/0.010758878950649977)
        ta = round(ta,0)
        data1a = ultimacinf + timedelta(days = ta) 
        data2a = proximacinf - timedelta(days = ta)
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
        else:
            cmax1a = (584-36-36)
            cmax2a = (36+36)
            hojea = "Hoje é dia de brilho máximo! "
        φb = (math.acos((rb**2+s**2-S**2)/(2*rb*s)))
        θb = (math.acos((s**2+S**2-rb**2)/(2*s*S)))
        pb = (0.5*(1+math.cos(φb)))*100
        bb = ((2*s*rb+rb**2+s**2-S**2)/rb**3)
        tb = (θb/0.010758878950649977)
        tb = round(tb,0)
        data1b = ultimacinf + timedelta(days = tb)
        data2b = proximacinf - timedelta(days = tb)
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
        else:
            cmax1b = (584-36-36)
            cmax2b = (36+36)
            hojeb = "Hoje é dia de brilho máximo! "
        
elif info == 3: 
    φ = float(input("Entre com o valor do ângulo Sol-Vênus-Terra, em radianos (até"
    "\n15 casas decimais, e 3.141592653589793 para π (180°)): "))
    if φ == 3.141592653589793:
        erro = "conjinf"
    elif φ == 0:
        erro = "conjsup"
    elif φ > 3.141592653589793:
        erro = 3
    elif φ < 0: 
        erro = 3.2
    else: 
        ψ = (math.asin(((math.sin(φ)*s)/S)))
        θ = (3.141592653589793-φ-ψ)
        r = ((s*math.sin(θ))/math.sin(ψ))
        p = (0.5*(1+math.cos(φ)))*100
        b = ((2*s*r+r**2+s**2-S**2)/r**3)
        t = (θ/0.010758878950649977)
        t = round(t,0)
        data1 = ultimacinf + timedelta(days = t)
        data2 = proximacinf - timedelta(days = t)
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
        else:
            cmax1 = (584-36-36)
            cmax2 = (36+36)
            hoje = "Hoje é dia de brilho máximo! "
            
elif info == 4: 
    θ = float(input("Entre com o valor do ângulo Vênus-Sol-Terra, em radianos (até"
    "\n15 casas decimais, e 3.141592653589793 para π (180°)): "))
    if θ == 3.141592653589793:
        erro = "conjsup"
    elif θ == 0:
        erro = "conjinf"
    elif θ > 3.141592653589793:
        erro = 3
    elif θ < 0: 
        erro = 3.2
    else: 
        r = (math.sqrt(s**2+S**2-2*s*S*(math.cos(θ))))
        ψ = (math.acos((S**2+r**2-s**2)/(2*S*r)))
        φ = (math.acos((r**2+s**2-S**2)/(2*r*s)))
        p = (0.5*(1+math.cos(φ)))*100
        b = ((2*s*r+r**2+s**2-S**2)/r**3)
        t = (θ/0.010758878950649977)
        t = round(t,0)
        data1 = ultimacinf + timedelta(days = t)
        data2 = proximacinf - timedelta(days = t)
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
        else:
            cmax1 = (584-36-36)
            cmax2 = (36+36)
            hoje = "Hoje é dia de brilho máximo! "

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
    else:
        t = userData - ultimacinf
        t = t.days
        if t < 292: 
            dias = t
        else:
            dias = (584-t)
        θ = 0.010758878950649977*dias
                          
                          
        r = (math.sqrt(s**2+S**2-2*s*S*(math.cos(θ))))
        ψ = (math.acos((S**2+r**2-s**2)/(2*S*r)))
        φ = (math.acos((r**2+s**2-S**2)/(2*r*s)))
        p = (0.5*(1+math.cos(φ)))*100 
        b = ((2*s*r+r**2+s**2-S**2)/r**3)
        data = userData
        cinf = (584-t)
        if t < 292: 
            csup = (292-t)
        else:
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
        else:
            cmax = (584-36-36-t) 
            hoje = ""

else:
    erro = 1


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
    
else:
    if info == 5:
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
        
    elif info != 2:
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

    else:
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