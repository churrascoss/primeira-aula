#contador de vogais e consoantes em uma frase 
frase = (input("digite uma frase: "))
num_vogais = 0
num_consoantes = 0
for letra in frase:
  if letra.isalpha():
    if letra == "a":
      num_vogais += 1
    elif letra == "e":
      num_vogais += 1
    elif letra == "i":
     num_vogais += 1
    elif letra == "o":
      num_vogais += 1
    elif letra == "u":
      num_vogais += 1
    elif letra == "A":
      num_vogais += 1
    elif letra == "E":
     num_vogais += 1
    elif letra == "I":
      num_vogais += 1
    elif letra == "O":
      num_vogais += 1
    elif letra == "U":
      num_vogais += 1
    else:
      num_consoantes += 1


print ("a frase tem ", num_vogais,"vogais e ", num_consoantes,"consoantes")