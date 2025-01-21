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

REM 检测并更新pip版本
pip install --upgrade pip --dry-run >nul 2>&1
if %errorlevel% neq 0 (
    echo pip已经是最新版本。
) else (
    echo 更新pip到最新版本。
    pip install --upgrade pip
)

REM 安装pyinstaller（如果尚未安装）
pip install pyinstaller

REM 检查PyInstaller是否存在
where pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo PyInstaller 未安装。请运行：pip install pyinstaller
    pause
    exit /b
)