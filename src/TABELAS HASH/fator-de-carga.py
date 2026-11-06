# ====================================== FATOR DE CARGA ======================================

def fator_de_carga(demandas_kw=None, energia_kwh=None, demanda_max_kw=None, horas=None):
    """
    Calcula o fator de carga (valor entre 0 e 1).

    Uso 1: a partir de uma série de demandas (ex.: leituras a cada 15 min)
        fator_de_carga(demandas_kw=[...])

    Uso 2: a partir da energia consumida
        fator_de_carga(energia_kwh=..., demanda_max_kw=..., horas=...)
    """
    if demandas_kw is not None:
        if len(demandas_kw) == 0:
            raise ValueError("A lista de demandas não pode ser vazia.")
        demanda_media = sum(demandas_kw) / len(demandas_kw)
        demanda_max = max(demandas_kw)
    elif None not in (energia_kwh, demanda_max_kw, horas):
        demanda_media = energia_kwh / horas
        demanda_max = demanda_max_kw
    else:
        raise ValueError("Informe 'demandas_kw' ou (energia_kwh, demanda_max_kw, horas).")

    if demanda_max <= 0:
        raise ValueError("A demanda máxima deve ser maior que zero.")

    return demanda_media / demanda_max


# Exemplo 1: série de demandas (kW)
demandas = [120, 150, 180, 200, 170, 140, 110, 90]
fc = fator_de_carga(demandas_kw=demandas)
print(f"Fator de carga: {fc:.3f} ({fc:.1%})")

# Exemplo 2: energia mensal (30 dias = 720 h)
fc = fator_de_carga(energia_kwh=72_000, demanda_max_kw=200, horas=720)
print(f"Fator de carga: {fc:.3f} ({fc:.1%})")