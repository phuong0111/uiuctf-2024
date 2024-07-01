import liblll

# Private Key
S, m, n, k = [2, 3, 7, 14, 30, 57, 120, 251], 41, 491, 12

# Public Key
T = [66128, 61158, 36912, 65196, 15611, 45292, 84119, 65338]

# Ciphertext
ct = [273896, 179019, 273896, 247527, 208558, 227481, 328334, 179019, 336714, 292819, 102108, 208558, 336714, 312723, 158973, 208700, 208700, 163266, 244215, 336714, 312723, 102108, 336714, 142107, 336714, 167446, 251565, 227481, 296857, 336714, 208558, 113681, 251565, 336714, 227481, 158973, 147400, 292819, 289507]

# LLL Algorithm
flag = ""
for C in ct:
    M = liblll.create_matrix_from_knapsack(T, C)
    M_reduced = liblll.lll_reduction(M)
    U = liblll.best_vect_knapsack(M_reduced)
    flag+=(chr(int((''.join(map(str, U))),2)))

    assert liblll.scalar_product(T, U) == C
print(flag)

# knapsack cryptosystem
# https://drx.home.blog/2019/02/24/crypto-he-ma-merkle-hellman/
# uiuctf{i_g0t_sleepy_s0_I_13f7_th3_fl4g}

# Bài này là hệ mã knapsack, dấu hiệu nhận biết là lúc sinh khoá, nó cần 1 bộ số nguyên tăng chặt sao cho số ở sau lớn hơn tổng các số ở trước nó
# VD: [1, 2, 4, 9, 20]
# Bọn e đọc hàm get_b nó rất rõ dấu hiệu kia
# Xong tiếp theo thì hỏi google thôi :)))