import logging
logging.basicConfig(level=logging.INFO)
try:
    print('start')
    a=int("0")
    #assert a != 0,"a is zero"
    logging.info('a is %d' % a)
    10/a
except ZeroDivisionError as e:
        print(e)
except ValueError as e:
        print(e)
finally:
        print('end')