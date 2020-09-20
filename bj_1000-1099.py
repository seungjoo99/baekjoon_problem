#!/usr/bin/env python
# coding: utf-8

# ### 1000

# In[1]:


a,b=[int(x) for x in input().split()]

print(a+b)


# ### 1001

# In[2]:


a,b=[int(x) for x in input().split()]

print(a-b)


# ### 1002 - 터렛
# ###### 조규현 좌표 (x1, y1), 백승환 좌표 (x2, y2), 상대편과 조규현 거리 r1, 상대편과 백승환 거리 r2
# ###### 상대편이 있을 수 있는 좌표의 수 출력 ----> 원과 원 사이의 교점의 개수 생각!

# In[ ]:


n=int(input())
for i in range(n):
    x1,y1,r1,x2,y2,r2=map(int, input().split())
    
    d=((x2-x1)**2+(y2-y1)**2)**(0.5)  
    #중심이 (x1,y1) 반지름이 r1인 원과 중심이 (x2,y2) 반지름이 r2인 원사이의 거리
    #d= 중심사이의 거리
    
    rs=r1+r2
    rm=abs(r1-r2)
    
    if d==0:  # 중심사이의 거리가 같다면 두 원이 아예 같거나 작은 원이 큰 원의 한 가운데 존재
        if r1 == r2: #두 원이 아예 같다 == 좌표의 수가 무한 개
            print(-1)
        else: # 두 원이 같지는 않지만 만나는 점이 없음
            print(0)
    else:
        if d==rs or d==rm: #두 원이 외접 or 내점할 땐 만나는 점이 1개
            print(1)
        elif d<rs and d>rm: #두 원의 반지름 더한 것보다 d가 작거나, 두 원의 반지름 뺀 것 보다 d가 크다면 교점 2개
            print(2)
        else: #나머지는 만나지 않을 경우
            print(0)


# ### 1008

# In[1]:


a,b=map(int, input().split())
print(a/b)


# ### 1065 한수
# ###### 정수의 각 자리가 등차수열을 이루는 수를 한수 ---> 한수의 개수 출력

# In[2]:


n=int(input())
a=0
for i in range(1,n+1):
    if i<=99:
        a+=1
    else:
        nums=list(map(int, str(i)))
        if nums[0]-nums[1]==nums[1]-nums[2]:
            a+=1
print(a)


# In[ ]:




