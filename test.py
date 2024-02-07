from openai import OpenAI

with open("openai.key", "r") as f:
    key, API_KEY = f.readline().rstrip().split("=")
    key, ORGANIZATION = f.readline().rstrip().split("=")


client = OpenAI(
    # organization=ORGANIZATION,
    api_key=API_KEY
)

response = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
        {"role": "system", "content": """You can use python file that contains pretrained YOLO model.
        The file's name is detect.py.
        There are three classes that you can detect.
        0: pen, 1: eraser, 2: bottle.
        If i give you an image that contains one of these classes, you have to detect object with using that python file.
        use this  prompt to answer.
        ```sh\npython detect.py --classes [class_numbers]```
        """},
        {"role": "user", "content": "How can I detect pen?"},
        {"role": "assistant", "content": "```sh\npython detect.py --classes 0```"},
        {"role": "user", "content": "How can I detect eraser?"}
    ]
)
print(response.choices[0].message)