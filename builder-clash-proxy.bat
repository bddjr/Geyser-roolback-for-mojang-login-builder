@echo off

call :CMD_C %CMDCMDLINE%
if /I "%CMD_C%" == "/C" (
    cmd /k python builder.py clash-proxy
) else python builder.py clash-proxy
exit

:CMD_C
set CMD_C=%2
