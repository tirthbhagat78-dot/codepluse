from django.http import Http404
from django.shortcuts import render


FEATURE_PAGES = {
    "explore": {
        "title": "Explore Topics",
        "subtitle": "Browse practical paths and discover what to learn next.",
        "cards": [
            {"name": "Web Development", "detail": "Build websites with Python and Django."},
            {"name": "Data Analysis", "detail": "Learn data cleaning, charts, and insights."},
            {"name": "Automation", "detail": "Automate repetitive tasks with scripts."},
            {"name": "Interview Prep", "detail": "Practice Python questions step by step."},
        ],
    },
    "ai-tutor": {
        "title": "AI Tutor",
        "subtitle": "Get instant help, hints, and explanations while learning.",
        "cards": [
            {"name": "Ask a Question", "detail": "Type any Python doubt and get guided help."},
            {"name": "Explain Code", "detail": "Paste code and receive simple explanations."},
            {"name": "Debug Help", "detail": "Share errors and get likely fixes."},
            {"name": "Practice Coach", "detail": "Generate bite-sized quiz questions."},
        ],
    },
    "progress": {
        "title": "Your Progress",
        "subtitle": "Track consistency, completed lessons, and weekly streaks.",
        "cards": [
            {"name": "Daily Streak", "detail": "Keep your momentum with short daily goals."},
            {"name": "Course Completion", "detail": "See overall progress per module."},
            {"name": "Skill Heatmap", "detail": "Identify strong and weak areas."},
            {"name": "Milestones", "detail": "Unlock badges for completed checkpoints."},
        ],
    },
    "more": {
        "title": "More Tools",
        "subtitle": "Extra learning resources to support your coding journey.",
        "cards": [
            {"name": "Cheat Sheets", "detail": "Quick references for Python syntax."},
            {"name": "Bookmarks", "detail": "Save lessons and snippets for later."},
            {"name": "Study Planner", "detail": "Create and manage your weekly plan."},
            {"name": "Community Help", "detail": "Find answers and peer support."},
        ],
    },
}


LESSONS = [
    {
        "slug": "python-introduction",
        "title": "Python Introduction",
        "tone": "teal",
        "done": 2,
        "total": 10,
        "summary": "Understand what Python is and write your first commands.",
        "duration": "12 min",
        "sections": [
            {
                "heading": "What Python is",
                "points": [
                    "Python is a readable, beginner-friendly programming language.",
                    "It is used for web apps, data analysis, automation, and AI.",
                ],
            },
            {
                "heading": "First program",
                "points": [
                    "Use print() to show output.",
                    "Run your script and check the output in terminal.",
                ],
            },
        ],
        "exercise": {
            "task": "Print your name and favorite subject in two lines.",
            "starter": "print('Your name')\nprint('Favorite subject')",
        },
    },
    {
        "slug": "variables-and-data-types",
        "title": "Variables and Data Types",
        "tone": "indigo",
        "done": 3,
        "total": 10,
        "summary": "Store values in variables and understand core Python types.",
        "duration": "15 min",
        "sections": [
            {
                "heading": "Variables",
                "points": [
                    "Variables are names that hold values.",
                    "Example: age = 20 stores an integer.",
                ],
            },
            {
                "heading": "Data types",
                "points": [
                    "Common types: int, float, str, bool.",
                    "Use type(value) to inspect type.",
                ],
            },
        ],
        "exercise": {
            "task": "Create variables for your name, age, and whether you are a student.",
            "starter": "name = 'Ava'\nage = 20\nis_student = True",
        },
    },
    {
        "slug": "control-flow",
        "title": "Control Flow",
        "tone": "pink",
        "done": 1,
        "total": 10,
        "summary": "Use if/elif/else to control decisions in your program.",
        "duration": "14 min",
        "sections": [
            {
                "heading": "Conditional logic",
                "points": [
                    "if runs when condition is true.",
                    "elif checks another condition.",
                    "else handles all remaining cases.",
                ],
            }
        ],
        "exercise": {
            "task": "Write a program that prints 'Pass' if marks >= 40, otherwise 'Fail'.",
            "starter": "marks = 56\nif marks >= 40:\n    print('Pass')\nelse:\n    print('Fail')",
        },
    },
    {
        "slug": "functions",
        "title": "Functions",
        "tone": "green",
        "done": 4,
        "total": 10,
        "summary": "Group reusable logic with functions and parameters.",
        "duration": "16 min",
        "sections": [
            {
                "heading": "Defining functions",
                "points": [
                    "Use def to create a function.",
                    "Parameters pass input values.",
                    "return sends a result back.",
                ],
            }
        ],
        "exercise": {
            "task": "Create a function add(a, b) that returns the sum.",
            "starter": "def add(a, b):\n    return a + b",
        },
    },
    {
        "slug": "strings",
        "title": "Strings",
        "tone": "rose",
        "done": 2,
        "total": 10,
        "summary": "Work with text using indexing, slicing, and methods.",
        "duration": "13 min",
        "sections": [
            {
                "heading": "String basics",
                "points": [
                    "Strings are text values in quotes.",
                    "Use len(text) for length and text.upper() for uppercase.",
                ],
            }
        ],
        "exercise": {
            "task": "Take a name and print it in uppercase.",
            "starter": "name = 'code pulse'\nprint(name.upper())",
        },
    },
    {
        "slug": "lists",
        "title": "Lists",
        "tone": "purple",
        "done": 1,
        "total": 10,
        "summary": "Store multiple values in order and update them easily.",
        "duration": "15 min",
        "sections": [
            {
                "heading": "List operations",
                "points": [
                    "Create with square brackets: [1, 2, 3].",
                    "Use append() to add and remove() to delete values.",
                ],
            }
        ],
        "exercise": {
            "task": "Create a list of 3 subjects and append one more.",
            "starter": "subjects = ['Math', 'Physics', 'Chemistry']\nsubjects.append('Python')",
        },
    },
]


def _lesson_with_progress(lesson):
    lesson_data = dict(lesson)
    lesson_data["progress"] = int((lesson_data["done"] / lesson_data["total"]) * 100)
    return lesson_data


def home(request):
    lessons = [_lesson_with_progress(lesson) for lesson in LESSONS]

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
            "app_name": "Code Pulse",
            "lessons": lessons,
            "quick_access": quick_access,
        },
    )


def feature_page(request, page_key):
    page = FEATURE_PAGES.get(page_key)
    if not page:
        return home(request)

    return render(
        request,
        "learn/feature_page.html",
        {
            "app_name": "Code Pulse",
            "title": page["title"],
            "subtitle": page["subtitle"],
            "cards": page["cards"],
        },
    )


def lessons(request):
    lesson_items = [_lesson_with_progress(lesson) for lesson in LESSONS]
    return render(
        request,
        "learn/lessons.html",
        {
            "app_name": "Code Pulse",
            "title": "Lesson Map",
            "subtitle": "Pick a lesson and continue where you left off.",
            "lessons": lesson_items,
        },
    )


def lesson_detail(request, slug):
    lesson = next((item for item in LESSONS if item["slug"] == slug), None)
    if lesson is None:
        raise Http404("Lesson not found")

    return render(
        request,
        "learn/lesson_detail.html",
        {
            "app_name": "Code Pulse",
            "lesson": _lesson_with_progress(lesson),
        },
    )
