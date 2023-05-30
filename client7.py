# Python program to translate
# speech to text and text to speech

import socket
import ssl
import threading as th

import speech_recognition as sr

from enter_screen1 import Ui_startWindow, show_win
from log_in_screen1 import Ui_LogInWindow, show_window
from ready_screen import Ui_readyWindow, show_ready_window
from sign_in_screen import Ui_signUpWindow, show_sign_window
from game_screen1 import Ui_gameWindow, show_game

context = ssl.create_default_context()
# Set the context to not verify the server's SSL/TLS certificate
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE


class Client:

    def __init__(self, server_socket):
        self.socket = server_socket
        self.screen_state = -1
        self.first_name = ""
        self.last_name = ""
        self.username = ""
        self.password = ""
        self.client_ready = False
        self.client_singed = False
        self.game_start = False


def create_msg(data1, cmd):
    data_len = len(data1)
    data_len_len = len(str(data_len))
    data_len = str(data_len)
    for i in range(4 - data_len_len):
        data_len = "0" + data_len
    return cmd + data_len + data1


def handle_msg(client_socket):
    data_len_received = client_socket.recv(4).decode()
    data_received = client_socket.recv(int(data_len_received)).decode()
    return data_received


def voice_to_text():
    global MyText
    r = sr.Recognizer()
    try:
        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            try:
                audio2 = r.listen(source2, 5, 3)
                MyText = r.recognize_google(audio2)
                print(MyText)
            except:
                print("error")
                pass
            # Using google to recognize audio


    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")


categories_milon = {
    "country": 0,
    "capital": 1,
    "boy": 2,
    "movie": 3,
    "animal": 4,
    "fruit/vegetable": 5,
    "household item": 6,
}
ans = " "
closeFunc = False
MyText = ""
counterOfText = 0
buf = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8820))
s = context.wrap_socket(s, server_hostname='127.0.0.1')
socket_running = True
client7 = Client(s)
start_window = Ui_startWindow(client7)
game_window = Ui_gameWindow(client7)
round_num = 0

try:
    show_win(start_window)
except:
    pass

while client7.screen_state == -1:
    pass
if client7.screen_state == 0:
    sign_in_window = Ui_signUpWindow(client7)
    try:
        print("before")
        e = th.Thread(target=show_sign_window, args=(sign_in_window,))
        print("after")
        e.start()
        print("after2")
    except:
        pass
    while client7.username == "":
        pass
    s.send(("username:" + client7.username).encode())
    current_username = client7.username
    data = s.recv(1024).decode()
    print(data)
    while "taken" in data:
        sign_in_window.username_taken.show()
        while client7.username == current_username:
            pass
        s.send(("username:" + client7.username).encode())
        data = s.recv(1024).decode()
    userInfo = client7.username + " " + client7.first_name + " " + client7.last_name + " " + client7.password
    client7.client_singed = True
    s.send(userInfo.encode())
    data = s.recv(1024).decode()
    print(" fgbfgb" + data)
elif client7.screen_state == 1:
    log_in_window = Ui_LogInWindow(client7)
    try:
        e = th.Thread(target=show_window, args=(log_in_window,))
        e.start()
    except:
        pass
    while client7.username == "":
        pass
    s.send(("usernameold:" + client7.username).encode())
    old_username = client7.username
    data = s.recv(1024).decode()

    while "found." in data:
        log_in_window.label_2.show()
        while client7.username == old_username:
            pass
        s.send(("username:" + client7.username).encode())
        old_username = client7.username
        data = s.recv(1024).decode()
    s.send(("password:" + client7.password).encode())
    old_password = client7.password
    data = s.recv(1024).decode()
    print("asdds" + data)
    while "wrong:" in data:
        log_in_window.label_2.show()
        while client7.password == old_password:
            pass
        old_password = client7.password
        s.send(("password:" + client7.password).encode())
        data = s.recv(1024).decode()
        print(data)
    client7.client_singed = True
ready_window = Ui_readyWindow(client7)
try:
    w = th.Thread(target=show_ready_window, args=(ready_window,))
    w.start()
except:
    pass
while socket_running:
    client7.client_ready = False
    round_num = 0
    client7.screen_state = 2
    client7.game_start = False
    while client7.client_ready is False:
        pass
    s.send("ready: indeed".encode())
    client7.screen_state = 3
    try:
        t1 = th.Thread(target=show_game, args=(game_window,))
        t1.start()
    except:
        pass
    while round_num < 3:
        print("start round" + str(round_num + 1))
        if round_num == 0:
            while game_window.opened is False:
                pass
            try:
                t3 = th.Thread(target=game_window.waiting_for_players)
                t3.start()
            except:
                pass
        round_num += 1
        # try:
        #     t1 = th.Thread(target=game_window.start_round)
        #     t1.start()
        # except:
        #     pass
        print("wait letter round " + str(round_num))
        data = s.recv(1024).decode()
        print(data + " data 4")
        while "The letter is:" not in data:
            data = s.recv(1024).decode()
        client7.game_start = True
        letter = data.split(":")[1]
        game_window.set_letter(round_num, letter)
        game_window.game_table.update()
        ans = " "
        while "finished@" not in ans:
            print(ans)
            MyText = " "
            voice_to_text()
            s.send(MyText.encode())
            ans = s.recv(buf).decode()
            if "you " in ans:
                ans_list = ans.split(":")
                cat_list = ans.split("?")
                for i in range(int(len(ans_list) / 2)):
                    # table in row round num, coloum category dictionary = ans list 1+2i
                    game_window.insert_value(categories_milon[cat_list[1 + 2 * i]], round_num, ans_list[1 + 2 * i])
                    game_window.game_table.update()
                    print("put value")

        print(ans)
        s.send("game done:".encode())
    game_window.continue_button.show()
    while client7.screen_state == 3:
        pass
    ready_window.ready_button.show()
    ready_window.waiting_text.hide()
    ready_window.dot1.hide()
    ready_window.dot2.hide()
    ready_window.dot3.hide()
