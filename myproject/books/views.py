from django.shortcuts import render
from django.http import JsonResponse
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import requests
from functools import reduce


'''def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})
'''
@csrf_exempt
def operation(request): 
    json_data = json.loads(request.body)
    name = json_data.get('name')
    amount = json_data.get('amount')
    tip = json_data.get('tip')
    tax = json_data.get('tax')
    discount = json_data.get('discount')
    shprice = json_data.get('share price')
    shperson = json_data.get('share person')
    total = sum(amount)
    Task1 = total/len(name)
    Task2a = []
    Task2b = []
    n=0
    tip = tip/100
    tax = tax/100
    for i in amount:
        result = i - Task1
        if result < 0:
            Task2a.append(f"{name[n]} have to give {abs(result)} amount")
        elif result > 0:
            Task2b.append(f"{name[n]} have to take {abs(result)} amount")
        n = n + 1
    tipamount = total * tip
    taxamount = total * tax
    tipdistribute = tipamount/len(name) 
    taxdistribute = taxamount/len(name)
    tiptaxi = [tipdistribute,taxdistribute]
    tiptaxt = [tipamount,taxamount]
    afterdiscount = total-total*(discount/100)
    shamount = shprice/len(shperson)
    shstatement = f"{shperson} Share price {shamount} {shamount} equally"

    return JsonResponse({
        'Bill':total,
        'BasicSplitting': Task1,
        'UnevenSplittingGive': Task2a,
        'UnevenSplittingTake': Task2b,
        'Tip and Tax individual': tiptaxi,
        'Tip and Tax total': tiptaxt,
        'AmountAfterDiscount': afterdiscount,
        'SharePrice': shstatement
    })