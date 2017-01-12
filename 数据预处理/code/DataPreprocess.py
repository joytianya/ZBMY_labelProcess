# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 17:24:06 2017

@author: Administrator
"""
file_task='C:/Users/Administrator/Desktop/标签体系/数据预处理/tasks_myy.xlsx'
file_labels='C:/Users/Administrator/Desktop/标签体系/数据预处理/labels.xlsx'
import pandas as pd
#from pandas import Series,DataFrame
FrameTask=pd.read_excel(file_task)
FrameLabels=pd.read_excel(file_labels)
FrameTask.index=FrameTask.index+2
def IsInHowLabels(x):
    for i in range(len(x)):
        if x[i] not in FrameLabels['场景'].values:
            return False
    return True
def IsInWhatLabels(x):
    for i in range(len(x)):
        if x[i] not in FrameLabels['行业'].values:
            return False
    return True    
FrameHowJudgment=FrameTask[FrameTask['场景'].notnull()]['场景'].str.split('；|;|，|、').apply(IsInHowLabels)
FrameWhatJudgment=FrameTask[FrameTask['行业'].notnull()]['行业'].str.split('；|;|，|、').apply(IsInWhatLabels)
ErrHow=FrameHowJudgment[FrameHowJudgment==False]
ErrWhat=FrameWhatJudgment[FrameWhatJudgment==False]
#ErrHow.index=ErrHow.index
#ErrWhat.index=ErrWhat.index
print ("场景:\n",FrameTask['场景'][ErrHow.index])
print ("行业:\n",FrameTask['行业'][ErrWhat.index])
print ("行业错误的个数：",len(ErrWhat))
print ("场景错误的个数：",len(ErrHow))

