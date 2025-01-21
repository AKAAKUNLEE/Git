@echo off

REM 检查 Python-VENV 虚拟环境是否存在
if not exist "Python-VENV\Scripts\activate" (
    echo 无法找到 Python-VENV 虚拟环境。
    pause
    exit /b
)

REM 激活 Python-VENV 虚拟环境
call Python-VENV\Scripts\activate
if %errorlevel% neq 0 (
    echo 激活虚拟环境失败。
    pause
    exit /b
) else (
    echo 虚拟环境 Python-VENV 已激活。
)
REM 保持窗口打开并允许继续输入命令
cmd /k
