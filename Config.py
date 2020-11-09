#coding: utf-8

import utils

# 版本号
SOFTWARE_VERSION = "V1.0"
SOFTWARE_NAME = "DOSS TTS语音文件合成"
SOFTWARE_AUTHOR = "熊汉良"

# 日志配置格式
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

# 路径配置
AUDIO_OUTPUT_DIR='./audio_output/'



# 音频配置
SPEED = 5
VOLUME = 5
PERSON = 4
TONE = 5
AUE = 6
# 结果判断

def initConfig():
    param = utils.parse_json('param.json')
    SPEED = param['语速']
    VOLUME = param['音量']
    TONE = param['音调']
    PERSON = param['发音人']
    AUE = param['格式']

if __name__ == '__main__':
    initConfig()
