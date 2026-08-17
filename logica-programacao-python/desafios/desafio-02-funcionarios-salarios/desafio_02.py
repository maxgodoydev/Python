#Desafio_2
# 28/06/2026

empresa = [ 
           
           {"nome": "Amanda",
            "Salário": 2_500,
            "moeda": "R$", 
            "ativo": True},
             
            {"nome": "Patrícia", 
             "Salário": 3_600,
             "moeda": "R$",
             "ativo": False},
             
            {"nome": "Carlos", 
             "Salário": 3_200,
             "moeda": "R$", 
             "ativo":False},
             
            {"nome": "Fernanda", 
            "Salário": 4_100,
            "moeda": "R$", 
            "ativo": True},
            
            {"nome": "João", 
             "Salário": 2_800,
             "moeda": "R$", 
             "ativo":True}
          ]

total_salarios = 0
quantidade_ativos = 0
quantidade_inativos = 0

#1
for funcionario in empresa:
    if funcionario["ativo"]:
        total_salarios += funcionario["Salário"]
        
#2
for funcionario in empresa:
    if funcionario["ativo"]:
        quantidade_ativos += 1
    else:
        quantidade_inativos += 1
        
#3
for funcionario in empresa:
    if funcionario["ativo"]:
        status = "Ativo"
    else:
        status = "Inativo"
    print(funcionario["nome"], "--->", status)


print("Total: ", total_salarios)
print("Quantidade de funcionários ativos: ", quantidade_ativos)
print("Quantidade de funcionários Inativos: ", quantidade_inativos)

                