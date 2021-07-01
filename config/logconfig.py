import logging.handlers
'''
日志配置类
引入flask应用后将会开启日志系统，在程序根目录下生成app.log日志文件(utf-8编码)
日志默认记录等级为INFO，每条日志的格式为：日志生成时间 - 日志等级 - 执行该日志的当前程序名 - 日志当前行号 - 日志内容
日志使用全局配置，程序内所有 app.logger.INFO/WARNING/ERROR('log content') 均为编写日志操作
'''

handler = logging.FileHandler('app.log', encoding='utf-8')
handler.setLevel(logging.INFO)
logging_format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(lineno)s - %(message)s')
handler.setFormatter(logging_format)
logging.getLogger().addHandler(handler)
