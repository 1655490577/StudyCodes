import logging
from logging import handlers


# 1、创建一个logger
# 2、设置下logger的日志的等级
# 3、创建合适的Handler(FileHandler要有路径)
# 4、设置下每个Handler的日志等级
# 5、创建下日志的格式
# 6、向Handler中添加上面创建的格式
# 7、将上面创建的Handler添加到logger中
# 8、打印输出logger.debug\logger.info\logger.warning\logger.error\logger.critical

def log(msg):
    logger = logging.getLogger('test')  # 创建一个logger对象
    logger.setLevel(logging.DEBUG)  # 设置下logger的日志的等级
    # print(logger.handlers)    没添加handlers的情况下，logger.handlers返回的是一个空列表

    # 解决方案2：这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
    if not logger.handlers:
        # 创建合适的Handler(日志处理器)
        CDLogger = logging.handlers.RotatingFileHandler('test.log', maxBytes=2048, backupCount=6, encoding='utf-8')
        consLogger = logging.StreamHandler()  # 输出日志到控制台

        # 设置下每个Handler的日志等级
        CDLogger.setLevel(logging.WARNING)
        consLogger.setLevel(logging.ERROR)

        # 设置输出日志格式
        formatter = logging.Formatter(
            fmt='%(asctime)s %(name)s %(pathname)s %(processName)s %(threadName)s %(levelname)s %(message)s',
            datefmt='%Y-%m-%d  %H:%M:%S %a')

        # 为handler指定输出格式，注意大小写
        CDLogger.setFormatter(formatter)
        consLogger.setFormatter(formatter)

        # 为logger添加的日志处理器
        logger.addHandler(CDLogger)
        logger.addHandler(consLogger)

    logger.exception(msg)
    # #解决方案1，添加removeHandler语句，每次用完之后移除Handler
    # logger.removeHandler(CDLogger)
    # logger.removeHandler(consLogger)


# 输出不同级别的日志信息
# while True:
# logger.debug('debug')
# logger.warning('warning')
# logger.info('info')
# logger.error('error')
# logger.critical('critical')

log('test')
log('test2')
log('test3')
