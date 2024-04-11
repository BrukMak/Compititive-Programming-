class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        que = [i for i in range(len(deck))]
        deck.sort()
        que = deque(que)
        flag = True
        ans = [0] * len(deck)
        i = 0
        while que:
            top = que.popleft()
            if flag:
                ans[top] = deck[i]
                i += 1
            else:
                que.append(top)
            flag = not flag
        return ans