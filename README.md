# 代码流程

- 环境配置：fastapi （web server）、模型环境（transformers、 torch、 sklearn）
- 模型训练：tfidf、bert（下载权重）
- 模型推理服务 集成 在fastapi中

```commandline
python3 training_code/train_tfidf.py
python3 training_code/train_bert.py
fastapi run main.py
```

# 配置大模型 API Key

`/v1/text-cls/gpt` 接口调用阿里云百炼（DashScope）的 `qwen-plus` 模型。API Key 不写在代码里，`config.py` 会从环境变量 `DASHSCOPE_API_KEY` 读取。

1. 在 [阿里云百炼控制台](https://bailian.console.aliyun.com/) 创建 API Key。
2. 启动服务前，在同一个终端里设置环境变量：

macOS / Linux：

```commandline
export DASHSCOPE_API_KEY="你的API Key"
fastapi run main.py
```

Windows PowerShell：

```commandline
$env:DASHSCOPE_API_KEY="你的API Key"
fastapi run main.py
```

Windows CMD：

```commandline
set DASHSCOPE_API_KEY=你的API Key
fastapi run main.py
```

以上写法只对当前终端有效。想长期生效，可以把 `export` 那一行写进 `~/.bashrc` / `~/.zshrc`，Windows 上用 `setx DASHSCOPE_API_KEY "你的API Key"`（设置后需要新开一个终端）。

没有设置这个变量时，正则、TF-IDF、BERT 三个接口照常可用，只有 `/v1/text-cls/gpt` 会在 `error_msg` 里返回认证失败。

# 压测服务

```commandline
cd test/

ab -n 100 -c 100 -p data.json -T 'application/json' -H 'accept: application/json' 'http://0.0.0.0:8000/v1/text-cls/regex'
ab -n 100 -c 100 -p data.json -T 'application/json' -H 'accept: application/json' 'http://0.0.0.0:8000/v1/text-cls/tfidf'
ab -n 100 -c 100 -p data.json -T 'application/json' -H 'accept: application/json' 'http://0.0.0.0:8000/v1/text-cls/bert'
```

# 接口

```commandline
curl -X 'POST' \
  'http://0.0.0.0:8000/v1/text-cls/tfidf' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "request_id": "string",
  "request_text": "帮我播放周杰伦的歌曲"
}'
```

# 部署

```commandline
fastapi run main.py
```
