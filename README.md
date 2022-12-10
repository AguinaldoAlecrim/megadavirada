## Descrição
Este script APENAS gera uma combinação dos 60 (sessenta) números possíveis de serem sorteados na "Mega da VIRADA"™, combinando-os em 10(dez) sequências de 6(seis) números cada. Com isso, é certo que os números sorteados estarão dentro da matriz gerada. O grande problema é garantir um resultado em que os referidos 6(seis) estejam em uma linha da tabela.
## Ambiente virtual
É altamente recomendado o uso de um ambiente virtual para se brincar com esse projeto.
### Criando o ambiente:
Crie um diretório com um nome qualquer e, dentro dele, execute 
```cmd 
    python -m venv .
```
Depois ative o ambiente. Ex:
```cmd
    cd <meu_diretorio_qualquer>
    python -m venv .
    Script\activate
```

## Dependências
As dependências estão contidas no arquivo ```requirements.txt```. Para instalar as dependências, basta executar o comando abaixo:
```cmd
pip install -r requirements.txt
```

## Uso
Preencha o dict ```lucky_numbers``` com os nomes e os respectivos números da sorte de cada participante (do bolão). A aplicação irá somar todos os números da sorte de cada participante (dando uma ilusão de que cada um está contribuindo para o acerto 🤣🤣🤣) Feito isso, basta executar ```python app.py``` (presumindo-se que o nome do arquivo que contem o script é "app.py" e se está na mesma pasta do script).
## Exemplo de resultado:<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>dez01</th>
      <th>dez02</th>
      <th>dez03</th>
      <th>dez04</th>
      <th>dez05</th>
      <th>dez06</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1º</th>
      <td>10</td>
      <td>31</td>
      <td>35</td>
      <td>40</td>
      <td>48</td>
      <td>59</td>
    </tr>
    <tr>
      <th>2º</th>
      <td>5</td>
      <td>6</td>
      <td>33</td>
      <td>37</td>
      <td>50</td>
      <td>56</td>
    </tr>
    <tr>
      <th>3º</th>
      <td>7</td>
      <td>12</td>
      <td>15</td>
      <td>17</td>
      <td>19</td>
      <td>46</td>
    </tr>
    <tr>
      <th>4º</th>
      <td>4</td>
      <td>8</td>
      <td>29</td>
      <td>47</td>
      <td>49</td>
      <td>52</td>
    </tr>
    <tr>
      <th>5º</th>
      <td>3</td>
      <td>21</td>
      <td>24</td>
      <td>28</td>
      <td>44</td>
      <td>54</td>
    </tr>
    <tr>
      <th>6º</th>
      <td>1</td>
      <td>11</td>
      <td>16</td>
      <td>41</td>
      <td>43</td>
      <td>45</td>
    </tr>
    <tr>
      <th>7º</th>
      <td>2</td>
      <td>18</td>
      <td>30</td>
      <td>42</td>
      <td>51</td>
      <td>53</td>
    </tr>
    <tr>
      <th>8º</th>
      <td>20</td>
      <td>25</td>
      <td>34</td>
      <td>39</td>
      <td>57</td>
      <td>58</td>
    </tr>
    <tr>
      <th>9º</th>
      <td>14</td>
      <td>26</td>
      <td>36</td>
      <td>38</td>
      <td>55</td>
      <td>60</td>
    </tr>
    <tr>
      <th>10º</th>
      <td>9</td>
      <td>13</td>
      <td>22</td>
      <td>23</td>
      <td>27</td>
      <td>32</td>
    </tr>
  </tbody>
</table>
## ATENÇÃO:
Esta brincadeira não aumenta nem diminui suas chances de acertar na Mega da VIRADA™. Trata-se APENAS de uma brincadeira com a linguagem de programação Python.

