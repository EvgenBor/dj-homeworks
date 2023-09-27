from django.shortcuts import render
from django.core.paginator import Paginator

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'cappuccino': {
        'молоко, 100 мл': 1,
        'кофе, 100 мл': 1,
        'сахар, 2 чайные ложки': 2,
    },
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def recipes(request, dish):
    persons = int(request.GET.get('servings', 1))
    context = {
        'recipe': {},
    }
    for k, v in DATA.get(dish, {}).items():
        context['recipe'][k] = v * persons
    return render(request, 'calculator/index.html', context)