print("Seja bem-vindo(a) ao programa de notas, digite as informações pedidas para saber sobre sua média e aprovação.")

nota_1 = float(input("Digite sua primeira nota: "))
nota_2 = float(input("Digite sua segunda nota: "))
nota_3 = float(input("Digite sua terceira nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

def final():
  if media >= 6:
    return "aprovado(a)"
  else:
    return "reprovado(a)"

nota_final = final()

print(f"Sua média é de {media:.2f} pontos e você foi {nota_final}!")
