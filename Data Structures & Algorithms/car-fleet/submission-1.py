class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
            s = [(p,s) for p,s in zip(position, speed)]
            s.sort(reverse=True)
            stack = []
            maxT = 0
            for i in s:
                time = (target - i[0])/i[1]
                if stack and time > stack[-1]:
                    stack.append(time)
                elif not stack:
                    stack.append(time)
                else:
                    continue
            return len(stack)