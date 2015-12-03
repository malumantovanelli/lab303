# Lab303
## Introdução
O Projeto Lab303 tem por objetivo auxiliar alunos e professores usuários da planta de fluidos do laboratório 303 a ter mais facilidade na utilização da planta. Além disso, o projeto visa o aprendizado das metodologias de gestão de projetos empregadas no LEDS.

Para o desenvolvimento das soluções utilizamos as seguintes tecnologias:

* __Linguagem de Programação__: [Python] (https://www.python.org) 
* __Softwares__: [MatLab] (http://www.mathworks.com/products/matlab/) e [LabView] (http://www.ni.com/labview/pt/)
* __Repositório de códigos__: [Git](https://git-scm.com)

## Problemas
Após conversar com alguns alunos da Engenharia de Controle e Automação, foram levantados alguns pontos a respeito da utilização da planta de fluidos do laboratório 303. Essa planta é uma maquete que simula o funcionamento de uma planta de fluidos de escala industrial. O objetivo desta planta é ser utilizada para o ensino de duas disciplinas do curso de Engenharia de Controle e Automação: Controle e Supervisório.

A planta do laborátorio é demonstrada na imagem abaixo.

![Planta Lab 303](https://github.com/LEDS/Lab303/blob/master/Imagens/PlantaSupervisorio.jpg "Planta do Lab 303")

##Etapas do Desenvolvimento da Solução
Após identificado o problema era necessário definir quais eram as principais requisições e o que os clientes esperavam daquele produto ou serviço. Sendo assim, foram aplicados algumas técnicas para levantamento de mais informações que pudessem guiar a equipe sobre qual era exatamente o problema e de que maneira poderia ser solucionado. Para isso foram aplicadas algumas técnicas de levantamento de requisitos.

###Processo de Levantamento de Requisitos
Uma das etapas da engenharia de requisitos é a elicitação, fase complexa da definição de requisitos e de todo processo de desenvolvimento de software, uma vez que é base para todas as etapas posteriores (BELGAMO; MARTINS, 2000). Elicitar requisitos requer um processo interativo que deve acontecer de forma colaborativa, envolvendo analistas, usuários e aplicação de técnicas (FREITAS; BORGES; ARAÚJO, 2007). No primeiro contato do analista com o cliente, dificilmente se extrai todas as informações relevantes para a
implementação do sistema, daí a importância das técnicas que auxiliam no levantamento desses dados válidos.

Existem técnicas que buscam auxiliar os analistas e os usuários na identificação dos requisitos do sistema, contudo, a complexidade dessa etapa de elicitação se deve, não apenas a fatores técnicos, mas também humanos. (BARBOSA et al., 2009) Este é um momento em que o analista deve atentar-se ao escolher a técnica que irá auxiliá-lo, pois este fator é uma das etapas do projeto mais importante. Dada a natureza do nosso universo as técnicas escolhidas para esse levantamento de requisitos foram: Entrevistas, Brainstorming e Design Centrado ao Ser Humano (HCD).

####Entrevistas


####Brainstorming
Em sessões de Brainstorming, um grupo de pessoas é reunido, um cenário simulado e um assunto discutido para atrair os requisitos. As pessoas participantes devem sentir-se confortáveis para discuti-lo sem se intimidar. Nenhuma ideia é descartada, pois todas são boas
ideias (LAUESEN, 2002).

####Estórias de Usuário


###Project Model Canvas


## Soluções Propostas
Após realizadas diversas etapas de levantamento de requisitos, estabelecimento de casos de usuário, análises de dados, reuniões de equipe, entre outros; chegamos a uma solução que torna o processo de configuração e utilização da planta menos custoso tanto para os alunos quanto para os professores. Para isso foi escolhido criar um desenho padrão da planta, que pode ser acessado e modificado posteriormente pelos usuários, utilizando o software Labview, dado que o Ifes possui a licença para este software. Além disso, foi criada uma função no MatLab que permite a importação de arquivos .xls, exportados do LabView para formato Excel, para o MatLab, possibilitando posterior processamento de dados neste software. Essa solução será melhor explicada nas próximas sessões.

### Labview


### MatLab

