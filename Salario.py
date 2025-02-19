def calcular_porcentagem(cargo, salario):
    if cargo == 'senior':
        porcentagem = 0.20
    elif cargo == 'pleno':
        porcentagem = 0.15
    elif cargo == 'junior':
        porcentagem = 0.10
    else:
        return "Cargo inválido"
    
    aumento = salario * porcentagem
    novo_salario = salario + aumento
    
    return novo_salario


salario_atual = float(input("Digite o salário atual: R$ "))
cargo = input("Digite o cargo (senior, pleno ou junior): ").lower()

salario_com_aumento = calcular_porcentagem(cargo, salario_atual)

if isinstance(salario_com_aumento, float):
    print(f"O novo salário com o aumento é: R$ {salario_com_aumento:.2f}")
else:
    print(salario_com_aumento)
