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
REM ���ִ��ڴ򿪲����������������
cmd /k
