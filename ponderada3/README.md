# Ponderada  2 
## Como executar o projeto 
- Para executar o projeto é necessário clonar o repositório
<pre><code>
git clone https://github.com/Leao09/Ponderadas-progM8.git
</code></pre>
- Em seguida instale as dependencias para o funcionamento do código junto com os cósdigo para a criação do nó
<pre><code>
cd Ponderada-progM8/ponderada2/chat-bot/src
colcon build 
source install/local_setup.bash
</code></pre>
- Para rodar  basta utilizar o comando
<pre><code>
ros2 run chat-bot chat-node
</code></pre>

## Explicação breve sobre o código 
- O código possui um dicionário de ações e um dicionário de intenções, sendo esse dicionário de intenções o que possui todas as expresões regulares que estão conectados as ações do outro dicinário. Além de possui um função a nav_pronpt que tem com objetivo pegar o input procurá-lo no dicinário de intenções e associar a sua ação, Além de possuir a função main, que utiliza de um laço de repetição para manter o chat funcionando até que a condição seja quebrada

## Demonstração 

[Link](https://youtu.be/B1afECgxA64)