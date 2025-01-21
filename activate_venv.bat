@echo off

REM ��� Python-VENV ���⻷���Ƿ����
if not exist "Python-VENV\Scripts\activate" (
    echo �޷��ҵ� Python-VENV ���⻷����
    pause
    exit /b
)

REM ���� Python-VENV ���⻷��
call Python-VENV\Scripts\activate
if %errorlevel% neq 0 (
    echo �������⻷��ʧ�ܡ�
    pause
    exit /b
) else (
    echo ���⻷�� Python-VENV �Ѽ��
)

REM ��Ⲣ����pip�汾
pip install --upgrade pip --dry-run >nul 2>&1
if %errorlevel% neq 0 (
    echo pip�Ѿ������°汾��
) else (
    echo ����pip�����°汾��
    pip install --upgrade pip
)

REM ��װpyinstaller�������δ��װ��
pip install pyinstaller

REM ���PyInstaller�Ƿ����
where pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo PyInstaller δ��װ�������У�pip install pyinstaller
    pause
    exit /b
)