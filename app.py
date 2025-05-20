
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



dob=st.date_input("생년월일 선택", datetime.date(2000,1,1))


gender=st.radio("성별을 선택하세요",["남","여"])

subject=st.selectbox("좋아하는 과목",["파이썬","자바","리액트"])

agree=st.checkbox("약관에 동의합니다")


if st.button("확인"):
    st.success(f"{name}님 ,{age}세, {gender} 선택완료")



uploaded_file=st.file_uploader("파일을 업로드 하세요",type=["txt","csv"])

if uploaded_file:
    st.text("업로드된 파일 내용:")
    st.text(uploaded_file.read().decode("utf-8"))


st.success("성공 메시지입니다.")
st.info("정보 메세지")
st.warning("경고 메시지")
st.error("에러메시지")