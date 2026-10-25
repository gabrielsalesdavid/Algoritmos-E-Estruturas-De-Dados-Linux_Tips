# ====================================== CASO RECURSIVO ======================================

departamento_ti = {
    "nome": "Divisão de TI",
    "Faturamento": 1000.0,
    "Subdepartamentos": [
        {
            "nome": "Suporte Técnico",
            "Faturamento": 500.0,
            "Subdepartamentos": []
        },
        {
            "nome": "Desenvolvimento de Software",
            "Faturamento": 300.0,
            "Subdepartamentos": [
                {
                    "nome": "Frontend",
                    "Faturamento": 150.0,
                    "Subdepartamentos": []
                },
                {
                    "nome": "Backend",
                    "Faturamento": 200.0,
                    "Subdepartamentos": []
                }
            ]
        }
    ]
}

def calcular_faturamento(departamento):
    faturamento_total = departamento["Faturamento"]
    for subdepartamento in departamento["Subdepartamentos"]:
        faturamento_total += calcular_faturamento(subdepartamento)
    return faturamento_total

print(calcular_faturamento(departamento_ti))

def nome_do_depto_maior_gasto(departamento):
    maior_gasto = departamento["Faturamento"]
    nome_maior_gasto = departamento["nome"]

    for subdepartamento in departamento["Subdepartamentos"]:
        subdepartamento_maior_gasto, subdepartamento_nome = nome_do_depto_maior_gasto(subdepartamento)
        if subdepartamento_maior_gasto > maior_gasto:
            maior_gasto = subdepartamento_maior_gasto
            nome_maior_gasto = subdepartamento_nome

    return maior_gasto, nome_maior_gasto

print(nome_do_depto_maior_gasto(departamento_ti))