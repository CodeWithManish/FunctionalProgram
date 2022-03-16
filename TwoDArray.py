
def matrix():
    rows = int(input("Enter Number of Rows: "))
    cols = int(input("Enter number of columns: "))

    arr = [[0 for row in range(rows)] for column in range(cols)]

    for M in range(rows):
        for N in range(cols):
            arr[M][N] = M*N

        print(arr)

matrix()