import base64
import requests

# OpenAI API Key
with open("openai.key", "r") as f:
    key, API_KEY = f.readline().rstrip().split("=")
    key, ORGANIZATION = f.readline().rstrip().split("=")

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "desk2.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {API_KEY}"
}
class_a = "0: phone, 1: pencil, 2: glasses, 3: book."
class_b = "0:headphone, 1: keyboard, 2: mouse, 3: pen, 4: note"
payload = {
  "model": "gpt-4-vision-preview",
  "messages": [
    {
      "role": "system",
      "content": f"""You are robot pilot. But you have to know where the object is.
        You can use python file that contains pretrained YOLO model.
        The file's name is detect.py.
        There are three classes that you can detect.
        {class_b}
        If i give you an image that contains one of these classes, you have to detect object with using that python file.
        use this  prompt to answer.
        ```sh\npython detect.py --classes [class_numbers]```""",
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Can you give me that left of me?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    },
    {
      "role": "assistant",
      "content": "```sh\npython detect.py --classes 2```"
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Can you give me that?? I want to listen to music"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ]
}
response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
print(response.json()['choices'][0])
payload["messages"][3]['content'][0]['text'] = "Can you give me that gray and small one??"
response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
print(response.json()['choices'][0])
