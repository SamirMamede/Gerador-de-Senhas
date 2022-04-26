import random, string

tamanho = 16

chars = string.ascii_letters + string.digits + 'ç!@#$%()-=+&*¨:;?/.'

rnd = random.SystemRandom()

senha = ''.join(rnd.choice(chars) for i in range(tamanho))
print(senha)