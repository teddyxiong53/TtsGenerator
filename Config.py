#coding: utf-8

import utils
import os, json

# 版本号
SOFTWARE_VERSION = "V1.0"
SOFTWARE_NAME = "DOSS TTS语音文件合成"
SOFTWARE_AUTHOR = "熊汉良"

# 日志配置格式
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

# 路径配置
AUDIO_OUTPUT_DIR='./audio_output/'



# 音频配置
globalParam = {
    'speed': 5,
    'volume': 5,
    'tone': 5,
    'person': 0,
    'format': 1
}

# 结果判断

def readConfig():
    global globalParam
    if os.path.exists('param.json'):
        with open('param.json', encoding='utf-8') as f:
            globalParam = json.load(f)

def writeConfig():
    global globalParam
    with open('param.json', 'w', encoding='utf-8') as f:
        json.dump(globalParam, f)

if __name__ == '__main__':
    readConfig()
    globalParam['speed'] = 6
    writeConfig()
