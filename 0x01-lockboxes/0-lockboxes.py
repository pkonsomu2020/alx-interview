#!/usr/bin/python3
"""
Module that determines if all the boxes can be opened.
"""

def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n
    stack = [0]  # Initialize the stack with the first box (index 0)

    while stack:
        box_idx = stack.pop()
        if not visited[box_idx]:
            visited[box_idx] = True
            stack.extend(boxes[box_idx])

    return all(visited)
