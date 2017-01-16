#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 11:46:59 2017

@author: xuanwei
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 15:39:34 2017

@author: Administrator
"""
import pandas as pd
import numpy as np
from pandas import DataFrame
import os
rootDir='../taskFiles'
list_dirs=os.walk(rootDir)
flag=0
for root,dirs,files in list_dirs:
    for f0 in files:
        file_task_0=os.path.join(rootDir,f0)
#        print (f0)
        for f1 in files[files.index(f0)+1:]:
            file_task_1=os.path.join(rootDir,f1)
        
#            file_task_0='C:/Users/Administrator/Desktop/标签体系/数据预处理/tasks_zxw.xlsx'
#            file_task_1='C:/Users/Administrator/Desktop/标签体系/数据预处理/tasks_tml.xlsx'
            
            person_0=f0[6:-5]
            person_1=f1[6:-5]
            
            FrameTask_0=pd.read_excel(file_task_0)
            FrameTask_1=pd.read_excel(file_task_1)
            FrameTaskNotNullHow_0=FrameTask_0[FrameTask_0['场景'].notnull()]
            FrameTaskNotNullHow_1=FrameTask_1[FrameTask_1['场景'].notnull()]
            IntersectHowIndex=np.intersect1d(FrameTaskNotNullHow_0.index,FrameTaskNotNullHow_1.index)
#            DiffDataHowIndex=FrameTaskNotNullHow_0['场景'].loc[IntersectHowIndex]!=FrameTaskNotNullHow_1['场景'].loc[IntersectHowIndex]
            
            FrameTaskNotNullWhat_0=FrameTask_0[FrameTask_0['行业'].notnull()]
            FrameTaskNotNullWhat_1=FrameTask_1[FrameTask_1['行业'].notnull()]
            IntersectWhatIndex=np.intersect1d(FrameTaskNotNullWhat_0.index,FrameTaskNotNullWhat_1.index)
#            DiffDataWhatIndex=FrameTaskNotNullWhat_0['行业'].loc[IntersectWhatIndex]!=FrameTaskNotNullWhat_1['行业'].loc[IntersectWhatIndex]
            
#            DiffDataIndex=np.union1d(DiffDataWhatIndex[DiffDataWhatIndex==True].index,DiffDataHowIndex[DiffDataHowIndex==True].index)
            WholeIndex=np.union1d(IntersectHowIndex,IntersectWhatIndex)
            FrameMessage=FrameTask_0[['appid','title','url','desc']].loc[ WholeIndex].copy()
            Frame=DataFrame([FrameTaskNotNullHow_0['场景'].loc[WholeIndex], FrameTaskNotNullHow_1['场景'].loc[WholeIndex],FrameTaskNotNullHow_0['行业'].loc[WholeIndex],FrameTaskNotNullHow_1['行业'].loc[WholeIndex]],index=['0_场景','1_场景','0_行业','1_行业'])
            Frame=Frame.append(FrameMessage.T)
            
            #Frame['appid','title','url','desc']=FrameMessage
            Frame=Frame.T
            Frame['序号']=WholeIndex+2
            Frame['标注人_0']=person_0
            Frame['标注人_1']=person_1
            Frame=Frame.reindex(columns=['标注人_0','标注人_1','appid','序号','url','title','desc','0_场景','1_场景','0_行业','1_行业'])
#            print (Frame)
            #np.savetxt('C:/Users/Administrator/Desktop/标签体系/数据预处理/dataComparison.csv',Frame,fmt='%s',delimiter=',')
#            print ("不同个数:",len(Frame))
            if flag==0:
                Frame.to_csv('../ProcessResult/dataComparisonMerge.csv', index=False,mode='w')
                flag=1
            else:
                Frame.to_csv('../ProcessResult/dataComparisonMerge.csv', index=False,mode='a',header=False)
            #print ("different data:",FrameTaskNotNullHow_0['场景'].loc[DiffDataIndex],FrameTaskNotNullHow_1['场景'].loc[DiffDataIndex])
