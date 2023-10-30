@echo off

call :CMD_C %CMDCMDLINE%
if /I "%CMD_C%" == "/C" (
    cmd /k python builder.py gradlew-proxy
) else python builder.py gradlew-proxy
exit

:CMD_C
set CMD_C=%2
