import telebot
import random
import threading
import time
from telebot import types
# weka token ya bot apa
bot = telebot.TeleBot("6733585010:AAGywZFsAnz_kdUiomEFnnU_Kcjtp0qpnA8")

# hii nayo ni list ya maswali bot itakua inachagua kisha inauliza
tech_quiz_questions = [
        {"question": "What does HTML stand for?",
         "options": ["Hyper Text Markup Language", "High Tech Multi Language", "Hyperlinks and Text Markup Language"],
         "correct_option": 0},
        {"question": "In programming, what does GUI stand for?",
         "options": ["Graphical User Interface", "General Utility Input", "Graph Unit Interface"], "correct_option": 0},
        {"question": "Which company developed the Python programming language?",
         "options": ["Microsoft", "Apple", "Google", "Dropbox", "Python Software Foundation"], "correct_option": 4},
        {"question": "What is the most commonly used programming language for developing Android apps?",
         "options": ["JavaScript", "Swift", "Java", "Kotlin"], "correct_option": 2},
        {"question": "What does CSS stand for in web development?",
         "options": ["Creative Styling Sheets", "Cascading Style Sheets", "Computer Style Sheets"],
         "correct_option": 1},
        {"question": "Which of the following is NOT a version control system?",
         "options": ["Git", "SVN", "Mercurial", "Apache"], "correct_option": 3},
        {"question": "What does API stand for in programming?",
         "options": ["Automatic Programming Interface", "Application Programming Interface",
                     "Automated Parsing Interface"], "correct_option": 1},
        {"question": "Which cloud computing service is provided by Amazon?",
         "options": ["Azure", "Google Cloud", "AWS", "IBM Cloud"], "correct_option": 2},
        {"question": "Which database language is known for its relational model?",
         "options": ["SQL", "NoSQL", "MongoDB", "SQLite"], "correct_option": 0},
        {"question": "What is the main function of a VPN in network security?",
         "options": ["Blocking ads", "Hiding your IP address", "Encrypting internet traffic",
                     "Controlling Wi-Fi signal"], "correct_option": 2}
    ]
BUTTONS = types.InlineKeyboardMarkup(
    [
        [
            types.InlineKeyboardButton(
                text="DEVELOPER", url="https://telegram.me/EscaliBud"),
            types.InlineKeyboardButton(
                text="CHANNEL", url="https://t.me/InfinityHackersKE")
        ]
    ]
)
@bot.message_handler(commands=['start'])
def send_start_message(message):
    wlcmsg = """

Hello there !!
Am a simple bot to entertain your channel subscribers with some polls.
Currently am able to send only tech related questions.
Join my developers channel for my source code @InfinityHackersKE              
                 """
    bot.send_message(message.chat.id, wlcmsg, reply_markup = BUTTONS)



# Function ya kutuma hizo maswali ziko apo juu
def send_quiz_question():
 quiz_question = random.choice(tech_quiz_questions)
 question_text = quiz_question["question"]
 options = quiz_question["options"]

 answer_correct = quiz_question["correct_option"]

 # Construct poll options
 poll_options = [f"{i+1}. {option}" for i, option in enumerate(options)]

 # Send the quiz question as a poll
 quiz_message = bot.send_poll(chat_id="@Infinityhackerske",
                              question=question_text,
                              type="quiz",
                              correct_option_id=answer_correct,
                              options=poll_options)

 # hii ni ya kueka scores na answers correct😂
 bot_data = bot.get_chat_member(quiz_message.chat.id, quiz_message.from_user.id)
 bot_data.correct_option = answer_correct

 # After 15 minutes,bot inafaa ifute hio poll mzee then itume mpya
 bot.delete_message(chat_id=quiz_message.chat.id, message_id=quiz_message.message_id)

# Function ya kutuma poll ingine after 15 seconds
def schedule_quiz_questions(interval):
 while True:
     send_quiz_question()
     time.sleep(interval)

# hapa ndo una adjust time unataka itume hio poll
quiz_interval =900 # Send a quiz question every 15 minutes
quiz_thread = threading.Thread(target=schedule_quiz_questions, args=(quiz_interval,))
quiz_thread.start()

# Start the bot
bot.polling()