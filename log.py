import logging


def get_logger():
    logger = logging.getLogger()  # �ΰ� ����
    logger.setLevel(logging.DEBUG)  # debug �̻��� ���� ���
    formatter = logging.Formatter(
        "[%(levelname)s] [%(asctime)s] %(message)s", "%Y-%m-%d %H:%M:%S")  # levelname, �ð�, �޼��� ��� ����

    info = logging.FileHandler(filename="info.log")  # ���� �α� ������ �����ڵ鷯
    info.setFormatter(formatter)  # ������ ����
    logger.addHandler(info)  # logger�� info �α� ����

    return logger
