# coding: utf-8


def func1():
    import os
    print('Process (%s) start...' % os.getpid())
    """for()调用一次，返回两次"""
    pid = os.fork()
    if pid == 0:
        print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    else:
        print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


def func2():
    from multiprocessing import Process
    import os

    def run_proc(name):
        print('Run child process %s (%s)...' % (name, os.getpid()))

    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test', ))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')


"""如果在func3中创建会调用失败"""
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end-start)))


def func3():
    from multiprocessing import Pool

    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


def func4():
    import subprocess
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)

    print('% nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('utf-8'))
    print('Exist code:', p.returncode)


def func5():
    from multiprocessing import Process, Queue
    import os, time, random

    def write(q):
        print('Process to write: %s' % os.getpid())
        for value in ['A', 'B', 'C']:
            print('Put %s to queue...' % value)
            q.put(value)
            time.sleep(random.random())

    def read(q):
        print('Process to read: %s' % os.getpid())
        while True:
            value = q.get(True)
            print('Get %s from queue.' % value)

    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()


if __name__ == '__main__':
    func3()