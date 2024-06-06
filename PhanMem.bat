@echo off
REM Kiểm tra xem Python đã được cài đặt trên máy tính chưa
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Python không được cài đặt trên máy tính của bạn.
    pause
    exit /b
)

REM Khởi chạy file Python "main.py"
python main.py

REM Dừng lại để người dùng có thể đọc thông báo trước khi thoát
pause