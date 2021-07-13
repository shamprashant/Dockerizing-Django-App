from django.shortcuts import render
import random

# Create your views here.

def index(request):
    return render(request, 'first_app/index.html')

def fetch_word():
    global words, temp

    words = ['one', 'air', 'four', 'help', 'none', 'java', 'make', 'like', 'nike', 'hello']
    temp = random.choice(words)
    word =  list(temp)

    random.shuffle(word)

    word = ''.join(word)

    return word

def start_game(request):

    if request.method ==  'POST':

        guessed = True
        guess = request.POST['guess']
        ans = ''
        
        if guess == temp:
            ans = 'YES'
        else:
            ans = 'NO'

        return render(request, 'first_app/game.html', context = {'word': fetch_word(), 'answer': ans, 'guessed': guessed})

    return render(request, 'first_app/game.html', context = {'word': fetch_word(), 'guessed': False})

