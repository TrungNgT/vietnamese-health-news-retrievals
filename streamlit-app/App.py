import streamlit as st
from req2Qwen import Qwen
from req2Elastic import retrieve

# Set the title of the app
st.title('Chat with Vinmec News Retrievals')

# Create a text input field
user_input = st.text_input('Enter something:', '')

#contexts = retrieve(user_input)

prompt = "Nhập vai: Bạn là 1 Bác sĩ tư vấn sức khỏe tổng quát hàng đầu ở Việt Nam.\n"
prompt += f"Bệnh nhân của bạn có đưa ra một câu hỏi như sau: {user_input}.\n"
#prompt += "Bằng kiến thức chuyên môn của bạn, có thể sử dụng thông tin trong 4 bài viết tham khảo sau và đưa ra một câu trả lời thỏa đáng:\n"

#for context in contexts :
#    prompt += context
#    prompt += '\n'
    
# Handle and display the input
if user_input:
    print(prompt)
    out_put = Qwen(prompt=prompt)
    st.write(out_put)
else:
    st.write('Please enter something in the text field.')
