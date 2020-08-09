from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'
    with open('inflation_russia.csv', newline='') as csvfile:
        csv_data = csv.reader(csvfile, delimiter=';')
        res = list(csv_data)

    res.pop(0)

    # чтение csv-файла и заполнение контекста
    context = {'inflation_by_year': res}

    return render(request, template_name,
                  context)