from django.shortcuts import render
from loanForm.models import Product
from loanForm.forms import ProductForm
from django.http import HttpResponse

#First view
def home_view(request, *args, **kwargs):
    #print(args, kwargs)
    #print(request.user)
    return render(request, "home.html", {})

#Second view
def product_app_view(request):

    #submitButton = request.POST.get("submit")

    user_amt = 0
    user_yrs = 0

    form = ProductForm(request.POST or None)
    if form.is_valid():
        user_name = form.cleaned_data.get("name")
        user_amt = form.cleaned_data.get("amount")
        user_yrs = form.cleaned_data.get("years")
        user_type = form.cleaned_data.get("type")
        form.save()

        values = {
            'name': user_name,
            'amount': user_amt,
            'years': user_yrs
        }

        return render(request, "result.html", values)



    context = {
        'form': form,
    }

    return render(request, "main.html", context)
