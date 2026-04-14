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
