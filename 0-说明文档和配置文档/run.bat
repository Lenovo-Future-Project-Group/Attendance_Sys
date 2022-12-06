@echo off  
set INTERVAL=300
timeout %INTERVAL%
:Again  
echo Called000000000000000
copy C:\Users\Administrator\PycharmProjects\pythonProject\交付版本v3-添加模版\0-说明文档和配置文档\备份\配置文档.txt C:\Users\Administrator\PycharmProjects\pythonProject\交付版本v3-添加模版\0-说明文档和配置文档\
copy C:\Users\Administrator\PycharmProjects\pythonProject\交付版本v3-添加模版\0-说明文档和配置文档\备份\说明文档.txt C:\Users\Administrator\PycharmProjects\pythonProject\交付版本v3-添加模版\0-说明文档和配置文档\ 
timeout %INTERVAL%
goto Again