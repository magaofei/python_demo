from queue import Queue
import random,threading,time

#生产者类
class Producer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.queue=queue

    def run(self):
        for i in range(5):
            print("%s is producing %d to the queue!" % (self.getName(), i))
            self.queue.put(i)
            time.sleep(random.randrange(10)/5)
        print("%s finished!" % self.getName())

#消费者类
class Consumer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self,name=name)
        self.queue=queue

    def run(self):
        """
        轮流从生产者中取值, 并消费
        """
        
        # while self.queue.get():
        #     val = self.queue.get()
        #     print("%s is consuming. %d in the queue is consumed!" % (self.getName(),val))
        #     time.sleep(random.randrange(10))
        # print("%s finished!" % self.getName())

        for i in range(5):
            val = self.queue.get()
            print("%s is consuming. %d in the queue is consumed!" % (self.getName(),val))
            time.sleep(random.randrange(10))
        print("%s finished!" % self.getName())

def main():

    """
    初始化
    """
    queue = Queue()
    producer = Producer('Producer',queue)
    consumer = Consumer('Consumer',queue)

    """
    启动
    """
    producer.start()
    consumer.start()

    """
    阻塞
    """
    producer.join()
    consumer.join()
    print('All threads finished!')

if __name__ == '__main__':
    main()