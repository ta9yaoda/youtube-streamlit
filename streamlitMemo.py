import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.dataframe(df, width=500, height=500)  # writeではサイズ指定ができない

# highlight_maxで最大値の行をハイライト、axis=0は各列で比較、axis=1は各行で比較
st.dataframe(df.style.highlight_max(axis=0))
st.table(df.style.highlight_max(axis=0))  # Staticな表になる

# マークダウン記法の解説、発展編はStreamlit>documentation>API reference>Text elementsのst.markdown
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

# 折れ線グラフを書く、発展編はStreamlit>documentation>API reference>chart elements
df = pd.DataFrame(              # 辞書型{}不要なので削除
    np.random.rand(20, 3),       # 正規分布を基に20×3の表に乱数を生成する
    columns=['a', 'b', 'c']
)
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)  # 棒グラフ

# 新宿付近の座標情報をプロット、発展編はStreamlit>documentation>API reference>chart elements
df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(df)

# 画像を読み込む、冒頭にfrom PIL import Imageを記載する
img = Image.open('sample.jpg')
# 左記のuse_column_width=Trueは実際のレイアウトの横幅に合わせて表示してくれる
st.image(img, caption='Takuya Odagiri', use_column_width=True)

# チェックボックスにチェックを入れたら画像を表示
if st.checkbox('Show Image'):
    img = Image.open('sample.jpg')
    st.image(img, caption='Takuya Odagiri', use_column_width=True)


# select boxを作る、発展編はStreamlit>documentation>API reference>Input WidgetsのDisplay.interactive widgets
option = st.selectbox(  # option変数にselectboxを格納
    'あなたが好きな数字を教えてください、',
    list(range(1, 11))  # 1-10の数字一覧をリストで表示
)
'あなたの好きな数字は、', option, 'です。'

# text boxを作る、発展編はStreamlit>documentation>API reference>Input WidgetsのDisplay.interactive widgets
text = st.text_input('あなたの趣味を教えてください。', value="")
'あなたの趣味：', text

# スライダーを作る
condition = st.slider('あなたの今の調子は？', 0, 100, 50)  # 50は初期値
'コンディション：', condition

# textbox, sliderをsidebarに追加する場合
text = st.sidebar.text_input('あなたの趣味を教えてください。')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
'あなたの趣味：', text
'コンディション：', condition

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

# progress barの表示、冒頭にimport timeを記載する
'Start!!'
latest_iteration = st.empty()  # 表示したときにbarの上にlatest_iterationを表示させる（位置関係を設定）
bar = st.progress(0)  # 一旦0を指定しておく、特別な意味はない

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)  # barを100段階ですこしずつ進めていく
    time.sleep(0.1)  # すこしずつfor文の代入を進めていく、for文が完了するとfor文以下のコードが実行される
'Done!!!'
