import streamlit as st
from docx import Document
import io

st.title("Thay thế từ trong file Word")

# Bước 1 & 2
old_word = st.text_input("Nhập từ cần thay thế")
new_word = st.text_input("Nhập từ viết tắt")

# Bước 3
uploaded_file = st.file_uploader("Upload file Word (.docx)", type=["docx"])

if st.button("Chạy") and uploaded_file and old_word and new_word:
    doc = Document(uploaded_file)

    for para in doc.paragraphs:
        if old_word in para.text:
            para.text = para.text.replace(old_word, new_word)

    # Lưu file vào bộ nhớ
    file_stream = io.BytesIO()
    doc.save(file_stream)
    file_stream.seek(0)

    st.success("Hoàn thành!")
    st.download_button(
        label="Tải file Word đã thay thế",
        data=file_stream,
        file_name="output.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
