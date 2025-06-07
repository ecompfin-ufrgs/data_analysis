"""
Módulo datareader
Descrição: Este módulo oferece funções para leitura de dados de receitas da previdência 2024 no RS
Autor: Nelson Seixas dos Santos
Data: 06/06/2025
Versão: 0.0.1
"""

# importação de pacotes

import numpy as np
import pandas as pd
def reader(url="https://dados.tce.rs.gov.br/dados/municipal/prev-receitas/2024.csv"):
    dados = pd.read_csv(url)
    return dados

