# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

# pegar o número da sorte de cada apostador
# Inserir um par key/value para cada apostador
lucky_numbers={
    'Luiz': 35,
    'Aguinaldo': 152,
    'Patricia': 20,
    'Nathalia': 56,
    'Camila': 30,
    'Pedro': 98,
    'Gabriel': 13,
    'Enzo': 24
}
sum_lucky_numbers = np.array(list(lucky_numbers.values())).sum()
rng = np.random.default_rng(sum_lucky_numbers)
# gera a sequência aleatória de 60 números com base na soma do lucky number
numbers = rng.choice(np.arange(1,61), size=(10,6), replace=False)
for x, y in enumerate(numbers):
    numbers[x] = np.sort(y)

# gera índices e header do dataframe
jogos = [str(x) + "º" for x in np.linspace(1, 10, num=10, dtype=np.int32, axis=0)]
headers = [
    'dez01',
    'dez02',
    'dez03',
    'dez04',
    'dez05',
    'dez06']

megasena = pd.DataFrame(numbers, index=jogos, columns=headers)
print(megasena.to_markdown(tablefmt="grid"))
print(megasena.to_html('teste.html'))