from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<words>")
def game(words):
    # 콤마로 단어 구분하여 정답 단어 리스트로 저장
    # answerlist = ["사과", "자전거"]
    answerlist = words.split(",")

    # 단어가 섞여서 리스트로 저장됨
    # words_shuffled_lists = [["과","사"], ["거", "자", "전"]]
    words_shuffled_lists = []
    for word in answerlist:
        word_characters = list(word)
        random.shuffle(word_characters)
        words_shuffled_lists.append(word_characters)

    # answerlist, word_shuffled_lists를 합친 dictionary 생성
    content_wrap_dic = dict(zip(answerlist, words_shuffled_lists))
    return render_template("game.html", answerlist=answerlist, content_wrap_dic=content_wrap_dic)

if __name__ == "__main__":
    app.run()