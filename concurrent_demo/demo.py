import _thread
import threading
import multiprocessing

import concurrent.futures

import requests
import profile
import cProfile
import time

MAX_WORKER = 10

def test(value=None):
    """
    测试函数
    """
    URL = 'http://httpbin.org/get'
    r = requests.get(URL)
    
    

class OriginDemo():
    def __init__(self):
        for _ in range(100):
            test()
class ThreadDemo():
    """
    Python3 名称为 _thread
    几乎没有用过
    功能：
    - 开线程 start_new_thread
    - 加锁 acquire  release   locked
    - 中断和退出 interrupt_main  exit

    """
    def __init__(self):
        for i in range(100):
            _thread.start_new_thread(test, ("foo",))
    


class ThreadingDemo(object):
    """
    Threading 测试
    基于 _thread 
    - 获取激活数量
    - 获取运行线程数量
    - 开线程，运行，阻塞，等待，设置名字，获取名，后台执行
    - 信号量
    """

    def __init__(self):
        threads = []
        for _ in range(100):
            t = threading.Thread(target=test)
            threads.append(t)
            t.start()
        
        for t in threads:
            # 线程激活数
            # print(threading.active_count())
            t.join()

class ConcurrentThreadingDemo(object):
    """
    基于 Threading 
    API 最简单，易于理解，容易使用
    - 线程池功能
    - 批量执行
    - 自定义最大线程数

    """

    def __init__(self):
        with concurrent.futures.ThreadPoolExecutor(MAX_WORKER) as exector:
            values = (i for i in range(100))
            results = exector.map(test, values)
            
            concurrent.futures.as_completed(results)



if __name__ == '__main__':
    
    profile.run('ThreadDemo()')

    time0 = time.time()
    profile.run('OriginDemo()')
    print("OriginDemo\t" + str(time.time() - time0))

    time.sleep(5)
    
    time0 = time.time()
    profile.run('ThreadingDemo()')
    print("ThreadingDemo\t" + str(time.time() - time0))

    time.sleep(5)

    time0 = time.time()
    profile.run('ConcurrentThreadingDemo()')
    print("ConcurrentThreadingDemo\t" + str(time.time() - time0))

    
    # cProfile.run('thread_demo()')
    

