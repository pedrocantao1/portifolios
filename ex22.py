print('DESENVOLVIDO POR PEDROCANTAO')
nome = str(input('Qual seu nome completo ? ')).strip()
primeiro = nome.split()
print ('Analisando seu nome ... ')
print ('Seu nome em maiúsulo é  {} .' .format(nome.upper()))
print ('Seu nome em minúsculo é {} .'.format(nome.lower()))
print ('Seu nome tem ao todo {} letras .' .format(len(nome) - nome.count(' ')))
print ('Seu primeiro nome tem {} letras .'.format(len(primeiro[0])))