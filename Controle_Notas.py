continuar = input('Deseja iniciar o sistema (S/N)? ').upper()

while (continuar != 'S' and continuar != 'N'):
    print('Opção Inválida!')
    continuar = input('Informe S-Sim ou N-Não').upper()

totalAlunos = 0
porcentagemAprovados = 0
porcentagemRecuperacao = 0
porcentagemReprovados = 0
masculinoAprovado = 0
femininoAprovado = 0
masculinoRecuperacao = 0
femininoRecuperacao = 0
masculinoReprovado = 0
femininoReprovado = 0
totalAprovados = 0
totalRecuperacao = 0
totalReprovados = 0

while (continuar == 'S'):
    totalAlunos += 1
    nome = input('Informe o nome do aluno: ')

    sexo = input('Qual o sexo? (M/F): ').upper()
    while (sexo != 'M' and sexo != 'F'):
        print('Opção Inválida!')
        sexo = input('Informe M-Masculino ou F-Feminino').upper()

    #notas dos alunos
    nota1 = float(input('Informe a primeira nota: '))
    while (nota1 < 0 or nota1 > 10):
        print('Opção Inválida!')
        nota1 = float(input('Informe uma nota válida: '))
    else:
        nota2 = float(input('Informe a segunda nota: '))
        while (nota2 < 0 or nota2 > 10):
            print('opção Inválida!')
            nota2 = float(input('Informe uma nota válida: '))
        else:
            nota3 = float(input('Informe a terceira nota: '))
            while (nota3 < 0 or nota3 > 10):
                print('Opção Inválida!')
                nota3 = float(input('informe uma nota válida: '))

    #Média dos alunos
    media = (nota1 + nota2 + nota3)/3
    print('Média do aluno: ', media)
    if (media >= 7 and sexo == 'M'):
        totalAprovados += 1
        masculinoAprovado += 1
        print('Situação: Aprovado')
    if (media >= 7 and sexo == 'F'):
        totalAprovados += 1
        femininoAprovado += 1
        print('Situação: Aprovada')

    if (media >=4 and media <7 and sexo == 'M'):
        totalRecuperacao += 1
        masculinoRecuperacao += 1
        print('Situação: Exame')
    if (media >= 4 and media <7 and sexo == 'F'):
        totalRecuperacao += 1
        femininoRecuperacao += 1
        print('Situação: Recuperação')

    if (media < 4 and sexo == 'M'):
        totalReprovados += 1
        masculinoReprovado += 1
        print('Situação: Reprovado')
    if (media < 4 and sexo == 'F'):
        totalReprovados += 1
        femininoReprovado += 1
        print('Situação: Reprovada')


    continuar = input('Deseja continuar o sistema (S/N)?').upper()
    while(continuar != 'S' and continuar != 'N'):
        print('Opção Inválida!')
        continuar = input('Informe S-Sim ou N-Não: ').upper()
    else:
        print('\n\nRESULTADOS FINAIS\n\n')

    print('Total de Alunos: ', totalAlunos)
    print('Porcentual de alunos aprovados: ', (totalAprovados*100)/totalAlunos, '%')
    print('Porcentual de alunos de recuperação: ', (totalRecuperacao*100)/totalAlunos, '%')
    print('Porcentual de alunos reprovados: ', (totalReprovados*100)/totalAlunos, '%')
    print('Quantidade de pessoas do sexo feminino aprovadas: ', femininoAprovado)
    print('Quantidade de pessoas do sexo masculino aprovadas: ', masculinoAprovado)
    print('Quantidade de pessoas do sexo feminino de recuperação: ', femininoRecuperacao)
    print('Quantidade de pessoas do sexo masculino de recuperação: ', masculinoRecuperacao)
    print('Quantidade de pessoas do sexo feminino reprovadas: ', femininoReprovado)
    print('Quantidade de pessoas do sexo masculino reprovadas: ', masculinoReprovado)





