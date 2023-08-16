# Breno T. C. da S. Maeda

## Informações pessoais:

![Foto Breno Maeda](img/fotona.jpg)

Olá, meu nome é Breno Maeda e estou no programa de bolsas da compass.uol!

Resido atualmente na cidade de [Ilha Solteira SP](https://www.google.com/maps/place/Ilha+Solteira+-+SP,+15385-000/@-20.480396,-51.5590673,10z/data=!3m1!4b1!4m6!3m5!1s0x9499f8719482b45b:0x2763c44fdc87bc75!8m2!3d-20.4322835!4d-51.3487707!16zL20vMDQwd3dj?entry=ttu), 60 km do município de Três Lagoas cidade em que estudo e falando nisso, estudo sistemas de informação na instituição [UFMS](https://www.ufms.br) e já estou no meu 10 período, e sim! já estourei na perspectiva de ter concluído em 8 semestres, ainda faltam 4 semestres totalizando 14 no final, mas não sou uma pessoa que vê o copo meio cheio, esse tempo a mais não foi perdido, conheci pessoas incriveis no processo e sou grato por isso. 

Sobre hobbies, começo pelos esportes, sou enxadrista amador, já disputei alguns torneios na minha região, chegando no máximo individualmente em segundo lugar no JESP(jogos escolares de São Paulo) sub 15 e entre os primeiros no sub 18, se quiser jogar ou ter umas aulinhas é só chamar!! Finjo que jogo outros esportes também kkkk, basket e futsal são os que me garanto não ser uma total ameba. Prático corridas curtas, gosto de ler(estava tentado bater a meta de 1 livro por mês, mas não vai dar não kkkk) e curto para um caramba terminar um programa sabendo que deu certo. 

Escolhi passar pelo programa para ter um noção básica do mercado de trabalho (sou muito inseguro em não ser um bom profissional no futuro). Ciente que sou uma pessoa que procrastina bastante, luto muito para melhorar isso, vim almejando receber o máximo de críticas possível para me auxiliar profissionalmente.

# Marco Atual

- [x] Sprint 1
- [x] Sprint 2
- [ ] Sprint 3
- [ ] Sprint 4
- [ ] Sprint 5
- [ ] Sprint 6
- [ ] Sprint 7
- [ ] Sprint 8
- [ ] Sprint 9
- [ ] Sprint 10

# RESUMOS

## Sprint 1

### Curso Git e GitHub do básico ao avançado (c/ gist e GitHub Pages)

&nbsp;
* **Sobre o Git e GitHub**  
<p>
&nbsp;
Como desenvolvedor de softwares vejo claramente a importância do git e as frameworks que trabalham o utilizando, as modificações continuas, o uso de várias versões e a importância de trabalhar com a mesma versão nas máquinas de todos os membros do projeto é de suma importancia a medida que o projeto cresce e tudo isso se encaixa no tema do controle de versão que é a premissa principal do git.<br/>  
&nbsp;
O git é o sistema de controle de versão mais utilizado no mundo, ele cria e trabalha com repositórios, esses que são responsavéis de armazenarem todas as linhas de código de uma aplicação, quando falamos em trabalhar em um repositório estamos falando de trabalhar diretamente em uma aplicação.<br/>
&nbsp;
Há diversas ferramentas que usam do git e armazenam repositórios em divesos servidores online, podemos citar 3 grandes plataformas que fornecem esse serviço: GitHub, GitLab e BitBucket. Elas possuem sim algumas diferenças, como o foco não é citar a melhor, a pior ou o defeito de cada uma, comentarei apenas sobre o GitHub. O GitHub é a plataforma mais popular que existe no setor, ela é uma ferramenta gratuita que possui uma gigantesca comunidade que compartilha códigos públicos e privados. Para se criar uma conta no GitHub é simples, basta pesquisar por GitHub no navegador, clicar na opção de criar nova conta, preencher o formulário e aceitar o email de confirmação, se tudo der certo você estará cadastrado e pronto para compartilhar repositórios com outras pessoas.  
</p>

&nbsp;
* **Por onde começar?**  
<p>
&nbsp;
Primeiro de tudo faça o download das ferramentas, sendo elas o <a href=https://git-scm.com/downloads>git</a> e um editor de texto. Download concluído é preciso criar uma pasta no editor de testo e abrir o terminal nela, com o comando git init é possível criar o repositório, tendo uma conta no GitHub será possível gerenciar esse repositório o enviando para lá com a sequência de comandos, git commit -m ".", git branch -M main, git remote add "link(que você receberá dentro do GitHub)" e git push -u Origin master.<br/>
&nbsp;
Toda vez que criar pastas ou arquivos é preciso usar o comando git add ., toda modificação feita é preciso usar o comando git commit -a -m "mensagem tal" e para enviar para o repositório remoto é preciso dar um git push. Para baixar modificações se utiliza o comando git pull e é possível ver o status usando o git status.  
</p>

&nbsp;
* **Branch**
<p>
&nbsp;  
É importante se falar das branches, essas são as ramificações de um projeto, dentro de um projeto possivelmente haverá funçãos ou layouts que serão testados, para que possa ocorrer modificações diretas no projeto que não comprometam sua funcionalidade atual é usado uma ramificação, a ramificação principal é chamada de main e nela que há o projeto funcional(cuidado para não há modificar sem querer), qualquer outra ramificação não é vista para o usuário final.<br/> 
&nbsp;
Um bom exemplo de como utiliza-lás na prática de maneira saúdavel: imagine 3 desenvolvedores de um projeto web, um deles modificou a pasta css dentro de uma branch e enviou para o GitHub, outro modificou o arquivo index.html dentro de outra branch e também o enviou e o terceiro, sendo esse o responsável por alterar a main ele deu um push e gostou das modificações, apartir disso ele cópia com o código git merge as duas ramificações dentro da main. Apartir desse exemplo dá para ver que as ramificações podem ser utéis para que não hajá confusões nas modificações, se o primeiro dev precisasse fazer testes, esses teste ficariam apenas em sua ramificação.<br/> 
</p>

&nbsp;
* **Comandos principais**  
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

&nbsp;
* **Readme.md e marckdown**
<p> 
&nbsp;
O Readme é o que vai vender o seu peixe dentro do GitHub, a ideia é ter resumos principais da sua aplicação como o detalhamento da linguam utilizando, colaboradores, tarefas pendenter e concluídas e funcionalidades.<br />
&nbsp;
Para formatar esse arquivo é utilizado a linguagem de marcação MarckDown, ela converte as especificaçãos para o html.
</p>

* **Opnião Pessoal**
<p> 
&nbsp;
Gostei muito do curso, achei o professor bem didático e demonstrou o conteúdo perfeitamente na prática, acredito que usarei conhecimento aprendido de forma cotidiana no futuro.
</p>

### Curso Linux para Desenvolvedores (c/ terminal, Shell, Apache e +)

&nbsp;
* **Introdução do curso**  
<p>
&nbsp;
O Linux é um sistema operacional muito famoso entre os desenvolvedores, ele tem sim suas vantagens em ralação ao S.O Windows, o preço, a velocidade, segurança, algumas funcionalidades, entre outras. A ideia do curso não é falar sobre o linux e sim ensinar o aluno a trabalhar de forma prática com o terminal e o powershell.<br />
&nbsp;
Foi utilizado a distriubuição Ubuntu, pois ele é o mais popular das versões e atende bem o desejado de forma eficiente, diferente do mac e do wintowns é sempre preciso utilizar as distribuições mais recentes, nos sitemas operacionais temos o kernel que realiza a comunicação do hardawere com o usuário no linux também possuimos ele. Para instalar esse sistema sem precisar abrir mão do Windowns pode ser usado uma máquina virtual, a escolhida por mim foi a <a href=https://www.oracle.com/br/virtualization/technologies/vm/downloads/virtualbox-downloads.html?source=:ow:o:p:nav:mmddyyVirtualBoxHero_br&intcmp=:ow:o:p:nav:mmddyyVirtualBoxHero_br>VM VirtualBox</a>, da empresa Oracle, mas o instrutor sugere outra opção interessante também, agora é preciso do arquivo .iso do <a href=https://ubuntu.com/download/desktop>Ubuntu</a> para abri-ló dentro da VM, feito o download dos dois é preciso apenas criar um nova máquina virtual, escolher o sistema linux, Ubuntu e arrastar o arquivo .iso para opção de arquivos na tela.<br />
&nbsp;
Para abrir o terminal basta clicar em arquivos e abrir por la, ou clicar ctrl + t, e pronto o terminal estará aberto e pronto para ter a manipulação dos diretórios e arquivos com o uso simples de códigos a partir apenas do teclado. Podemos no perguntar da vantagem de usar o termianal, é possível citar a facilidade de usar apenas uma porta de entrada, a velocidade de criar, modificar e procurar por diretórios e arquivos, a praticidade de poder ver alterações e algumas outras  .
</p>

&nbsp;
* **Terminal e comandos básicos**  
<p>
&nbsp;
O terminal são janelas que podemos digitar comandos que comunicaram com o shell e o shell executará esses comandos retornando um resultado.
O basico da sintaxe do comando é seguir essa sequencia: comando -opções arquivo/diretorio, é importante saber a diferença entre arquivos e diretórios, os diretórios de forma direta são as pastas que podem armazenar arquivos ou outras pastas e os arquivos são únicos e contem apenas conteúdo.
</p>

&nbsp;
* **Gerenciamentos**  

1. Gerenciamento de arquivos e diretorios
    * Uso de comandos para criar, deletar, copiar ou mover arquivos e diretórios
    * Principais comandos: 
        1. mkdir - criar diretório
        2. rm - remover diretório ou arquivos
        3. rmdr - remover apenas diretórios
        4. cp - copiar arquivos ou diretórios
        5. mv - mover arquivos ou diretórios
2. Gerenciamento de pacotes e aplicativos
    * Com o auxílio de comandos no terminal é possível atualizar, instalar ou remover aplicativos ou até mesmo o Linux;
    * Tudo é feito de forma simples e é preciso ter permissão usando o comando sudo apt -get (+ o comando que precisa fazer) se for atualizar é upagrade, para instalar é install + o nome do aplicativo e para remover purge + o nome do aplicativo
3. Gerenciamento de usuários e grupos
    * Também há a possibilidade de criar e deletar usuários e grupos, nem sempre é tão utilizado, mas pode ser utilizado para garantir permissões de forma segura para usuários em várias funçãos em uma empresa que utiliza do Linux.
    * É preciso ter usuários para trabalhar com grupos, só conseguem fazer modificações desses grupos e usuários alguem com permissão para tal
4. Gerenciamento de permissões
    * Pemissões no linux são representandos por números, sendo o primeiro algarismo a permissão de diretório e arquivos, os três próximos são as permissões de leitura, escrita e execução, os três próximos são as permissões do grupo e os ultimos são as permissões do demais usuários;
    * Alterar permissões existem duas formas 1 sendo a numérica: chmod xxx file/dir (x são as permissões numérias):
        1. 0 ou -- = sem permissão
        2. 1 ou --x = Executar
        3. 2 ou -w- = Escrever
        4. 3 ou -wx = Escrever e executar
        5. 4 ou r-- = Ler
        6. 5 ou r-x = Ler e executar
        7. 6 ou r-w = Ler e excrever
        8. 7 ou rwx = Ler, escrever e executar

5. Gerenciamento de Redes
    * Fundamentos teóricos podem ser executados dentro do terminal do Linux 


## Sprint 2

### Curso SQL

&nbsp;

1. Baixar e Instalar:
    * Baixar e instalar o pgAdmin, software gráfico para administração do PostgreSQL.
    * Baixar e instalar o PostgreSQL, sistema gerenciador de banco de dados (SGBD) com SQL.

2. Configuração do Banco de Dados:

    * Rodar um script para criar tabelas a serem usadas no curso.

**Diagramas**:
&nbsp;
Representações gráficas de tabelas e suas conexões.
&nbsp;
**Pontos Importantes**:

- Usar aspas simples para textos e aspas duplas para nomes de colunas.
- `AS` para pseudônimos de colunas.
- Formato de datas: ano/mês/dia.
- `current_date` retorna a data atual.
&nbsp;
1. Comandos essenciais:

    * `SELECT`: selecionar colunas de tabelas.
    * `DISTINCT`: mostrar apenas linhas distintas.
    * `WHERE`: filtrar linhas com base em condições.
    * `ORDER BY`: ordenar colunas.
    * `LIMIT`: limitar número de linhas retornadas.

2. Funções de Agregação:

    * `COUNT()`: conta as linhas.
    * `SUM()`: opera a soma.
    * `MIN()`: devolve o mínimo valor de uma coluna.
    * `MAX()`: devolve o maior valor de uma coluna.
    * `AVG()`: realiza a média.

3. GROUP BY e HAVING:

    * agrupa os registros semelhantes de uma coluna.    
    * Filtra linhas da seleção por uma coluna agrupada possui a mesma função do where mas pode filtrar funções agregadas e não agregadas

4. Joins:

    * `LEFT JOIN`, `INNER JOIN`, `RIGHT JOIN`, `FULL JOIN`.
    * Combinação de dados de diferentes tabelas, sendo em sequência: a primeira tabela junto com o match da segunda, a segunda tabela junto com o match da primeira, só os match das duas e as duas tabelas combinadas 

5. Union:

    * `UNION`  so adiciona na tabela1 as linhas diferentes que estiverem na linha 2
    * `UNION ALL`faz a união da tabela 1 e no final dela faz a cola da tabela 2

6. Subqueries:

    * São query que podem ser trabalhadas dentro de outras
    * `WITH` é possível escrever subquery diretos no from, so que escrever no with da mais organização
    * Subqueries podem ser usadas em diferentes partes.

7. Tipos de Conversão:

    * Operador `::` e `CAST`
    * O operador é mais utilizado e simples de se entender, porém em algumas situações ele não funcionará e aí que entra o uso do cast que opera a mesma função.

8. Tratamento de Dados:

    * `CASE WHEN` para respostas específicas.
    * `COALESCE` para valores não nulos.
    * Funções como `LOWER`, `UPPER`, `TRIM`, `REPLACE` auxiliam a transformar strings, cada qual tendo sua função

9. Comandos de Tratamento de Data:

    * `INTERVAL`, opera soma de datas, caso não especifique somará em dias
    * `DATE_TRUNC`, trunca uma data no início do período
    * `EXTRACT`,  extrai unidades de uma data
    * `DATE_DIFF`. calcula a diferença entre datas alterando a unidade

10. Criar Tabelas e Manipular Linhas e Colunas:

    * `CREATE TABLE` para criar tabelas.
    * `INSERT INTO` para adicionar linhas.
    * `UPDATE` para atualizar linhas.
    * `DELETE FROM` para deletar linhas.
    * `ALTER TABLE` para modificar tabelas.

    1. Manusear Colunas:
        * `ADD` para adicionar colunas.
        * `ALTER COLUMN` para alterar tipos de colunas.
        * `DROP COLUMN` para remover colunas.