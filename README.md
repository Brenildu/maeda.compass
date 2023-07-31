# Breno T. C. da S. Maeda

## Informações pessoais:

![Foto Breno Maeda](img/fotona.jpg)

Olá, meu nome é Breno Maeda e estou no programa de bolsas da compass.uol!

Resido atualmente na cidade de [Ilha Solteira SP](https://www.google.com/maps/place/Ilha+Solteira+-+SP,+15385-000/@-20.480396,-51.5590673,10z/data=!3m1!4b1!4m6!3m5!1s0x9499f8719482b45b:0x2763c44fdc87bc75!8m2!3d-20.4322835!4d-51.3487707!16zL20vMDQwd3dj?entry=ttu), 60 km do município de Três Lagoas cidade em que estudo e falando nisso, estudo sistemas de informação na instituição [UFMS](https://www.ufms.br) e já estou no meu 10 período, e sim! já estourei na perspectiva de ter concluído em 8 semestres, ainda faltam 4 semestres totalizando 14 no final, mas não sou uma pessoa que vê o copo meio cheio, esse tempo a mais não foi perdido, conheci pessoas incriveis no processo, a cada dp que pegava só me insentivava a correr atrás de novo e hoje já me vejo mais maduro e responsavél(melhorando aos poucos) coisa que não evoluiria se passasse nas matérias tudo com a nota mínima.

Queria ser breve, me empolguei kkkk. Sobre hobbies, começo pelos esportes, sou enxadrista amador, já disputei alguns torneios na minha região, chegando no máximo individualmente em segundo lugar no JESP(jogos escolares de São Paulo) sub 15 e entre os primeiros no sub 18, por equipe já ficamos em segundo nos abertos dos JJSP(jogos da juventude de SP, sub 18), atualmente jogo por Ilha Solteira, se quiser jogar ou ter umas aulinhas é só chamar!! Finjo que jogo outros esportes também kkkk, basket e futsal são os que me garanto não ser uma total ameba. Prático corridas curtas, gosto de ler(estava tentado bater a meta de 1 livro por mês, mas não vai dar não kkkk) e curto para um caramba terminar um programa sabendo que deu certo. 

Escolhi passar pelo programa para ter um noção básica do mercado de trabalho (sou muito inseguro em não ser um bom profissional no futuro). Ciente que sou uma pessoa que procrastina bastante, luto muito para melhorar isso, vim almejando receber o máximo de críticas possível para me auxiliar profissionalmente.


# Sprint 1

## Curso Git e GitHub do básico ao avançado (c/ gist e GitHub Pages)

* **Sobre o Git e GitHub**  
<p>
Como desenvolvedor de softwares vejo claramente a importância do git e as frameworks que trabalham o utilizando, as modificações continuas, o uso de várias versões e a importância de trabalhar com a mesma versão nas máquinas de todos os membros do projeto é de suma importancia a medida que o projeto cresce e tudo isso se encaixa no tema do controle de versão que é a premissa principal do git.  
&nbsp;
O git é o sistema de controle de versão mais utilizado no mundo, ele cria e trabalha com repositórios, esses que são responsavéis de armazenarem todas as linhas de código de uma aplicação, quando falamos em trabalhar em um repositório estamos falando de trabalhar diretamente em uma aplicação.  
&nbsp;
Há diversas ferramentas que usam do git e armazenam repositórios em divesos servidores online, podemos citar 3 grandes plataformas que fornecem esse serviço: GitHub, GitLab e BitBucket. Elas possuem sim algumas diferenças, como o foco não é citar a melhor, a pior ou o defeito de cada uma, comentarei apenas sobre o GitHub. O GitHub é a plataforma mais popular que existe no setor, ela é uma ferramenta gratuita que possui uma gigantesca comunidade que compartilha códigos públicos e privados. Para se criar uma conta no GitHub é simples, basta pesquisar por GitHub no navegador, clicar na opção de criar nova conta, preencher o formulário e aceitar o email de confirmação, se tudo der certo você estará cadastrado e pronto para compartilhar repositórios com outras pessoas.  
&nbsp;
</p>

* **Por onde começar?**  
&nbsp;
<p>
Primeiro de tudo faça o download das ferramentas, sendo elas o [git](https://git-scm.com/downloads) e um editor de texto. Download concluído é preciso criar uma pasta no editor de testo e abrir o terminal nela, com o comando git init é possível criar o repositório, tendo uma conta no GitHub será possível gerenciar esse repositório o enviando para lá com a sequência de comandos, git commit -m ".", git branch -M main, git remote add "link(que você receberá dentro do GitHub)" e git push -u Origin master.  
&nbsp;
Toda vez que criar pastas ou arquivos é preciso usar o comando git add ., toda modificação feita é preciso usar o comando git commit -a -m "mensagem tal" e para enviar para o repositório remoto é preciso dar um git push. Para baixar modificações se utiliza o comando git pull e é possível ver o status usando o git status.  
&nbsp;
</p>

* **Branch**
<p>  
É importante se falar das branches, essas são as ramificações de um projeto, dentro de um projeto possivelmente haverá funçãos ou layouts que serão testados, para que possa ocorrer modificações diretas no projeto que não comprometam sua funcionalidade atual é usado uma ramificação, a ramificação principal é chamada de main e nela que há o projeto funcional(cuidado para não há modificar sem querer), qualquer outra ramificação não é vista para o usuário final.  
&nbsp;
Um bom exemplo de como utiliza-lás na prática de maneira saúdavel: imagine 3 desenvolvedores de um projeto web, um deles modificou a pasta css dentro de uma branch e enviou para o GitHub, outro modificou o arquivo index.html dentro de outra branch e também o enviou e o terceiro, sendo esse o responsável por alterar a main ele deu um push e gostou das modificações, apartir disso ele cópia com o código git merge as duas ramificações dentro da main. Apartir desse exemplo dá para ver que as ramificações podem ser utéis para que não hajá confusões nas modificações, se o primeiro dev precisasse fazer testes, esses teste ficariam apenas em sua ramificação.    
</p>

&nbsp;
* **Comandos principais**  
&nbsp;
1. git init
    * Comando para criar um novo repositório, vai ser criado um pasta .git e um novo repo.
2. git add (+ . ou o nome do arquivo/pasta)
    * Comando que adiciona arquivos para o repositório
3. git commit (+-a  +-m +"especificações")    
    * Apenas usando commit já será comitada os arquivos, mais o -a e o -m vem como suporte para boas práticas comitando todos os arquivos e mando uma mensagem exclarecendo o commit.
4. git remote    
    * Faz a conexão entre seu repositório local e o GitHub.
5. git push
    * Sobe as modificações para o GitHub.
6. git pull
    * Baixa a ultima versão que foi dado o push do GitHub      
7. git branch
    1. (lista todas as ramificações)
    2. git branch (+ nome da branch): cria uma branch com esse nome
    3. git branch (+ nome da branch): deleta uma branch com esse nome
8. git checkout (+ nome da branch)
    * vai para a ramificação digitada, se usar o comando -b antes do nome, ele cria e vai para essa ramificação
9. git fetch
    * A partir desse comando, você irá receber todas as informações de commits, para avaliar, antes de aplicar essas alterações na sua versão local do repositório.    
10. git clone (+ link de um repositório original)
    * Comando para clonar um repostório já existente
11. git tag
    * Cria um marco dentro da branch, os marcos servem para ajudar no controle da versao: v 1.0
12. git rm (+ nome do arquivo)
    * Remove um arquivo    


## Curso Linux para Desenvolvedores (c/ terminal, Shell, Apache e +)


## Resumo 