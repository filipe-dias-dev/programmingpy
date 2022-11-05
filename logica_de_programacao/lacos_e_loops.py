idades = [18 , 22, 30, 14, 10]

def verifica_se_pode_dirigir(idades):
  for idade in idades:
    if idade >= 18:
      print(f'{idade} anos de idade, TEM permissão para dirigi!')
  else:
      print(f'{idade} anos de idade, NÃO tem permissão para dirigir!')

verifica_se_pode_dirigir(idades)