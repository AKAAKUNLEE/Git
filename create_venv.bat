@echo off
REM �ű����ƣ�create_venv.bat
REM ���ܣ�������ΪPython-VENV�����⻷��
REM ���ߣ�AKUNLEE
REM ���ڣ�2025-01-21

REM ����Python������·�������Python����PATH�У���ָ��Python������·��
set PYTHON_EXE=python 

REM ����Ƿ��Ѿ�������Ϊ Python-VENV �����⻷��
if exist "Python-VENV" (
    echo ���⻷�� Python-VENV �Ѿ����ڡ�
    pause
    exit /b
)

REM �������⻷��
%PYTHON_EXE% -m venv Python-VENV
if %errorlevel% neq 0 (
    echo �������⻷��ʧ�ܡ�
    pause
    exit /b
) else (
    echo ���⻷�� Python-VENV �����ɹ���
    pause
)

REM ���ִ��ڴ򿪲����������������
cmd /k