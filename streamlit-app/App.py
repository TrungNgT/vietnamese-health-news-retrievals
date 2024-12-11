import streamlit as st
from req2Qwen import Qwen
from req2Elastic import retrieve

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .main {
        max-width: 90%;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Set the title of the app
st.title('Chat with Vinmec News')

# Create a text input field
user_input = st.text_input('Enter something:', '')

if user_input : 
    contexts = retrieve(user_input)

    prompt = "Nhập vai: Bạn là 1 Bác sĩ tư vấn sức khỏe tổng quát hàng đầu ở Việt Nam.\n"
    prompt += f"Bệnh nhân của bạn có đưa ra một câu hỏi như sau: {user_input}.\n"
    prompt += "Dưới đây là 4 bài viết có thể có liên quan đến câu hỏi bên trên.\n"
    #prompt += "Bằng kiến thức chuyên môn của bạn, có thể sử dụng thông tin trong 4 bài viết tham khảo sau và đưa ra một câu trả lời thỏa đáng:\n"

    i = 1
    for context in contexts :
        prompt += f"\n\n\nBài viết thứ {i} :"
        i += 1
        prompt += context
        prompt += '\n'

    prompt += "Với các tri thức bổ sung trên, kết hợp với kiến thức chuyên môn của bạn để có thể đưa ra câu trả lời BẰNG TIẾNG VIỆT cho bệnh nhân."
    
    # log the prompt:
    with open("../prompts_log.txt", mode="w", encoding='utf-8') as file :
        file.write(prompt)
        file.write("\n\n####################################################################################\n\n")

# Handle and display the input
# if user_input:
#    print(prompt)
#    out_put = Qwen(prompt=prompt)
#    st.write(out_put)
# else:
#    st.write('Please enter something in the text field.')



if user_input: 
    col1, col2 = st.columns(2)

    with col1 :
        st.header("Chat without Retrievals")
        out_put = Qwen(prompt="", userInput=user_input)
        st.write(out_put)
    
    with col2 :
        st.header("Chat with Retrievals")
        out_put = Qwen(prompt=prompt, userInput=user_input)
        st.write(out_put)
else :
    st.write("Please enter something in the text field.")
