class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []

        while popped:
            if pushed:
                stack.append(pushed.pop(0))

            push_tail = stack[-1]
            pop_head = popped[0]

            while push_tail == pop_head and push_tail is not None:
                stack.pop()
                popped.pop(0)

                push_tail = stack[-1] if stack else None
                pop_head = popped[0] if popped else None

            if push_tail != pop_head and len(pushed) == 0:
                return False

        if len(popped) == 0:
            return True

        return False