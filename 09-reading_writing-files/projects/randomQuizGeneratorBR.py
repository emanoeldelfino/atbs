import random
import string
import os

os.mkdir('quiz_capitais')

capitals = {'Acre': 'Rio Branco', 'Alagoas': 'Maceió', 'Amapá': 'Macapá',
            'Amazonas': 'Manaus', 'Bahia': 'Salvador', 'Ceará': 'Fortaleza',
            'Distrito Federal': 'Brasília', 'Espírito Santo': 'Vitória',
            'Goiás': 'Goiânia', 'Maranhão': 'São Luís', 'Mato Grosso': 'Cuiabá',
            'Mato Grosso do Sul': 'Campo Grande', 'Minas Gerais': 'Belo Horizonte',
            'Pará': 'Belém', 'Paraíba': 'João Pessoa', 'Paraná': 'Curitiba',
            'Pernambuco': 'Recife', 'Piauí': 'Teresina', 'Rio de Janeiro': 'Rio de Janeiro',
            'Rio Grande do Norte': 'Natal', 'Rio Grande do Sul': 'Porto Alegre',
            'Rondônia': 'Porto Velho', 'Roraima': 'Boa Vista', 'Santa Catarina': 'Florianópolis',
            'São Paulo': 'São Paulo', 'Sergipe': 'Aracaju', 'Tocantins': 'Palmas'}

letters = string.ascii_uppercase

letters = letters[:letters.index('M') + 1]

for quiz_letter in letters:
    file1 = f'quiz_capitais{os.sep}quizcapitais_perguntas{quiz_letter}.txt'
    file2 = f'quiz_capitais{os.sep}quizcapitais_respostas{quiz_letter}.txt'

    with open(file1, 'w') as quiz_file, open(file2, 'w') as answer_key_file:

        quiz_file.write('Nome: \n\nData: \n\nTurma: \n\n')
        quiz_file.write((' ' * 20) + f'Quiz das capitais estaduais {quiz_letter}\n\n')

        states = list(capitals.keys())
        random.shuffle(states)

        for question_num in range(27):
            correct_answer = capitals[states[question_num]]
            wrong_answers = list(capitals.values())
            del wrong_answers[wrong_answers.index(correct_answer)]
            wrong_answers = random.sample(wrong_answers, 3)
            answer_options = wrong_answers + [correct_answer]
            random.shuffle(answer_options)

            quiz_file.write(f'{question_num + 1}. Qual é a capital do/de {states[question_num]}?\n')
            for i in range(4):
                quiz_file.write(f"    {'ABCD'[i]}. {answer_options[i]}\n")
            quiz_file.write('\n')

            answer_key_file.write(f"{question_num + 1}. {'ABCD'[answer_options.index(correct_answer)]}\n")
