from django.shortcuts import render
import random

# Create your views here.

def index(request):
    return render(request, 'first_app/index.html')

def fetch_word():
    global words

    words = ['one', 'air', 'four', 'help', 'none', 'java', 'make', 'like', 'nike', 'hello']
    word =  list(random.choice(words))

    random.shuffle(word)

    word = ''.join(word)

    return word

def start_game(request):
    
    word = fetch_word()
    guessed = False

    if request.method ==  'POST':

        guessed = True
        guess = request.POST['guess']
        ans = ''
        
        if guess in words:
            ans = 'YES'
        else:
            ans = 'NO'

        return render(request, 'first_app/game.html', context = {'word': word, 'answer': ans, 'guessed': guessed})

    return render(request, 'first_app/game.html', context = {'word': word, 'guessed': guessed})

