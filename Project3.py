import random
import time

INF = float("inf")

def run_dp(C, a, k):
    n = len(C)
    T = [[INF] * (k + 1) for _ in range(n)]
    T[0][0] = 0

    for m in range(k + 1):
        for i in range(n):
            if m >= a[i]:
                pm = m - a[i]
                best = T[i][m]
                for j in range(n):
                    if j == i:
                        continue
                    v = T[j][pm] + C[j][i]
                    if v < best:
                        best = v
                T[i][m] = best

    ans = INF
    for m in range(k + 1):
        if T[-1][m] < ans:
            ans = T[-1][m]
    return ans

def make_instance(n, k):
    a = [0] + [random.randint(0,1) for _ in range(n-2)] + [0]
    C = [
        [0 if i == j else random.randint(1,20) for j in range(n)]
        for i in range(n)
    ]
    return C, a

def test_n2(ns, k=3):
    print("n^2 experiment (k constant)")
    for n in ns:
        C, a = make_instance(n, k)
        start = time.time()
        run_dp(C, a, k)
        t = time.time() - start
        print(f"n={n}, k={k}, time={t:.5f}s")

def test_n3(ns):
    print("\nn^3 experiment (k ~ n)")
    for n in ns:
        k = n//2
        C, a = make_instance(n, k)
        start = time.time()
        run_dp(C, a, k)
        t = time.time() - start
        print(f"n={n}, k={k}, time={t:.5f}s")

if __name__ == "__main__":
    # test_n2([40, 60, 80, 100, 120, 140, 160, 180, 200, 220])
    test_n3([40, 60, 80, 100, 120, 140, 160, 180, 200, 220])