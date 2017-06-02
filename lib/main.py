# coding=utf-8
from Queue import Queue
import options
import getTask
import scan
import sys
import os

# 获取参数
args = options.oparser()

# 获取任务
try:
    qtask = getTask.getTask(args.urls,args.pocfile)
    # qsize = qtask.qsize()
    # while not qtask.empty():
    #     print qtask.get() 
except TypeError as e:
    print e
    sys.exit(0)
except Exception as e:
    print e
    sys.exit(0)

# 启动扫描
qresults = Queue()
scan.main(qtask,qresults,args.thread)


# 保存结果
if args.out:
    if '/' in args.out  or '\\' in args.out:
        path = os.path.dirname(args.out)
        if not os.path.exists(path):
            os.makedirs(path)
    with open(args.out,'w') as f:
        while not qresults.empty():
            result = qresults.get()
            f.write(result['info'])
            f.write('\n')



