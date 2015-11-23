function [vet_dados, vet_tempo] = funcao_leitura()
% teste_func
%   Esta função recebe como parâmetros um tempo, chamado de
%   tempo_de_discretizacao e um arquivo xls contendo os dados
%   recebidos do labview.
dados = input('Digite o nome do arquivo:  ');
vet_dados = xlsread(dados);
[M N] = size(vet_dados);
x = 1:M;
plot(x, vet_dados)
end
