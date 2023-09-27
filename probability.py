
def permutation(n, constant, k):
    if (n == constant-k+1):
        return n
    else:
        return n*permutation(n-1, constant, k)
    
def factorial(n):
    if (n==1):
        return n
    else:
        return n*factorial(n-1)

def combination(n, k):
    return int(permutation(n, n, k)/factorial(k))

if __name__ == "__main__":
    n = int(input("How many possible objects? (n=?) "))
    k = int(input("Choose how many? (k=?) "))

    valid = False
    while valid == False:
        order = input("Does order matter? (y/n) ")

        match order:
            case "y":
                print(f"Number of ways to choose {k} from {n} objects (order matters): {permutation(n, n, k)}")
                valid = True
            case "n":
                print(f"Number of ways to choose {k} from {n} objects (order doesn't matter): {combination(n, k)}")
                valid = True
            case _:
                print("Please enter either \"y\" or \"n\"")
                valid = False
    
    