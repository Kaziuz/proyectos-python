# Analizador de texto

textInput = input("Ingrese un texto: ")
print("\n")
letra1 = input("Ingrese la primera letra que desea buscar en el texto: ")
letra2 = input("Ingrese la segunda letra que desea buscar en el texto: ")
letra3 = input("Ingrese la tercera letra que desea buscar en el texto: ")
print("\n")

letrasInput = [letra1.lower(), letra2.lower(), letra3.lower()]

# cuantas veces aparece en el textInput cada una de las letras que eligió
print(f"La letra {letra1} aparece {textInput.lower().count(letrasInput[0])} veces")
print(f"La letra {letra2} aparece {textInput.lower().count(letrasInput[1])} veces")
print(f"La letra {letra3} aparece {textInput.lower().count(letrasInput[2])} veces")

# decir al usuario cuantas palabras hay a lo largo de todo el texto
print(f"El texto tiene {len(textInput.split())} palabras")

# decir cual es el primera letra del texto y cual es la ultima
print(f"La primera letra del texto es: {textInput[0]}")
print(f"La ultima letra del texto es: {textInput[-1]}")

# mostrar el texto invertido
splitted_text = textInput.split()
splitted_text.reverse()
texto_invertido = " ".join(splitted_text)

print("El texto invertido es: ", texto_invertido)

# nos va a decir si el textInput contiene la palabra python
dic = { True: "Si", False: "No"}
buscar_python = "python" in textInput
print("Esta la palabra python en el texto: ", dic[buscar_python])