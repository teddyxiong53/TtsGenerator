@echo off
chcp 65001
echo "------清空dist目录"
rd /S /Q dist
echo "-----------生成exe文件"
pyinstaller.exe -F -w TtsGenerator.py
echo "----------拷贝文件"

copy param.json dist
copy 使用说明.txt dist


