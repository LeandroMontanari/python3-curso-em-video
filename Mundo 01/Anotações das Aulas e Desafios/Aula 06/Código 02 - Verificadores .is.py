n = input('Digite algo: ')
print(n.isnumeric())  # Verifica se o que foi digitado é ou pode se tornar um valor numérico; retorna True se sim
print(n.isalpha())  # Verifica se o que foi digitado é uma letra ou contém apenas letras; retorna True se sim
print(n.isalnum())  # Verifica se o que foi digitado contém apenas letras e números; retorna True se sim
print(n.isupper())  # Verifica se o que foi digitado contém apenas letras maiúsculas; retorna True se sim
# Existem ainda outros métodos "is", como "islower()", "isspace()" etc.
