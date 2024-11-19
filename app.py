'''from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
import pandas as pd
# Load Excel data
university_data = pd.ExcelFile("data4.xlsx")
courses_df = university_data.parse("Courses")
cdf= courses_df.map(lambda x: x.lower() if isinstance(x, str) else x)
teachers_df = university_data.parse("Teachers")
tdf= teachers_df.map(lambda x: x.lower() if isinstance(x, str) else x)
timetable_df = university_data.parse("Timetable")
timedf= timetable_df.map(lambda x: x.lower() if isinstance(x, str) else x)
references_df = university_data.parse("References")
refdf=references_df.map(lambda x: x.lower() if isinstance(x, str) else x)
print(refdf)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_input = request.form['msg']
    # Use your chatbot response function here
    bot_response = chatbot_response(user_input)
    return jsonify({"response": bot_response})


def try2(inp):
    return inp
def chatbot_response(user_input):
    # For simplicity, let's use a basic rule-based chatbot.
    from nltk.chat.util import Chat, reflections

    pairs = [
        (r"hi|hello", ["Hello!", "Hi, how can I help you today?"]),
        (r"how are you?", ["I'm good, thank you!", "I'm doing well, how about you?"]),
        (r"(.*)", [lambda user_input: try2(user_input)]),
    ]
    chatbot = Chat(pairs, reflections)
    return chatbot.respond(user_input)

if __name__ == '__main__':
    app.run(debug=True)'''

#attempt 2

'''from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

# Example function to process user input dynamically
def try2(inp):
    return f"You entered: {inp}. This is a dynamic response!"

# Custom Chat class to handle callable responses
class CustomChat(Chat):
    def respond(self, statement):
        for pattern, response_list in self._pairs:
            match = self._match(pattern, statement)
            if match:
                response = response_list[0]
                if callable(response):
                    return response(statement)  # Call the function with the input
                return self._select_response(response_list, match)
        return None

# Chatbot logic
def chatbot_response(user_input):
    pairs = [
        (r"hi|hello", ["Hello!", "Hi, how can I help you today?"]),
        (r"how are you?", ["I'm good, thank you!", "I'm doing well, how about you?"]),
        (r"(.*)", [lambda user_input: try2(user_input)]),
    ]
    chatbot = CustomChat(pairs, reflections)
    return chatbot.respond(user_input)

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_input = request.form.get('msg', '')  # Get the message from the form
    bot_response = chatbot_response(user_input)
    return jsonify({"response": bot_response})  # Return the bot response as JSON

# Run the app
if __name__ == '__main__':
    app.run(debug=True)'''

#attempt3

'''from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections
import re  # For regex matching

app = Flask(__name__)

# Example function to process user input dynamically
def try2(inp):
    return f"You entered: {inp}. This is a dynamic response!"

# Custom Chat class to handle callable responses
class CustomChat(Chat):
    def __init__(self, pairs, reflections):
        super().__init__(pairs, reflections)

    def respond(self, statement):
        for pattern, response_list in self._pairs:
            match = re.match(pattern, statement)  # Use re.match for regex
            if match:
                response = response_list[0]
                if callable(response):
                    return response(statement)  # Call the function with the input
                return self._select_response(response_list, match.groups())
        return None

# Chatbot logic
def chatbot_response(user_input):
    pairs = [
        (r"hi|hello", ["Hello!", "Hi, how can I help you today?"]),
        (r"how are you?", ["I'm good, thank you!", "I'm doing well, how about you?"]),
        (r"(.*)", [lambda user_input: try2(user_input)]),
    ]
    chatbot = CustomChat(pairs, reflections)
    return chatbot.respond(user_input)

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_input = request.form.get('msg', '')  # Get the message from the form
    bot_response = chatbot_response(user_input)
    return jsonify({"response": bot_response})  # Return the bot response as JSON

# Run the app
if __name__ == '__main__':
    app.run(debug=True)'''

from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections
import random  # For random response selection
import re  # For regex matching
import pandas as pd
# Load Excel data
university_data = pd.ExcelFile("data4.xlsx")
courses_df = university_data.parse("Courses")
cdf= courses_df.map(lambda x: x.lower() if isinstance(x, str) else x)
teachers_df = university_data.parse("Teachers")
tdf= teachers_df.map(lambda x: x.lower() if isinstance(x, str) else x)
timetable_df = university_data.parse("Timetable")
timedf= timetable_df.map(lambda x: x.lower() if isinstance(x, str) else x)
references_df = university_data.parse("References")
refdf=references_df.map(lambda x: x.lower() if isinstance(x, str) else x)

app = Flask(__name__)

# Example function to process user input dynamically
def try2(inp):
    #return f"You entered: {inp}. This is a dynamic response!"
    i1 = inp.lower()  # Convert input to lowercase for case-insensitive matching.
    finale = None

    # Check for teacher-related queries
    if "teacher" in i1 or "professor" in i1:
        name = ""
        for teacher_name in tdf["Name"]:
            if teacher_name.lower() in i1:
                name = teacher_name
                break

        if name:  # If a teacher's name is found
            # finale = tdf.loc[tdf["Name"] == name]
            # finale=f"Professor {tdf.loc[tdf["Name"]==name]["Name"]} teaches {tdf.loc[tdf["Name"]==name]["Department"]}, contact number is {tdf.loc[tdf["Name"]==name]["Contact Number"]}, email is {tdf.loc[tdf["Name"]==name][""]}"
            # name=tdf.loc[tdf["Name"]==name]["Name"]
            dept = list(tdf.loc[tdf["Name"] == name]["Department"])[0]
            # print(dept)
            cn = list(tdf.loc[tdf["Name"] == name]["Contact Number"])[0]
            # print(cn)
            email = list(tdf.loc[tdf["Name"] == name]["Email"])[0]
            # print(email)
            oh = list(tdf.loc[tdf["Name"] == name]["Office Hours"])[0]
            # print(oh)
            finale = f"Professor {name} teaches {dept}, contact number is {cn}, email is {email} and has classes on {oh}"

        else:
            return "Teacher not found in database."
            # print("Teacher not found in database.")
            # return ""

    # Check for timetable-related queries
    elif "timetable" in i1:
        course, sem = "", ""
        for course_option in timedf["Course"]:
            if course_option.lower() in i1:
                course = course_option
                break

        for sem_option in timedf["Semester"]:
            if sem_option.lower() in i1:
                sem = sem_option
                break

        if course and sem:
            # c=timedf.loc[timedf["Course"]==course][[timedf["Semester"]==sem]]["Timetable"][0]
            tt = list(timedf[(timedf["Course"] == course) & (timedf["Semester"] == sem)][["Timetable"]]['Timetable'])[0]

            rn = list(timedf[(timedf["Course"] == course) & (timedf["Semester"] == sem)][["Room"]]['Room'])[0]
            finale = f"The timetable for course {course} in {sem} semester is {tt} in {rn}"

        else:
            return "Course or semester not found in timetable data."
            # print("Course or semester not found in timetable data.")
            return ""

    # Check for reference material-related queries
    elif "reference" in i1:
        course, sub = "", ""
        for course_option in refdf["Course"]:
            if course_option.lower() in i1:
                course = course_option
                break

        for subject_option in refdf["Subject"]:
            if subject_option.lower() in i1:
                sub = subject_option
                break

        if course and sub:
            rl = list(refdf[(refdf["Course"] == course) & (refdf["Subject"] == sub)][["Reference Material Link"]][
                          "Reference Material Link"])[0]
            # finale = refdf[(refdf["Course"] == course) & (refdf["Subject"] == sub)][["Reference Material Link"]]
            finale = f"for the {course}, the material for {sub} is {rl}"
        else:
            return "Course or subject not found in reference material data."
            # print("Course or subject not found in reference material data.")
            # return ""

    # Handle general queries
    '''else:
        course, sub, sem = "", "", ""
        for course_option in cdf["Course"]:
            if course_option.lower() in i1:
                course = course_option
                break

        for subject_option in cdf["Subject"]:
            if subject_option.lower() in i1:
                sub = subject_option
                break

        for sem_option in cdf["Semester"]:
            if sem_option.lower() in i1:
                sem = sem_option
                break

        if course and sub and sem:
            finale = cdf[(cdf["Course"] == course) & (cdf["Subject"] == sub) & (cdf["Semester"] == sem)]
        else:
            return "Relevant information not found in course data."
            #print("Relevant information not found in course data.")
            #return ""
            '''

    return finale

# Custom Chat class to handle callable responses
class CustomChat(Chat):
    def __init__(self, pairs, reflections):
        super().__init__(pairs, reflections)

    def respond(self, statement):
        for pattern, response_list in self._pairs:
            match = re.match(pattern, statement)  # Use re.match for regex
            if match:
                response = response_list[0]
                if callable(response):
                    return response(statement)  # Call the function with the input
                return random.choice(response_list)  # Randomly select a response
        return "Sorry, I didn't understand that."

# Chatbot logic
def chatbot_response(user_input):
    pairs = [
        (r"hi|hello", ["Hello!", "Hi, how can I help you today?"]),
        (r"how are you?", ["I'm good, thank you!", "I'm doing well, how about you?"]),
        (r"(.*)", [lambda user_input: try2(user_input)]),
    ]
    chatbot = CustomChat(pairs, reflections)
    return chatbot.respond(user_input)

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_input = request.form.get('msg', '')  # Get the message from the form
    bot_response = chatbot_response(user_input)
    return jsonify({"response": bot_response})  # Return the bot response as JSON

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

