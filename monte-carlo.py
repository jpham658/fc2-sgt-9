from scipy.stats import binom
from numpy import floor

P_SUCCESS = 2 / 3

def main():
    print("Number of runs N           P(X >= ceil(N / 2))")
    for N in range(3, 20, 2):
        half_of_N = floor(N / 2)
        p_gte_half_of_N = 1 - binom.cdf(half_of_N, N, P_SUCCESS)
        print(f"{N}                           {p_gte_half_of_N}")

if __name__ == "__main__":
    main()