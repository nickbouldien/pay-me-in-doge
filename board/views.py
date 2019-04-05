from django.shortcuts import render

mock_sites = [
    {
        "link": "http://dogeiscool.com",
        "name": "dogeiscool",
        "poster": "doge4life",
        "date_posted": "November 29, 2018",
        "upvotes": 3,
        "description": "marketplace for doge things",
    },
    {
        "link": "http://dogerulez.all",
        "name": "doge rulez",
        "poster": "dogegod",
        "date_posted": "November 23, 2018",
        "upvotes": 7,
        "description": "the place where you can buy things",
    },
]


def home(request):
    context = {"sites": mock_sites}
    return render(request, "board/home.html", context)


def about(request):
    return render(request, "board/about.html")
