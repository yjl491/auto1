import os,time,unittest
from tools.HTMLTestRunner import HTMLTestRunner

class PathOpers():
    #遍历目录下的文件
    def walkDir(self,path): 
        lists = os.listdir(path)  #只遍历log_path下的第1层
        if('.project' in lists):
            return path
        else:
          path_parent = os.path.abspath(os.path.join(path,os.path.pardir))
          return self.walkDir(path_parent)
            
    #3.获取项目路径（含项目文件夹名称）
    def getProjectDir(self):
        curr_path = os.path.dirname(os.path.realpath(__file__))
        projectPath = self.walkDir(curr_path)
        print(projectPath)
        return projectPath.replace('\\', '/') 

if __name__=='__main__':
    #1.定义discover测试套件os.path.join(reportpath, “result.html”)
    #或者写作：start_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),'testcase')
    start_dir = os.path.dirname(os.path.realpath(__file__))+'/testcase'
    pattern='*.py'
    discover = unittest.defaultTestLoader.discover(start_dir, pattern)
    print(discover)  # 看有没找到用例
    
    #2.定义报告路径
    now_day=time.strftime('%Y-%m-%d')
    now_time=time.strftime('%Y%m%d_%H%M%S')
    #report_dir = PathOpers().getProjectDir()+'/src/report/'+now_day
    report_dir = PathOpers().getProjectDir()+'/src/report/'
    if(not os.path.exists(report_dir)):
        os.makedirs(report_dir)
    #f = open(report_dir+'/'+now_time+"result.html", 'wb')  #定义保存报告路径
    f = open(report_dir+'/'+"result.html", 'wb')  #定义保存报告路径
    
    #3.获取runner，并执行测试：erbosity表示打印案例的三点间的注释
    runner = HTMLTestRunner(stream=f,  title='全部案例的测试报告', description='用例执行情况：', verbosity=2) 
    runner.run(discover)
    f.close()