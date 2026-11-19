import logging # 日志打印模块

logging.basicConfig(
    level=logging.INFO,# level=logging.INFO：记录 INFO 及以上级别的日志
    # format：日志包含时间、记录器名称、级别和消息。
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),  # 输出到文件
        logging.StreamHandler(),         # 同时输出到控制台
    ]
)

logger = logging.getLogger(__name__)