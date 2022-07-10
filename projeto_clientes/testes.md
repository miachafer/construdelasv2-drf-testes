# Teste de usabilidade

## Teste manual de contraste

O objetivo desse teste é aferir e assegurar se/que na interface há o contraste adequado entre o fundo da tela e o texto. 

### Ferramenta de teste

[Color Contrast Analyser](https://dequeuniversity.com/rules/axe/3.1/color-contrast)  disponível no site da Deque University

### Critério para sucesso
O contraste deve ser de 4.5:1 para textos pequenos e 3:1 para textos grandes. Isso significa que para textos pequenos, a cor do texto (supondo que a cor do texto seja mais escura que a do fundo) tem que ser 4,5 vezes mais escura que a cor do fundo. 

### Telas analisadas

![Api Root](/projeto_clientes/prints/api_root.png)

![Cliente Instance](/projeto_clientes/prints/cliente_instance.png)

### Análise detalhada

#### 1. Cabeçalho
![cabecalho](/projeto_clientes/prints/cabecalho.png)
- Cor de fundo: #2c2c2c
- Cor do texto: #9a9a9a

**Resultado:**

![resultado cabeçalho](/projeto_clientes/prints/resultado_cabecalho.png)

Esse resultado mostra que essa combinação de cores não teria um bom contraste se fosse usada uma fonte de tamanho pequeno. Por sorte, o texto ("Django Rest Framework") ocupa um bom espaço do cabeçalho em fonte de tamanho médio. Além disso, quando se passa o cursor sobre ess parte do cabeçalho, a cor do texto muda para branco (#ffffff), o que resolve o problema do contraste. 

#### 2. Título
![titulo](/projeto_clientes/prints/titulo.png)
- Cor de fundo: #ffffff
- Cor do texto: #343434

**Resultado:**

![resultado título](/projeto_clientes/prints/resultado_titulo.png)

Sem problemas de contraste.

#### 3. Botões azuis
![botões](/projeto_clientes/prints/botoes.png)
- Cor de fundo: #337ab2
- Cor do texto: #ffffff

**Resultado:**

![resultado botões](/projeto_clientes/prints/resultado_botoes.png)

O resultado mostra que essa combinação de cores não tem um bom contraste em fontes de tamanho pequeno. No entanto, como o texto está dentro de um item gráfico (um botão), não há maiores problemas.

#### 4. Conteúdo
![conteúdo](/projeto_clientes/prints/conteudo.png)
- Cor de fundo: #f7f7f9
- Cor do texto (escuro): #333333
- Cor do texto (azul): #195f91
- Cor do texto (vermelho): #dd1144
- Cor do texto colchetes (cinza): #93a1a1

**Resultado:**

![resultado texto escuro](/projeto_clientes/prints/resultado_conteudo_texto_escuro.png)

Sem problemas de contraste. 

![resultado texto azul](/projeto_clientes/prints/resultado_conteudo_texto_azul.png)

O resultado mostra que essa combinação de cores não tem um bom contraste em fontes de tamanho pequeno, e esse texto tem tamanho pequeno na interface.

![resultado texto vermelho](/projeto_clientes/prints/resultado_conteudo_texto_vermelho.png)

O resultado mostra que essa combinação de cores não tem um bom contraste em fontes de tamanho pequeno, e esse texto tem tamanho pequeno na interface.

![resultado texto cinza (colchetes)](/projeto_clientes/prints/resultado_conteudo_texto_cinza.png)

O resultado mostra que essa combinação de cores não tem um bom contraste. Felizmente, o único texto com essa cor são alguns colchetes, não muito importantes para o uso da interface.

#### 5. Formulário
![formulário](/projeto_clientes/prints/formulario.png)
- Cor do fundo: #f5f5f5
- Cor do texto: #333333
- Cor do fundo dos campos do formulário: #ffffff
- Cor do texto dos campos do formulário: #555555

**Resultado:**

![resultado formulario](/projeto_clientes/prints/resultado_formulario.png)

![resultado formulario campos](/projeto_clientes/prints/resultado_formulario_campos.png)

Nem as cores de dentro dos campos de formulário e nem as de fora tem problemas de contraste.

#### 6. Opções do formulário
![opções do formulário](/projeto_clientes/prints/opcoes_formulario.png)
- Cor do fundo: #ffffff 
- Cor do texto (cinza): #555555
- Cor do texto (vermelho): #a30000

**Resultado:**

![resultado opções formulario cinza](/projeto_clientes/prints/resultado_opcoes_formulario_cinza.png)

![resultado opções formulario cinza](/projeto_clientes/prints/resultado_opcoes_formulario_vermelho.png)

Sem problemas de contraste.

#### 7. Botão delete
![botão delete](/projeto_clientes/prints/botao_delete.png)
- Cor do fundo: #c9302c
- Cor do texto: #ffffff

![resultado botão delete](/projeto_clientes/prints/resultado_botao_delete.png)

O resultado mostra que essa combinação de cores não tem um bom contraste em fontes de tamanho pequeno. No entanto, como o texto está dentro de um item gráfico (um botão), não há maiores problemas.
