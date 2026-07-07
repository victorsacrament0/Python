nome = input("Digite seu nome: \n")
idade = input('Digite sua idade: \n')
curso = input('Curso Matriculado: \n')
email = input('E-mail para contato: \n')
print("Dados gravados com sucesso.")

arquivo = open('registro.txt', 'a', encoding="utf-8")
arquivo.write("Nome: " + nome + "\n")
arquivo.write("Idade: "+idade + "\n")
arquivo.write("Curso: "+curso + "\n")
arquivo.write("E-mail: "+email + "\n\n")
arquivo.write("-----------------------------------" + "\n")

arquivo.close()
