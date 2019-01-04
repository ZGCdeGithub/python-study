import threading
import time
import myQueue
import queue


# 参数4代表最多只能四个线程同时使用资源
semphore = threading.Semaphore(4)


def fun(que):
    if semphore.acquire():
        # 将输出信息放到queue中，防止输出混乱
        prt = threading.currentThread().getName(), ' get semphore'
        que.put(prt)
        time.sleep(5)
        semphore.release()
        prt = threading.currentThread().getName(), ' release semphore'
        que.put(prt)


if __name__ == '__main__':
    # 启动一个线程来运行queue,将输出信息一个个读出，然后输出
    que = queue.Queue()
    q = myQueue.MsgQueue(que)
    q.start()
    for i in range(8):
        t = threading.Thread(target=fun, args=(que,))
        t.start()
        # t.join()
        # time.sleep(1)


