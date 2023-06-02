def selecionar_cargo(area, pretensao_salarial):
    grafo = {
        0: {"Cargo": "Desenvolvedor Junior", "salario": 3500},
        1: {"Cargo": "Desenvolvedor Pleno", "salario": 7000},
        2: {"Cargo": "Desenvolvedor Senior", "salario": 10000},
        3: {"Cargo": "Gerente de Projeto", "salario": 15000},
        4: {"Cargo": "Auxiliar de Logastica", "salario": 1500},
        5: {"Cargo": "Assistente de Logistica", "salario": 2500},
        6: {"Cargo": "Analista de Logistica", "salario": 5000},
        7: {"Cargo": "Coordenador de Logistica", "salario": 8000}
    }
    
    if area == "Tecnologia":
        cargos = {"Desenvolvedor Junior": 0, "Desenvolvedor Pleno": 1, "Desenvolvedor Senior": 2, "Gerente de Projeto": 3}
    elif area == "Logistica":
        cargos = {"Auxiliar de Logistica": 4, "Assistente de Logistica": 5, "Analista de Logistica": 6, "Coordenador de Logistica": 7}
    else:
        return "area invalida"
    
    cargos_filtrados = {k: v for k, v in cargos.items() if grafo[v]["salario"] <= pretensao_salarial}
    
    if len(cargos_filtrados) == 0:
        return "Nao ha cargos disponaveis na area de {} com a pretensao salarial de R${:.2f}".format(area, pretensao_salarial)
    
    cargo_escolhido = max(cargos_filtrados, key=cargos_filtrados.get)
    salario_cargo = grafo[cargos[cargo_escolhido]]["salario"]
    
    return "O cargo mais apropriado na area de {} com a pretensao salarial de R${:.2f} � {} (salario: R${:.2f})".format(area, pretensao_salarial, cargo_escolhido, salario_cargo)


area = input("Qual area voce deseja trabalhar? (Tecnologia ou Logistica): ")
pretensao_salarial = float(input("Qual e a sua pretensao salarial? R$"))
print(selecionar_cargo(area, pretensao_salarial))


