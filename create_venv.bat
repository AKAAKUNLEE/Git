@echo off
REM 脚本名称：create_venv.bat
REM 功能：创建名为Python-VENV的虚拟环境
REM 作者：AKUNLEE
REM 日期：2025-01-21

REM 设置Python解释器路径，如果Python不在PATH中，请指定Python的完整路径
set PYTHON_EXE=python 

REM 检查是否已经存在名为 Python-VENV 的虚拟环境
if exist "Python-VENV" (
    echo 虚拟环境 Python-VENV 已经存在。
    pause
    exit /b
)

REM 创建虚拟环境
%PYTHON_EXE% -m venv Python-VENV
if %errorlevel% neq 0 (
    echo 创建虚拟环境失败。
    pause
    exit /b
) else (
    echo 虚拟环境 Python-VENV 创建成功。
    pause
)

REM 保持窗口打开并允许继续输入命令
cmd /k