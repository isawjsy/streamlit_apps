import streamlit as st
import pandas as pd
table=pd.DataFrame({"Column 1": [1,2,3,4,5,6,7], "Column 2": [11,12,13,14,15,16,17]})

st.title(' Hi! I am Streamlit WebApp \n 안녕하세요! 스트림릿 웹앱')
st.subheader("Hi! I am Your Subheader")
st.header("I am Header")
st.text("Hi I am Text function and programmers uses")
st.markdown("# 1 Hello World!")
st.markdown("## 2 Hello World!")
st.markdown("### 3 Hello World!")
st.markdown("#### 4 Hello World!")
st.markdown("[google](https://google.com)")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

st.write("## H2")
st.metric(label="Wind Speed", value="120ms⁻¹", delta="-1.4ms⁻¹")
st.table(table)

#st.image("image.png", caption="This is my image", width=300)
#st.audio("BFC_MP_2.mp3")
#st.video("y2mate.com - Blender  Make A Short Movie Part 1 BEGINNERS_1080p.mp4")

# Streamlit 상단 우측의 ... 버튼 없애기: 크롬에서 F12 누르고, ... 버튼에 해당하는 class 이름을 찾아서 적어줌. 공백에는. 입력
st.markdown("""

<style>
.st-emotion-cache-czk5ss.e16jpq800
{
    visibility: hidden; 
}
</style/>
""", unsafe_allow_html=True)

