# ====================================== O(n³) ======================================

def cubico(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)

cubico(3)