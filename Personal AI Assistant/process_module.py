from output_module import output
from timing_module import get_time
from database import get_answer, insert_questionAndanswer
from input_module import ask_something
from internet import check_internet_connection, open_browser, open_browser_and_search

def process(query):
    answer = get_answer(query)
    if answer == "get time details":
        return "The Time Is " + get_time()
    elif answer == "check internet connection":
        if check_internet_connection():
            return "Your Internet Is Connected"
        else:
            return "Your internet is not connected"
    elif answer == "open browser":
        open_browser()
        return "Opening Browser"
    elif answer == "search the web":
        open_browser_and_search()
        return "Searching the Web"
    else:
        output("I don't know what that means. Can you please explain?")
        return learn_new_command(query)

def learn_new_command(query):
    user_explanation = ask_something().lower()
    if "it means" in user_explanation:
        clean_explanation = user_explanation.replace("it means", "").strip()
        value = get_answer(clean_explanation)
        if value == "":
            return "Sorry, I can't help with this."
        else:
            insert_questionAndanswer(query, value)
            return "Thanks, I will keep this in mind."
    return "I still don't understand. Let's try something else."

