
def check(input, size, startIndex, sum1, sum2):
    if startIndex == size:
        return sum1 == sum2
    
    if input[startIndex] % 5 == 0:
        sum1 += input[startIndex]
    elif input[startIndex] % 3 ==0:
        sum2 += input[startIndex]
    else:
        # Recursive calls to explore both choices:
        # 1. Include input[startIndex] in sum1
        left_ans = check(input, size, startIndex + 1, sum1 + input[startIndex], sum2)
        # 2. Include input[startIndex] in sum2
        right_ans = check(input, size, startIndex + 1, sum1, sum2 + input[startIndex])
        # Return True if either left_ans or right_ans is True
        return left_ans or right_ans
    
    # Continue checking with the next element in the array
    return check(input, size, startIndex + 1, sum1, sum2)
    
def split_array(input, size):
    return check(input, size, 0, 0, 0)



    

def main():
    size = int(input())
    input_array = list(map(int, input().split()))

    if split_array(input_array, size):
        print("true")
    else:
        print("false")

if __name__ == "__main__":
    main()
