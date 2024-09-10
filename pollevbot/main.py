from pollevbot import PollBot
from pollevbot.config import user, password


def main():
    host = 'PollEverywhere URL Extension e.g. "uwpsych"'

    tfq_answer = True

    mcq_answer = 0   # 0 = A, 1 = B, 2 = C, 3 = D

    frq_answer = "I am a bot."

    # set wait times to 0 if you want to answer polls super fast
    with PollBot(user, password, host, tfq_answer, mcq_answer, frq_answer,
                 login_type="pollev", closed_wait=0, open_wait=0) as bot:
        bot.run()


if __name__ == '__main__':
    main()


# TODO
# 1. Add a GUI
# 2. Make poll bot stop after answering succesfully
# 3. Add pre-answering feature for the three types of questions
