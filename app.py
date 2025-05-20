
import streamlit as st
import datetime


st.title("제목입니다")
st.header("헤더입니다.")
st.subheader("서브헤더")
st.write("일반텍스트")
st.markdown("**굵게**,*기울임*,`코드`")
st.markdown("**굵게**,*기울임*,`코드`")
st.markdown("**굵게**,*기울임*,`코드`")
st.markdown("**굵게**,*기울임*,`코드`")


name = st.text_input("이름을 입력하세요")

age=st.number_input("나이를 입력하세요",min_value=0,max_value=120,value=20)




