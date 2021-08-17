import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')


st.write('DataFrame')

df = pd.DataFrame({
    '1列目' : [1, 2, 3, 4],
    '2列目' : [10, 20, 30, 40]
})

st.write(df)
st.dataframe(df.style, width=100,height=100)
st.dataframe(df.style.highlight_max(axis=0))
st.table(df.style.highlight_max(axis=0))

"""
# 章a
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns = ['a', 'b', 'c']
)
st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)

df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50,50]+[35.69,139.70],
    columns = ['lat', 'lon']
)

st.map(df3)


st.write('Display Image')
#img = Image.open('sample_image.jpeg')
#st.image(img, caption='tiger',use_column_width=True)

#if st.checkbox('Show Image'):
#    img = Image.open('sample_image.jpeg')
#    st.image(img, caption='tiger',use_column_width=True)


option = st.selectbox(
    'あなたが好きな数字を教えて下さい。',
    list(range(1,11))
)
'あなたの好きな数字は、',option,'です。'


st.write('Interactive Wigets')

text = st.text_input('あなたの趣味を教えて下さい。')
'あなたの趣味：', text

condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：' ,condition