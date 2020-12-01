from django.shortcuts import render
import json


# Create your views here.
def load_cv(request, num):
    data = []
    file = 'app/static/eurocv{}.json'.format(num)
    with open(file, 'r') as f:
        data = json.load(f)
    return render(request, 'eurocv.html', data)