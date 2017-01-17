#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from pandas import DataFrame
import os
rootDir='../taskFiles'
list_dirs=os.walk(rootDir)
flag=0
#for root,dirs,files in list_dirs:
#	for f in files:
for lists in os.listdir(rootDir):
	file_task=os.path.join(rootDir,lists)
	presonName=lists[6:-5]
	
	FrameTask=pd.read_excel(file_task)
#	print FrameTask
	if flag==0:
		FrameMerge=FrameTask[['appid','title','url','desc']].copy()
		FrameMerge['场景_%s'%presonName]=FrameTask['场景'].copy()
		FrameMerge['行业_%s'%presonName]=FrameTask['行业'].copy()
		flag=1
	else:
		FrameMerge['场景_%s'%presonName]=FrameTask['场景'].copy()
		FrameMerge['行业_%s'%presonName]=FrameTask['行业'].copy()
	FrameMerge.to_csv('../ProcessResult/dataMerge.csv', index=False,mode='w')
