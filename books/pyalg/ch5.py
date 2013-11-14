#! /usr/bin/env python
# -*- coding: utf-8
import collections


def bfs(graph, start, finish):
    in_progress = collections.deque()
    done = []
    parents = graph.keys()
    parents[start] = None
    in_progress.append(start)
    while in_progress:
        node = in_progress.popleft()
        if node == finish:
            break
        if node in done:
            continue
        for sibling in graph[node]:
            parents[sibling] = node
            in_progress.append(sibling)
        done.append(sibling)

    path = [finish]
    parent = finish
    while parents[parent] is not None:
        path.append(parents[parent])
        parent = parents[parent]

    return list(reversed(path))


def dfs(graph, start):
    done = []
    in_progress = []

    in_progress.append(start)
    while in_progress:
        node = in_progress.pop()
        if node in done:
            continue
        for sibling in graph[node]:
            in_progress.append(sibling)
        done.append(node)
    return done


def dfs_rec(graph, start, done=None):
    if not done:
        done = []
    done.append(start)
    for node in graph[start]:
        if node in done:
            continue
        dfs_rec(graph, node, done)
    return done


def top_sort(graph):
    def _dfs(graph, start):
        visited.append(start)
        for node in graph[start]:
            if node in visited:
                continue
            _dfs(graph, node)
        result.append(start)

    visited, result = [], []
    for node in graph:
        if node in visited:
            continue
        _dfs(graph, node)

    result.reverse()
    return result
