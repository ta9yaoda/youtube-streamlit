import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プレグレスバーの表示')
'Start!!'

latest_iteration = st.empty()  # 表示したときにbarの上にlatest_iterationを表示させる（位置関係を設定）
bar = st.progress(0)  # 一旦0を指定しておく、特別な意味はない

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)  # barを100段階ですこしずつ進めていく
    time.sleep(0.1)  # すこしずつfor文の代入を進めていく、for文が完了するとfor文以下のコードが実行される

'Done!!!'

# ページを2columnにする
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

# expanderを作成する
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')
# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'あなたの趣味：', text
# 'コンディション：', condition

# if st.checkbox('Show Image'):
#     img = Image.open('sample.jpg')
#     st.image(img, caption='Takuya Odagiri', use_column_width=True)
