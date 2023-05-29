from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
monthly_challenge_dict = {
    'january': 'Eat no meat for the entire month',
    'febuary': 'Walk for atleast 20 minutes every day!',
    'march': 'Learn django for atleast 20 minutes everyday!',
    'april': None,
    'may': None,
    'june': None,
    'july': None,
    'august': None,
    'september': None,
    'october': None,
    'november': None,
    'december': None,
}


def index(request):
    months = list(monthly_challenge_dict.keys())

    return render(request, "challenges/index.html", {
        "months": months,
    })


def monthly_challenge_number(request, month):
    try:
        months = list(monthly_challenge_dict.keys())
        redirect_month = months[month - 1]
        # it will create a dynamic url instead of hard coded like /challenges/month_name
        redirect_path = reverse("monthly-challenge", args=[redirect_month])
        response = HttpResponseRedirect(redirect_path)
    except:
        response = HttpResponseNotFound("<h1>Index out of month range</h1>")
    return response


def monthly_challenge(request, month):
    try:
        description_text = monthly_challenge_dict[month]
        return render(request, "challenges/challenge.html", {
            'month': month,
            'text': description_text
        })
    except:
        raise Http404()

