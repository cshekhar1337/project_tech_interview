


class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
  def setNext(self, n):
        self.next = n






def question5(ll, m):
    head = ll;
    ptr1 = ll;
    ptr2 = ll;
    if head == None:
        return;
    while m > 0 and ptr2 != None:
        ptr2 = ptr2.next
        m = m -1
    if m > 0:
        return
    while ptr2 != None:
        ptr2 = ptr2.next
        ptr1 = ptr1.next
    return ptr1.data

def checkpalindrome(s):
    if s == Null:
        return True
    if len(s) == 1:
        return True
    l = len(s) -1 
    i = 0
    while i < (l+1)/2 :
        if s[i] != s[l - i]:
            return False
        i = i + 1

    return True






def question1(s , t):
    t_len = len(t)
    t_list = sorted(t)
    s_list = list(s[0: t_len])
    if t_list == sorted(s_list):
        return True
    del s_list[0]
    for i in range(1, len(s) - t_len):
        s_list.append(s[i])
        #print("\ns_list = ", str(s_list))
        #print("\nt_list = ", str(t_list))
        if t_list == sorted(s_list):
            return True
        del s_list[0]
    return False

print(question1("udacity", "ad"))

m1 = Node(1)
m2 = Node(2)
m3 = Node(3)
m4 = Node(4)
m5 = Node(5)
m6 = Node(6)
m1.setNext(m2)
m2.setNext(m3)
m3.setNext(m4)
m4.setNext(m5)
m5.setNext(m6)
print(question5(m1, 3))









