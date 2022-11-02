# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import logging


def getDebugLogger():
    logger = logging.getLogger("debug")  # "debug"이름을 가진 로거 생성
    logger.setLevel(logging.DEBUG)  # debug 이상의 로그 전부 출력
    formatter = logging.Formatter(
        "[%(levelname)s] [%(asctime)s] %(message)s", "%Y-%m-%d %H:%M:%S")  # levelname, 시각, 메세지 출력 포맷

    # 개발시 처리 기록을 남겨야 하니까 debug
    debug = logging.FileHandler(filename="debug.log")  # 파일에 로그 저장
    debug.setFormatter(formatter)  # 포매터 연결
    logger.addHandler(debug)  # logger에 debug 로그 저장

    return logger


def getWarnLogger():
    logger = logging.getLogger("warn")  # 로거 생성

    formatter = logging.Formatter(
        "[%(levelname)s] [%(asctime)s] %(message)s", "%Y-%m-%d %H:%M:%S")  # levelname, 시각, 메세지 출력 포맷

    # 입력된 정보를 처리할 수 있으나 의도치 않은 정보가 들어왔을 경우니까 warning
    warn = logging.FileHandler(filename="warn.log")
    warn.setFormatter(formatter)
    logger.addHandler(warn)

    return logger
