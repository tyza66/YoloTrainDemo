@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

:: 提示用户输入自定义前缀
set /p prefix=请输入自定义前缀（如 0 或 1）:

:: 初始化计数器
set count=0

:: 遍历当前文件夹中的所有 jpg 文件
for %%f in (*.txt) do (
    :: 生成新的文件名
    set "newname=%prefix%(!count!).txt"
    :: 重命名文件
    ren "%%f" "!newname!"
    :: 计数器加 1
    set /a count+=1
)

echo 所有文件已成功重命名！
pause
