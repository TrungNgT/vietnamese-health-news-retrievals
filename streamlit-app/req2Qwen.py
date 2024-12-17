import requests
import json
from openai import OpenAI

baseUrl = "https://f47f-35-185-254-25.ngrok-free.app"
url = baseUrl + "/v1/chat/completions"
API_KEY = "EMPTY"

qwenAssist = OpenAI(
    base_url= baseUrl + "/v1",
    api_key= API_KEY
)

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}",
}

# create json data-prompt for curl post requests
def makeData(prompt: str) : 
    data = {
        "model": "Qwen/Qwen2.5-1.5B-Instruct",
        "messages": 
        [
            {
            "role": "system",
            "content": prompt,
            }
        ]
    }
    return data

def Qwen(prompt: str, userInput: str) :
    
    response = qwenAssist.chat.completions.create(
        model= "Qwen/Qwen2.5-1.5B-Instruct",
        messages= [
            {"role": "system",
             "content": prompt},
            {"role": "user",
             "content": userInput}
        ]
    )
    
    # data = makeData(prompt)
    # post with curl requests
    # response = requests.post(url, headers=headers, data=json.dumps(data))
    #if (response.status_code == 200) :
    #    print("Request was successful!")
    #    #print("Response JSON:", response.json())
    #    dt = response.json()
    #    text = dt['choices'][0]['message']['content']
        
    #    return text
    #else :
    #    print(f"Request failed with status code {response.status_code}")
    #    print("Response Text:", response.text)
    
    return response.choices[0].message.content
    
#print(Qwen("ngày nô en ở Việt Nam là ngày nào? nó có phải ngày Christmas không? "))