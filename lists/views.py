from django.shortcuts import render, redirect
# from django.http import HttpResponse
from lists.models import Item

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        # new_item_list = request.POST['item_text']
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'item': items})



    #     Item.objects.create(text=new_item_list)
    # else:
    #     new_item_list = ''
    # # item = Item()
    # # item.text = request.POST.get('item_text', '')
    # # item.save()
    #
    # return render(request, 'home.html', {
    #     'new_item_text': new_item_list})
    #