
for /f "delims=" %%i in ('dir /b /a-h "*.proto"') do (call .\protoc.exe -I=./ --python_out=../Message %%i)