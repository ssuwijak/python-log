import logging

logger = logging.getLogger(__name__)


def Add(a, b):
    logger.debug(f"calling Add({a},{b})")
    ret = a+b
    logger.info(f"answer = {ret}")
    return ret


def Sub(a, b):
    logger.debug(f"calling Sub({a},{b})")
    ret = a-b

    if ret < 0:
        logger.error(f"answer = {ret}")
    elif ret == 0:
        logger.warning(f"answer = {ret}")
    else:
        logger.info(f"answer = {ret}")

    return ret


def Mul(a, b):
    logger.debug(f"calling Mul({a},{b})")
    ret = 0
    try:
        ret = a*b
        logger.info(f"answer = {ret}")
    except Exception as ex:
        logger.exception(f"{ex}")

    return ret


def Div(a, b):
    logger.debug(f"calling Div({a},{b})")
    ret = 0
    try:
        ret = a/b
        logger.info(f"answer = {ret}")
    except Exception as ex:
        logger.exception(f"{ex}")

    return ret
