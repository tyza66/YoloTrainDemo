@echo off
setlocal enabledelayedexpansion

:: 初始化计数器
set count=0

:: 遍历当前文件夹中的所有 jpg 文件
for %%f in (*.jpg) do (
    :: 生成新的文件名
    set "newname=0(!count!).jpg"
    :: 重命名文件
    ren "%%f" "!newname!"
    :: 计数器加 1
    set /a count+=1
)

echo 所有文件重命名完成！
pause
