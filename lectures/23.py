# parenthesis check
import queue

stack = queue.LifoQueue()

def parenthesis(sen):
    for idx, ch in enumerate(sen):

        if ch == "(":
            stack.put(idx)

        elif ch == ")":
            if stack:
                print("Output:", stack.get(), idx)

            else:
                print("Error")

        else:
            pass

if __name__ == "__main__":
    parenthesis("(a*(b+c)+d)")


# tower of Hanoi
def TOH(n, x, y, z):
    if n > 0:
        TOH(n-1, x, z, y)
        print("Move top disk from ", x, " to ", y)
        TOH(n-1, z, y, x)

if __name__ == "__main__":
    n = 3
    TOH(n, "tower x", "tower y", "tower z")
