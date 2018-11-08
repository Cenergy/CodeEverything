# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '8/11/2018 9:24 AM'

"""
广度优先搜索实现代码：
图由多个节点构成，每个节点都与邻近的节点相连，类似于"你"---->"bob",散列表能够表示其中的关系。


"""
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["peggy", "anuj"]
graph["claire"] = ["thom", "jonny"]
graph["alice"] = ["peggy"]

graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

from collections import deque


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_for_search(person):
                print(person + " is for search")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return  False


def person_is_for_search(name):
    return name[-1]=='m'


if __name__ == '__main__':
    search('you')
