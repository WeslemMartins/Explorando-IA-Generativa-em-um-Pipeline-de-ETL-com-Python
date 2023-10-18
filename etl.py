# etl.py

import pandas as pd
import openai

# Configure a chave de API da OpenAI
openai.api_key = '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'

# Função para extração de dados
def extract_data(csv_path):
    data = pd.read_csv(csv_path)
    return data

# Função para transformação de dados usando a API da OpenAI
def transform_data(data):
    for name in data['nome']:
        prompt = f"Gere uma saudação para {name}."
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50
        )
        greeting = response['choices'][0]['text'].strip()
        print(f"Saudação para {name}: {greeting}")

# Função principal para executar o ETL
def main():
    # Caminho do arquivo CSV
    csv_path = 'dados.csv'

    # Extração de dados
    raw_data = extract_data(csv_path)

    # Transformação de dados usando a API da OpenAI
    transform_data(raw_data)

if __name__ == '__main__':
    main()
