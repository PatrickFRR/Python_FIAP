equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

#adicionando dados a lista
while resposta == "S":
 equipamentos.append(input("Equipamento: "))
 valores.append(float(input("Valor: ")))
 seriais.append(int(input("Número Serial: ")))
 departamentos.append(input("Departamento: "))
 resposta = input("Digite \"S\" para continuar: ").upper()

for equipamento in equipamentos:
 print("Equipamento: ", equipamento)

#retornando dados adicionados a lista no formato de indice
busca = input("\nDigite o nome do equipamento que deseja buscar: ")
for indice in range(0,len(equipamentos)):
 if busca == equipamentos[indice]:
  print("Valor..: ", valores[indice])
  print("Serial.:", seriais[indice])

#deletando dado depreciado
serial=int(input("\nDigite o serial do equipamento que será excluido: "))
for indice in range(0, len(departamentos)):
 if seriais[indice]==serial:
  del departamentos[indice]
  del equipamentos[indice]
  del seriais[indice]
  del valores[indice]
  break
for indice in range(0,len(equipamentos)):
 print("\nEquipamento..: ", (indice+1))
 print("Nome.........: ", equipamentos[indice])
 print("Valor........: ", valores[indice])
 print("Serial.......: ", seriais[indice])
 print("Departamento.: ", departamentos[indice])