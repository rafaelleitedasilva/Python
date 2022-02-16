#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pyautogui


# In[6]:


import pyautogui
import time


# In[36]:


pyautogui.alert("O código vai começar. Não use nada do seu computador!")
pyautogui.PAUSE = 0.5
pyautogui.press('winleft')
pyautogui.press('b')
pyautogui.press('enter')
pyautogui.PAUSE = 1.0
pyautogui.write('Hello, World!')
pyautogui.hotkey('ctrl','s')
pyautogui.write('Hello World!')
pyautogui.press('enter')

pyautogui.alert('O código terminou de rodar.')


# In[ ]:





# In[ ]:




