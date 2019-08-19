from dictionaries import lil_nas_x, mark_hamill, playstation
from create import generate_text

print ('Welcome to Twitwit! please select an option below.')

print('1.) Lil Nas X')
print('2.) Mark Hamill')
print('3.) PlayStation')

def launcher(number):
    assert type(number) == 1 or 2 or 3

    if number == 1:
        return generate_text(lil_nas_x, 20)
    elif number == 2:
        return generate_text(mark_hamill, 20)
    elif number == 3:
        return generate_text(playstation, 20)

account = int(input('choice: '))

generated = launcher(account)

print(generated)


