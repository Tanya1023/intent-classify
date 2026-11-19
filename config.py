import os

REGEX_RULE = {
    "FilmTele-Play": ["播放", "电视剧"], # 句子是不是包含特定的单词，做出分类
    "HomeAppliance-Control": ["空调", "广播"]
}




CATEGORY_NAME = [
    'Travel-Query', 'Music-Play', 'FilmTele-Play', 'Video-Play',
    'Radio-Listen', 'HomeAppliance-Control', 'Weather-Query',
    'Alarm-Update', 'Calendar-Query', 'TVProgram-Play', 'Audio-Play',
    'Other'
]

'''
- TFIDF_MODEL_PKL_PATH：TF-IDF 模型文件路径。
- BERT_MODEL_PKL_PATH：BERT 微调权重路径。
- BERT_MODEL_PERTRAINED_PATH：预训练模型目录。
- LLM_OPENAI_SERVER_URL：远程模型服务地址。
- LLM_MODEL_NAME：实际调用的模型名称。
- LLM_OPENAI_API_KEY：认证密钥，从环境变量 DASHSCOPE_API_KEY 读取，不要写进代码。
大写变量名是“把它当常量使用”的约定，Python 不会禁止修改它。

'''
TFIDF_MODEL_PKL_PATH = "assets/weights/tfidf_ml.pkl"

BERT_MODEL_PKL_PATH = "assets/weights/bert.pt"
BERT_MODEL_PERTRAINED_PATH = "assets/models/bert-base-chinese/"

LLM_OPENAI_SERVER_URL = f"https://dashscope.aliyuncs.com/compatible-mode/v1" # ollama
LLM_OPENAI_API_KEY = os.getenv("DASHSCOPE_API_KEY", "")
LLM_MODEL_NAME = "qwen-plus"
