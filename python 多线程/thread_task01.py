from threading import Thread
from types import FunctionType
import threading
import copy

class Task(object):
    def __init__(self,jobs,func,threadnum=2):
        if not isinstance(jobs,list):
            raise ValueError('jobs must be a list')
        if not isinstance(func,FunctionType):
            raise ValueError('func must be a function')
        self.job = jobs
        self.func= func
        self.thread_num = threadnum
        self.unfinish_jobs = copy.deepcopy(self.job)
        self.cuurent_thrad = []
        self.error_thread = []
        self.sucess_thread = []
        self.lock = threading.Lock()


    def start(self):
        for t in self.set_thread():
            t.start()

    def set_thread(self):

        for i in range(self.thread_num):
            temp = Thread(target=self.run_thread)
            self.cuurent_thrad.append(temp)
        return self.cuurent_thrad


    def run_thread(self):
        while True:
            self.lock.acquire()
            if len(self.unfinish_jobs)==0:
                self.lock.release()
                break
            job = self.unfinish_jobs.pop()
            self.lock.release()

            try:
                self.func(job)
                self.sucess_thread.append(job)
            except:
                self.error_thread.append(job)


def func_job(job):
    print("job name id {}".format(job))

t=Task([1,2,3,4,5,6],func=func_job,threadnum=2)
t.start()






