@echo off

REM ���ִ��ڴ򿪲����������������
cmd /k

REM ����Python������·�������Python����PATH�У���ָ��Python������·��
set PYTHON_EXE=python
 
REM ����Ƿ��Ѿ�������Ϊ666�����⻷��
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

