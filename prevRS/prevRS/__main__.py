"""
Aplicativo prevRS
Descrição:
Este aplicativo analisa os dados da receita previdenciária do RS em 2024.
Autor: Nelson Seixas dos Santos
Data: 06/06/2025
Versão: 0.0.1
"""

# Importação dos módulos da aplicação
import datareader
import loader
import transformer.cleaner as cleaner
import transformer.explorer as explorer

def main():
    data = datareader.reader()
    data_cleaned = cleaner.double_cleaner(cleaner.miss_cleaner(data))
    media = explorer.calcula_media(data_cleaned)
    desvpad = explorer.calcula_desvio_padrao(data_cleaned)
    explorer.plotadora(data_cleaned)

if __name__ == "__main__":
    main()

