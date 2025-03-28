from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse 

list_location = "shopping/list.txt" #for testing
#list_location = "Einkaufsliste/shopping/list.txt" #for deployement

def index(request):
    # initialize list
    items = []
    # read existing shopping list from file
    liste = open(list_location, "r")
    data = liste.read()
    # store items in list
    items = data.split("\n")
    liste.close()
    # remove blank list entries
    tmp = [x for x in items if x]
    items = tmp
    # return list to create index html
    return render(request, "shopping/index.html", {
        "items": items
    })

def add(request):
    # initialize list
    items = []
    if request.method == "POST":
        # receive new entry from form
        newentry = request.POST.get('newentry')
        # store new item to list and save as txt file
        items.append(newentry)
        liste = open(list_location, "a")
        for item in items:
            liste.write(f"{item}\n")
        liste.close()
        return HttpResponseRedirect(reverse("shopping:index"))
    else:
        return render(request, "shopping/add.html")
    
def delete(request):
    # initialize list
    items = []
    # read existing items from txt file
    liste = open(list_location, "r")
    data = liste.read()
    items = data.split("\n")
    liste.close()
    if request.method == "POST":
        # receive item to be deleted from form
        delete = request.POST.get('item')
        items.remove(delete)
        # remove blank list entries
        tmp = [x for x in items if x]
        items = tmp
        # store updated list as txt file
        liste = open(list_location, "w")
        for item in items:
            liste.write(f"{item}\n")
        liste.close()
        return HttpResponseRedirect(reverse("shopping:index"))