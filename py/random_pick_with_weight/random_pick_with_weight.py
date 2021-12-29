'''
Author: fghpdf
Date: 2021-12-29 09:31:15
LastEditTime: 2021-12-29 10:03:18
LastEditors: fghpdf
'''
from typing import List
import random

class Solution:

    def __init__(self, w: List[int]):
        '''
        Create n uniform boxes of size 1/n each
        Fill them with (at most) 2 indices, and the weight associated with the first index
        O(n) time & space
        '''
        self.n = len(w)
        self.boxes = []

        ep = 10e-5
        summ = sum(w)
        weights = [elem / summ for elem in w]
        size = 1 / self.n
        bigWeights = {i: x for i, x in enumerate(weights) if x >= size}
        smallWeights = {i: x for i, x in enumerate(weights) if x < size}

        while bigWeights and smallWeights:
            # Pick a small and a big weight to make a full box
            i = next(iter(bigWeights))
            j, w_j = smallWeights.popitem()
            self.boxes.append([j, i, w_j])

            # The leftover from the big weight may now qualify as a small one
            bigWeights[i] -= (size - w_j)
            if bigWeights[i] < size - ep:  
                smallWeights[i] = bigWeights.pop(i)

        self.boxes.extend([key] for key in bigWeights)

    def pickIndex(self) -> int:
        boxNum = random.randint(0, self.n - 1)
        if len(self.boxes[boxNum]) == 1:
            return self.boxes[boxNum][0]
        
        return self.boxes[boxNum][random.uniform(0, 1 / self.n) >= self.boxes[boxNum][2]]