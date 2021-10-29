#CONCEITO DE TESTE DE CAIXA BRANCA OU TESTE DE CAIXA PRETA

# > Test White Block - Testes baseados em informações do software. Sãos testes unitários feitos com
#base em conhecimentos prévios do software. Geralmente testes de CAIXA BRANCA são feitos após o código
#estar escrito. Sendo ele feito com partes diferentes do código.

# > Test Black Block - São testes sem conhecimentos internos do software. Não é necessário saber como o 
#código é escrito para esxecutar os tetse. São Block Black testes quando escritos antes mesmo do software ser escrito.
#um exemplo seria digitar um link na barra de endereço e ver se aigintiu o objetivo, não é preciso nenhum conhecimento
#de como funciou o software, o teste é opaco.


#  >>>>>>>>> OUTROS TIPOS DE TESTES <<<<<<<<<<<<<<<<<<<<<

#Testes de intergação
    """
- Verifica se as integrações com diferentes partes do projeto estão funcionoando como deveriam. Por exemplo, um teste de 
banco de dados que recebe e sincroniza os dados do usuário. Um grupo de testes executaria vários pequenos testes de maneira que as 
intergações funcionasse. Talvez seja preciso criar um ambiente de testes. Garante que todas as peças estejam conectadas e funcionando antes
de serem postas no ambiente de produção.
    """

#Testes de Regressão
    """
- Verfica se um problema foi corrigido depois de identificado. Eles faz testes frequentes para verificar se os mesmos erros 
não estão ocorrendo novamente ou seja, garante que os mesmos erros não aconteçam de novo. Se um mesmo erro ja solucionado for introduzido novamente
fará com que o teste de regressão FALHE.
    """

#Testes de fumaça -  Verificação de construção
    """
- As vezes chamado de teste de construção, utilizado para encontrar grandes BUGS no sistema. Onde a fumaça a fogo, ou seja um programa não irá executar
se houver fumaça. Esse tipo de teste responde perguntas básicas como "O programa executa?".
Teste esse feito antes mesmo de testes mais refinados, uma vez que o teste de fumaça falhar ele não passará em nenhum outro.
    """

#Testes de Carga
    """
- São testes para verificiar se o software funciona com grande grande carga de requisões ou de dados, ou seja um teste de demanda. Quantos usuários
fazendo requisões simultaneas a aplicação suporta. 
    """

#Conjunto de testes
    """
    Um conjunto de testes mais robusto tem apossibilidade de criar um software profissional. Minimizando os erros e danos tanto para a empresa quanto para os usuários.
    Esse são os testes mais comuns, mas ainda existem muitos outros testes a serem estudados.
    
    """
"""

Desenvolvimento Orientado por Testes
Vamos tratar dos TDD

>>>>>>>>>>   TEST DRIVEN DEVELOPMENT   <<<<<<<<<

"""
