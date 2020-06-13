import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(pathname)s %(processName)s %(threadName)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d  %H:%M:%S %a')


# for i in range(6):
#     if i == 1:
#         logging.debug('this is debug log')
#     elif i == 2:
#         logging.info('this is info log')
#     elif i == 3:
#         logging.warning('this is warning log')
#     elif i == 4:
#         logging.error('this is error log')
#     elif i == 5:
#         logging.critical('this is critical log')

def test_input(titler):
    while True:
        text = input(f'请输入您的{titler}：\n')
        if titler == '年龄':
            try:
                text = int(text)
                if text == 0 or text == '':
                    test_hint(titler)
                    continue
                else:
                    return text
            except Exception as f:
                test_hint(titler)
                # logging.exception(f)
                continue
        elif text.strip() == '':
            test_hint(titler)
        else:
            return text


def test_hint(titlers):
    print('*' * 20)
    print(f"{titlers}输入无效，请重新输入")
    print('*' * 20)


def test():
    a = test_input('姓名')
    b = test_input('年龄')
    c = test_input('学校')
    print(f'姓名：{a}\n年龄：{int(b)}\n学校：{c}\n**************\n欢迎来到德莱联盟\n**************')


if __name__ == '__main__':
    try:
        test()
    except Exception as e:
        logging.exception(e)
