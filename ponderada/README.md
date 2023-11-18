# Ponderadas-progM8 
- Está ponderada tinha como objetivo desenvolver um pacote ros de mapeamento e navegaççao utilizando o turtlebot3.
## Estrutura de pastas
<pre>
<code>
ponderada/pacotao/
│
├── launch/
├── pacotao/
└── setup.py
</code>
</pre>
## Como rodar a aplicação
- Primeiro é necessario realizar todas as configurações de ambiente relacionadas ao ros e ao bash ou zsh, feito isso o próximo passo e clonar o meu repositório do githib.
<pre>
<code>
git clone https://github.com/Leao09/Ponderadas-progM8.git
</code>
</pre>
- Posteriormente você deve instalar o meu pacote
<pre>
<code>
 source /Ponderadas-progM8/ponderada/pacotao/install/setup.bash
</code>
</pre>
- Por fim para executar o launch de mapeamento você deve entrar na pasta launch e rodas o script mapeando.launch.py
<pre>
<code>
ros2 launch mapeando.launch.py
</code>
</pre>
- Para a criação do mapa é necessário que você movimento o turtlebot3 ao redor do mapa, não precisa passar por todos os pontos mas caso ele não se mexa pode haver erros no salvamento do mapa.
- Após gerar o mapa basta rodar o launch de navegação dentro da pasta launch, o run.launch.py
<pre>
<code>
 ros2 launch run.launch.py
</code>
</pre>
## Demonstração
[link do video](https://youtu.be/ngbyQlLP3Ts)