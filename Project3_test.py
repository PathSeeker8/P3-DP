"""
File: Project3_test.py
Author: Team 16

Description (Unit tests for Project3.py):
    These test cases check to make sure that our dynamic programming algo works correctly:
        - "test_run_min_dp_finds_best_path_with_limited_haunted":
            - Builds a tiny 3-galaxy graph where the optimal route goes through one haunted node. The test checks that "run_min_dp" returns the expected minimum cost (8) when the haunted limit is high enough (1), proving the DP implementation finds the best path under those constraints.
        
        - "test_run_min_dp_returns_inf_when_limit_too_low":
            - Uses a similar 3-galaxy graph but sets the haunted limit to 0 while the only viable path requires entering a haunted node. The function should report no feasible solution, so the test asserts the result is "inf".
        
        - "test_optimal_path_uses_max_haunted":
            - Builds a 4-galaxy graph with a cheap path through 2 haunted nodes and an expensive direct path. Checks that "run_min_dp" picks the cheaper route when given enough haunted.

Directions: Ensure that the main script is in the same dir. so the import below works. That is all.
"""

import math
import unittest
import Project3 as project

class TestMinDP(unittest.TestCase):
    def test_run_min_dp_finds_best_path_with_limited_haunted(self):
        teleport_matrix = [
            [0, 5, 12],
            [5, 0, 3],
            [12, 3, 0],
        ]
        haunted_state = [0, 1, 0]
        result = project.run_min_dp(teleport_matrix, haunted_state, haunted_limit=1)
        self.assertEqual(result, 8)  # 0->1->2 path with cost 8

    def test_run_min_dp_returns_inf_when_limit_too_low(self):
        big = project.INF
        teleport_matrix = [
            [0, 4, big],
            [4, 0, 2],
            [big, 2, 0],
        ]
        haunted_state = [0, 1, 0]
        result = project.run_min_dp(teleport_matrix, haunted_state, haunted_limit=0)
        self.assertTrue(math.isinf(result))
    
    def test_optimal_path_uses_max_haunted(self):
        teleport_matrix = [
            [0, 3, 47, 52],
            [3, 0, 4, 41],
            [47, 4, 0, 6],
            [52, 41, 6, 0],
        ]
        haunted_state = [0, 1, 1, 0]
        result = project.run_min_dp(teleport_matrix, haunted_state, haunted_limit=2)
        self.assertEqual(result, 13)

if __name__ == "__main__":
    unittest.main()