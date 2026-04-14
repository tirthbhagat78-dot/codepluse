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
    "my-notes": {
        "title": "My Notes",
        "subtitle": "Store your personal notes for each lesson and topic.",
        "cards": [
            {"name": "Lesson Notes", "detail": "Capture key ideas from every lesson."},
            {"name": "Code Snippets", "detail": "Save reusable code blocks."},
            {"name": "Revision List", "detail": "Flag topics for quick review."},
            {"name": "Pinned Notes", "detail": "Keep your most important notes on top."},
        ],
    },
    "cheat-sheets": {
        "title": "Cheat Sheets",
        "subtitle": "Fast-reference cards for Python syntax and core patterns.",
        "cards": [
            {"name": "Syntax Basics", "detail": "Variables, loops, conditions, and functions."},
            {"name": "Data Types", "detail": "Strings, lists, dictionaries, tuples, and sets."},
            {"name": "Methods", "detail": "Most-used string and list methods."},
            {"name": "Error Fixes", "detail": "Common Python errors and quick fixes."},
        ],
    },
    "help-center": {
        "title": "Help Center",
        "subtitle": "Find support topics and troubleshooting guidance.",
        "cards": [
            {"name": "Getting Started", "detail": "Setup help and first steps."},
            {"name": "Account Help", "detail": "Profile, settings, and access support."},
            {"name": "Lesson Issues", "detail": "Fix progress or page issues quickly."},
            {"name": "Contact Support", "detail": "Reach out when you need help."},
        ],
    },
    "bookmarks": {
        "title": "Bookmarks",
        "subtitle": "Access your saved lessons and reference pages.",
        "cards": [
            {"name": "Saved Lessons", "detail": "Open lessons you marked for later."},
            {"name": "Saved Examples", "detail": "Keep useful examples in one place."},
            {"name": "Quick Revisit", "detail": "Jump directly to your focus topics."},
            {"name": "Organize", "detail": "Group bookmarks by topic."},
        ],
    },
    "study-goals": {
        "title": "Study Goals",
        "subtitle": "Set daily and weekly goals to stay consistent.",
        "cards": [
            {"name": "Daily Target", "detail": "Choose how many lessons per day."},
            {"name": "Weekly Goal", "detail": "Track your weekly completion target."},
            {"name": "Consistency Meter", "detail": "See streak and habit progress."},
            {"name": "Goal History", "detail": "Review previous goal performance."},
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
        "quiz": {
            "question": "Which function prints text to the screen in Python?",
            "options": ["echo()", "print()", "show()", "write()"],
            "answer": 1,
            "explanation": "Python uses print() to display output.",
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
        "quiz": {
            "question": "Which is a boolean value in Python?",
            "options": ["'True'", "1", "True", "yes"],
            "answer": 2,
            "explanation": "True (without quotes) is a boolean literal.",
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
        "quiz": {
            "question": "Which keyword handles all remaining conditions?",
            "options": ["if", "then", "else", "elif"],
            "answer": 2,
            "explanation": "else runs when previous if/elif conditions are false.",
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
        "quiz": {
            "question": "Which keyword sends a value back from a function?",
            "options": ["yield", "return", "break", "pass"],
            "answer": 1,
            "explanation": "return sends the function result to the caller.",
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
        "quiz": {
            "question": "What does 'python'.upper() return?",
            "options": ["python", "PYTHON", "Python", "error"],
            "answer": 1,
            "explanation": "upper() converts all characters to uppercase.",
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
        "quiz": {
            "question": "Which method adds a value to the end of a list?",
            "options": ["add()", "append()", "push()", "insert_end()"],
            "answer": 1,
            "explanation": "append() adds one item to the end of a list.",
        },
    },
]


def _get_progress_state(request):
    completed_slugs = set(request.session.get("completed_lessons", []))
    quiz_results = request.session.get("lesson_quiz_results", {})
    return completed_slugs, quiz_results


def _save_progress_state(request, completed_slugs, quiz_results):
    request.session["completed_lessons"] = sorted(completed_slugs)
    request.session["lesson_quiz_results"] = quiz_results
    request.session.modified = True


def _lesson_with_progress(lesson, completed_slugs=None, quiz_results=None):
    lesson_data = dict(lesson)
    completed_slugs = completed_slugs or set()
    quiz_results = quiz_results or {}

    if lesson_data["slug"] in completed_slugs:
        lesson_data["done"] = lesson_data["total"]

    lesson_data["progress"] = int((lesson_data["done"] / lesson_data["total"]) * 100)
    lesson_data["is_completed"] = lesson_data["slug"] in completed_slugs

    quiz_result = quiz_results.get(lesson_data["slug"], {})
    lesson_data["quiz_done"] = bool(quiz_result)
    lesson_data["quiz_correct"] = bool(quiz_result.get("is_correct"))
    lesson_data["quiz_score"] = 100 if lesson_data["quiz_correct"] else 0
    return lesson_data


def _course_metrics(lessons):
    if not lessons:
        return {"overall_progress": 0, "completed_count": 0, "lessons_today": 0}

    completed_count = sum(1 for lesson in lessons if lesson["is_completed"])
    overall_progress = int(sum(lesson["progress"] for lesson in lessons) / len(lessons))
    lessons_today = min(completed_count, 3)
    return {
        "overall_progress": overall_progress,
        "completed_count": completed_count,
        "lessons_today": lessons_today,
    }


def home(request):
    completed_slugs, quiz_results = _get_progress_state(request)
    lessons = [_lesson_with_progress(lesson, completed_slugs, quiz_results) for lesson in LESSONS]
    metrics = _course_metrics(lessons)

    quick_access = [
        {"name": "AI Tutor", "icon": "spark", "url_name": "ai_tutor"},
        {"name": "My Notes", "icon": "note", "url_name": "my_notes"},
        {"name": "Cheat Sheets", "icon": "book", "url_name": "cheat_sheets"},
        {"name": "Help Center", "icon": "help", "url_name": "help_center"},
        {"name": "Bookmarks", "icon": "bookmark", "url_name": "bookmarks"},
        {"name": "Study Goals", "icon": "goal", "url_name": "study_goals"},
    ]

    return render(
        request,
        "learn/home.html",
        {
            "app_name": "Code Pulse",
            "lessons": lessons,
            "quick_access": quick_access,
            "metrics": metrics,
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
    completed_slugs, quiz_results = _get_progress_state(request)
    lesson_items = [_lesson_with_progress(lesson, completed_slugs, quiz_results) for lesson in LESSONS]
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

    completed_slugs, quiz_results = _get_progress_state(request)
    feedback = None

    if request.method == "POST":
        action = request.POST.get("action")
        if action == "complete":
            completed_slugs.add(slug)
            _save_progress_state(request, completed_slugs, quiz_results)
            feedback = {"kind": "success", "text": "Lesson marked as complete."}
        elif action == "quiz":
            selected = request.POST.get("choice")
            if selected is None:
                feedback = {"kind": "error", "text": "Select an answer before submitting the quiz."}
            else:
                is_correct = int(selected) == lesson["quiz"]["answer"]
                quiz_results[slug] = {"is_correct": is_correct}
                _save_progress_state(request, completed_slugs, quiz_results)
                feedback = {
                    "kind": "success" if is_correct else "error",
                    "text": "Correct." if is_correct else "Not quite. Try again.",
                    "explanation": lesson["quiz"]["explanation"],
                }

    return render(
        request,
        "learn/lesson_detail.html",
        {
            "app_name": "Code Pulse",
            "lesson": _lesson_with_progress(lesson, completed_slugs, quiz_results),
            "feedback": feedback,
        },
    )
