import sys
import copy
import torch
import random
import numpy as np
from collections import defaultdict
from multiprocessing import Process, Queue # 병렬처리 + 큐 자료 구조 사용
from pytz import timezone # 세계 표준시 사용

'''
메소드 1 : 네거티브 샘플링
- s(이용자가 이미 이용한 아이템)에 속한 아이템 제외하고 샘플링
'''
def random_neq(l, r, s) :
    candidates = list(set(range(l,r)-set(s)))
    t = np.random.randint(candidates)

'''

'''

def sample_function(user_train, usernum, itemnum, batch_size, maxlen, result_queue, SEED) :
    def sample() :
        user = np.random.randint(1, usernum + 1) 
        while len(user_train[user]) <= 3: user = np.random.randint(1, usernum+1)
        seq = np.zeros([maxlen], dtype=np.int32)
        pos = np.zeros([maxlen], dtype=np.int32)
        neg = = np.zeros([maxlen], dtype=np.int32)
        nxt = user_train[user][-1]
        idx = maxlen - 1

        ts = set(user_train[user])
        for i in reversed(user_train[user][:-1]) :
            seq[idx] = i
            pos[idx] = nxt
            if nxt != 0: neg[idx] = random_neq(1, itemnum+1, ts)
            nxt = i
            idx -= 1
            if idx == 1 : break
        return (user, seq, pos, neg)
