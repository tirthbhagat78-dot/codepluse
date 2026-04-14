from django.shortcuts import render


def home(request):
    lessons = [
        {"title": "Python Introduction", "done": 0, "total": 10, "tone": "teal"},
        {"title": "Variables and Data Types", "done": 0, "total": 10, "tone": "indigo"},
        {"title": "Control Flow", "done": 0, "total": 10, "tone": "pink"},
        {"title": "Functions", "done": 0, "total": 10, "tone": "green"},
        {"title": "Strings", "done": 0, "total": 10, "tone": "rose"},
        {"title": "Lists", "done": 0, "total": 10, "tone": "purple"},
        {"title": "Tuples", "done": 0, "total": 10, "tone": "indigo"},
        {"title": "Dictionaries", "done": 0, "total": 10, "tone": "purple"},
    ]

    quick_access = [
        {"name": "AI Tutor", "icon": "spark"},
        {"name": "My Notes", "icon": "note"},
        {"name": "Cheat Sheets", "icon": "book"},
        {"name": "Help Center", "icon": "help"},
        {"name": "Bookmarks", "icon": "bookmark"},
        {"name": "Study Goals", "icon": "goal"},
    ]

    return render(
        request,
        "learn/home.html",
        {
            "app_name": "Code Pluse",
            "lessons": lessons,
            "quick_access": quick_access,
        },
    )
