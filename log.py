import logging


def get_logger():
    logger = logging.getLogger()  # 로거 생성
    logger.setLevel(logging.DEBUG)  # debug 이상의 전부 출력
    formatter = logging.Formatter(
        "[%(levelname)s] [%(asctime)s] %(message)s", "%Y-%m-%d %H:%M:%S")  # levelname, 시각, 메세지 출력 포맷

    info = logging.FileHandler(filename="info.log")  # 정상 로그 저장할 파일핸들러
    info.setFormatter(formatter)  # 포매터 연결
    logger.addHandler(info)  # logger에 info 로그 저장

    return logger
