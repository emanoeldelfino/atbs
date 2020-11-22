name = 'Al'
age = 4000
print('My name is %s. I am %s years old.' % (name, age))
print(f'My name is {name}. Next year I will be {age + 1}.')

user = 'Joseph'
directory = fr'C:\Users\{user}\Downloads'
print(directory)
# F'strings e raw strings são úteis quando o que vai nas chaves não possui escape characters, caso contrário será
# interpretado pela f string como tal, ou seja, se for um \n irá dar um espaço.
# É útil como no caso acima, quer um nome de caminho flexível conforme o nome do usuário.
