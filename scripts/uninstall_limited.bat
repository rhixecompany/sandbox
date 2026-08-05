@echo off
setlocal
REM Non-elevated uninstall of user-scope packages (runs via limited-token scheduled task).
set LOG=%USERPROFILE%\Desktop\SandBox\results\app-uninstall-limited.log
echo [%date% %time%] START > "%LOG%"
for %%A in (
  "Google.DartSDK,DartSDK"
  "Julialang.Julia,Julia"
  "GitHub.Copilot,CopilotCLI"
  "BtbN.FFmpeg.LGPL.7.1,FFmpegLGPL"
  "NirSoft.BatteryInfoView,BatteryInfoView"
) do (
  for /f "tokens=1,2 delims=," %%a in (%%A) do (
    echo === uninstall %%a (%%b) === >> "%LOG%"
    winget uninstall --id %%a --silent --disable-interactivity >> "%LOG%" 2>&1
    echo rc=%errorlevel% %%a >> "%LOG%"
  )
)
echo [%date% %time%] DONE >> "%LOG%"
exit /b 0