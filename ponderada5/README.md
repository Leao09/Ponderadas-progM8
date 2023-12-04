# Ponderada 4
# Como executar o projeto
- Primeiramente para rodar o projeto é necessário clonar o meu repositório do git hub.
<pre><code>
git clone https://github.com/Leao09/Ponderadas-progM8.git
</code></pre>
- Em seguida é necessário entrar na pastas no qual o código está
<pre><code>
cd Poderadas-progM8/ponderada4
</code></pre>
- Assim, você deve criar um ambiente virtual para realizar as intalações de dependêcias e executar o código, por definição utilizaremos o miniconda que é uma versão menor. O comando para instalação:
<pre><code>
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && bash Miniconda3-latest-Linux-x86_64.sh
</code></pre>
- Comando para criar um ambiente virtual
<pre><code>
conda create -n "nome do seu ambiente" python=3.11
</code></pre>
- Comando para ativar o seu ambiente 
<pre><code>
conda activate "nome do seu ambiente"
</code></pre>
- Por fim iremos instalar todos os pacotes que vamos utilizar 
<pre><code>
conda install -r requirements.txt
</code></pre>
- Para rodar este projeto você precisa ter uma key da api da opneai e precisa ter créditos para utilizá-la, assim aṕos ter essa key crie um arquivo .env e coloque sua key em uma variável com o nome OPENAI_API_KEY.

> Alerta:
>Lembre-se de colocar o arquivo .env no seu arquivo .gitignore para que ele não seja publicado



- Finalizado toda a criação do ambiente é  necessário apenas rodar o seguinte comando para inicializar o código 
<pre><code>
streamlit run app.py
</code></pre>

# Descriação do código 
## app.py 
- Neste arquivo possui 3 funções a primeira é para carregar o pdf gerado pela página dada no enunciado, armazenar em um vetor e retornar a váriavel retriver. A segunda função é responsável por carregar o modelo utilizando a api da openai, além de criar a corrente com o conteudo do pdf junto a resposta. Por fim a função main cria os elementos visuais do streamlit e manda a requisição para a api.
# Demonstração
[Link](https://youtu.be/c8jEU-5aYzE)