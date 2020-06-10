import sys

def main(s, f):
    
    print("\nGuilherme Cavalheiro e Marco Goedert\n\nProblema do Escalonamento de Intervalos\n")
    
    n = len(s)
    print(f"s: {s}\nf: {f}\n")
    
    output = gula(s, f, n)
    print(f"x: {output}")
    
def gula(s, f, n):
    
    f[0] = -sys.maxsize - 1
    x = []
    
    i = 0
    k = 1
    while k < n:
        if s[k] > f[i]:
            x.append(k)
            i = k
        k += 1    
    
    return x
    
if __name__ == "__main__":
    
    s = [4, 6, 13, 4, 2, 6, 7, 9, 1, 3, 9]
    f = [8, 7, 14, 5, 4, 9, 10, 11, 6, 13, 12]
    
    main(s, f)
    