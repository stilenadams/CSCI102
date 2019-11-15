# fibonacci.py

def fib():
    fibs = [1, 2]
    n1=1
    n2=2
    for i in range(1,9):
        
        Next=n2+n1
        
        fibs.append(Next)
        n1=n2
        n2=Next
        

    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
