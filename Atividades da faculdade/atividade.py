# AOP 2 IntProg

alunos_total = 100
alunos_aprovados = 0
alunos_reprovados = 0

for i in range(alunos_total):
    nome = input("Nome do aluno: ")
    aop1 = float(input("Nota da AOP 1: "))
    while aop1 > 1 or aop1 < 0:
        print("\nValor inválido, a nota mínima da AOP 1 é 0 e a máxima é 1.\nPreencha novamente.\n")
        aop1 = float(input("Nota da AOP 1: "))

    aop2 = float(input("Nota da AOP 2: "))
    while aop2 > 2 or aop2 < 0:
        print("\nValor inválido, a nota mínima da AOP 2 é 0 e a máxima é 2.\nPreencha novamente.\n")
        aop2 = float(input("Nota da AOP 2: "))

    aop3 = float(input("Nota da AOP 3: "))
    while aop3 > 1 or aop3 < 0:
        print("\nValor inválido, a nota mínima da AOP 3 é 0 e a máxima é 1.\nPreencha novamente.\n")
        aop3 = float(input("Nota da AOP 3: "))

    prova_regular = float(input("Nota da Prova Regular: "))
    while prova_regular > 6 or prova_regular < 0:
        print("\nValor inválido, a nota mínima da prova regular é 0 e a máxima é 6.\nPreencha novamente.\n")
        prova_regular = float(input("Nota da Prova Regular: "))

    soma_módulo = aop1 + aop2 + aop3 + prova_regular

    print("\n---> Sua nota foi:", soma_módulo)

    if soma_módulo >= 7:
        print("\nParabéns", nome, ",você foi aprovado(a)!")
        alunos_aprovados += 1
    else:
        print("\n", nome, ",você não atingiu a nota suficiente, faça a prova de recuperação!\n")
        prova_recuperação = float(input("Nota da Prova de Recuperação: "))

        while prova_recuperação > 10 or prova_recuperação < 0:
            print("\nValor inválido, a nota mínima da prova de recuperação é 0 e a máxima é 10.\nPreencha novamente.\n")
            prova_recuperação = float(input("Nota da Prova de Recuperação: "))

        média_módulo = (aop1 + aop2 + aop3 + prova_regular + prova_recuperação) / 2
        print("\n---> Sua nota da recuperação foi:", média_módulo)

        if média_módulo >= 5:
            print("\n", nome, ",você foi aprovado(a) com a recuperação!")
            alunos_aprovados += 1
        else:
            print("\n", nome, ",você foi reprovado(a)!")
            alunos_reprovados += 1
    print("-"*50, "\n")

aprovações_porcentagem = (alunos_aprovados / alunos_total) * 100
reprovações_porcentagem = (alunos_reprovados / alunos_total) * 100

print("Aprovados: ", aprovações_porcentagem, "%")
print("Reprovados: ", reprovações_porcentagem, "%")