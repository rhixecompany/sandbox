@echo off
REM post-exec-state-log Hook Wrapper
REM Invokes state logging with the given event type and JSON payload
python "%USERPROFILE%\AppData\Local\hermes\hooks\post-exec-state-log.py" %*
