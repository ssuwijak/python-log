import logging
from log_common import logger
from  arith import *


logger = logging.getLogger(__name__)

def main():
    logger.info("Program started")
    a = 2
    b = 5
    
    Add(a,b)
    Sub(a,b)
    Mul(a,b)
    Div(a,b)

    logger.info("Program ended")

if __name__ == "__main__":
    main()
