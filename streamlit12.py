import pandas as pd
import streamlit as st
st.sidebar.text_input("输入API")
model = st.sidebar.selectbox("选择模型", ['glm-3-turbo', 'glm-4'])
max_tokens=st.sidebar.slider("max_tokexs", 0, 2000, value=512)
temperature=st.sidebar.slider("temperature", 0.0, 1.0, value=0.8)
st.session_state.message=[
    {"role": "assistant", "content": "你好我是CHATGLM，有什么可以帮助您的吗？"},
    {"role": "user", "content": "你好"}
]
for message in st.session_state.message:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt=st.chat_input()