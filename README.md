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

####Design Centrado ao Ser Humano (HCD)


## Soluções Propostas
Após realizadas estas etapas citadas acima, chegamos a uma solução que tornaria o processo de configuração e utilização da planta menos custoso tanto para os alunos quanto para os professores. Para isso a solução ideal escolhida foi criar um desenho padrão da planta, que poderia ser acessada e modificada posteriormente por seus usuários, junto de um programa de conversão de arquivos, que transformaria a extensão do arquivo exportado do Labview para um formato que o Matlab pudesse importar e trabalhar com esses dados.

O desenho foi desenvolvido utilizando o software Labview, dado que o Ifes Campus Serra (local onde o projeto está sendo aplicado) possui a licença para este software. E o programa de conversão foi desenvolvido na linguagem Python, e poderá ser acessado através de um arquivo executável que será disponibilizado nos laboratórios.

###Project Model Canvas
Segundo o [site] (http://www.projectmodelcanvas.com/) do Project Model Canvas, o Project Model Canvas é uma metodologia robusta de gerenciamento de projetos, sem o preenchimento de inúmeros documentos e sem burocracia. É ideal para ambientes que querem aprimorar sua capacidade de planejamento mas que se caracterizam por inovação, alta dinâmica dos negócios, muitos projetos em paralelo e nos quais soluções rígidas e engessadas não se aplicam.

A [PmTech] (http://www.pmtech.com.br/canvas_PM.html) complementa dizendo que o PMC concentra-se no essencial, a alma do projeto e permite com que os stakeholders participem da concepção do plano. A aplicação desta metodologia é adequada a todos os tipos de projeto, não sendo focada em projetos de alguma área especifica.

Em nosso projetos utilizamos o PMC para gerenciar nosso projeto, a versão final do nosso Project Model Canvas é demonstrado na figura abaixo.

![PMC](https://github.com/LEDS/Lab303/blob/master/Imagens/PMC.jpg "PMC")

##Scrum




