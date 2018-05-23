"""
生产者消费者
"""


"""
图解：

生产者生产，消费者消费。
消费者每消费一次，都要去执行以下task_done()方法，来告诉消费者已经消费成功，相当于吃完饭，消费者应该给钱了。
消费者每消费一次，则队列中计数器会做减1操作。
当队列中的计数器为0的时候，则生产者不阻塞，继续执行，不为0的时候，则阻塞，直到消费者消费完毕为止。
"""

import time,random
import queue,threading
q = queue.Queue()
 

def producer(name):
    """ 生产者 """
    count = 0
 
    while count < 20:
        time.sleep(random.randrange(3))
        q.put(count)  # 在队列里放包子
        print('Producer %s has produced %s baozi..' % (name, count))
        count += 1
 
 
def consumer(name):
    """ 消费者 """
    count = 0
    while count < 20:
        time.sleep(random.randrange(4))
    if not q.empty():  # 如果还有包子
        data = q.get()  # 就继续获取保证
        print(data)
        print('\033[32;1mConsumer %s has eat %s baozi...\033[0m' % (name, data))
    else:
        print("-----no baozi anymore----")
    count += 1
 
if __name__ == '__main__':
    p1 = threading.Thread(target=producer, args=('A',))
    c1 = threading.Thread(target=consumer, args=('B',))
    p1.start()
    c1.start()