text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
#textのコンマとピリオドを削除する
text = text.replace(",","").replace(".","")
#空白で分割する
text_list = text.split()
#数える
count = "".join(map(str,map(len, text_list)))
answer = int(count)
print(answer)