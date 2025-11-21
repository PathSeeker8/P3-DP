"""
File: Project3.py
Author: Team 16

Description:
    This script is our answer to the dynamic programming problem “Teleportation in Astro Haunted Galaxies".

Pseudocode:
    See document due to length
        
Lines of code (w/ whitespace/comments):
    Total: 62 lines of code for algorithm, + 3 for execution

Time Complexity:
    Total: O(n^2 k)
"""

import random
import time

INF = float("inf")

def run_min_dp(teleport_matrix, haunted_state, haunted_limit):
    galaxy_count = len(teleport_matrix)
    
    # dp[i][h] = minimum cost to reach galaxy i using h haunted galaxies, starts at 0 to initialize
    dp = [[INF] * (haunted_limit + 1) for _ in range(galaxy_count)]
    dp[0][0] = 0

    # Loop that occurs over the possible number of haunted galaxies used
    for haunted_count in range(haunted_limit + 1):
        for current_galaxy in range(galaxy_count):
            if haunted_count >= haunted_state[current_galaxy]:      # Only considers this galaxy if we can afford it
                prev_haunted = haunted_count - haunted_state[current_galaxy]
                min_cost = dp[current_galaxy][haunted_count]
                for previous_galaxy in range(galaxy_count):     # Try all previous galaxies to find the minimum teleport cost
                    if previous_galaxy == current_galaxy:
                        continue
                    cost = dp[previous_galaxy][prev_haunted] + teleport_matrix[previous_galaxy][current_galaxy]
                    if cost < min_cost:
                        min_cost = cost
                dp[current_galaxy][haunted_count] = min_cost        # Updates our dp matrix with the current best min

    # Extract the min cost to reach the final galaxy using haunted_limit
    result = INF
    for haunted_count in range(haunted_limit + 1):
        if dp[-1][haunted_count] < result:
            result = dp[-1][haunted_count]
    return result

def make_galaxy_instance(galaxy_count, haunted_limit):      # Randomly assigns haunted status (except start and end), then generates a random cost
    haunted_state = [0] + [random.randint(0, 1) for _ in range(galaxy_count - 2)] + [0]
    teleport_matrix = [
        [0 if i == j else random.randint(1, 20) for j in range(galaxy_count)]
        for i in range(galaxy_count)
    ]
    return teleport_matrix, haunted_state

# Runs experiments with a constant haunted_limit (k), we didn't use it in the end but kept in for posterity
def test_n2(galaxy_sizes, k=3):
    print("~~~n^2 experiment (k constant)~~~")
    for galaxy_count in galaxy_sizes:
        teleport_matrix, haunted_state = make_galaxy_instance(galaxy_count, k)
        start = time.time()
        run_min_dp(teleport_matrix, haunted_state, k)
        elapsed_time = time.time() - start
        print(f"n={galaxy_count}, k={k}, time={elapsed_time:.5f}s")

# Runs experiments where haunted_limit grows with the galaxy size (k = n/2)
def test_n3(galaxy_sizes):
    print("\n~~~n^3 experiment (k ~ n)~~~")
    for galaxy_count in galaxy_sizes:
        k = galaxy_count // 2
        teleport_matrix, haunted_state = make_galaxy_instance(galaxy_count, k)
        start = time.time()
        run_min_dp(teleport_matrix, haunted_state, k)
        elapsed_time = time.time() - start
        print(f"n={galaxy_count}, k={k}, time={elapsed_time:.5f}s")

if __name__ == "__main__":
    # test_n2([40, 60, 80, 100, 120, 140, 160, 180, 200, 220])
    test_n3([40, 60, 80, 100, 120, 140, 160, 180, 200, 220])