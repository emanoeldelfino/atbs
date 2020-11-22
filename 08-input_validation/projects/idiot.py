import pyinputplus as pyip

while True:
    answer = pyip.inputYesNo('Want to know how to keep an idiot busy for hours?\n')
    # pyip inputYesNo is guaranteed to only return either the string yes or the string no, even if the
    # user enters 'n', that is valid for 'no', it'll turn it into 'no'.

    if answer == 'no':
        break

print('Thank you. Have a nice day.')


# In my mother language Portuguese:
while True:
    mensagem = 'Quer saber como manter um idiota ocupado por horas?\n'
    resposta = pyip.inputYesNo(mensagem, yesVal='sim', noVal='não')
    # Now the user can enter either 's' or 'sim' instead of 'yes' and 'y'.

    if resposta == 'não':
        break

print('Obrigado. Tenha um ótimo dia.')
