import sys

# ---------------------------------------
# 입출력: 9줄 x 9개 정수(빈 칸은 0) 입력, 해를 출력
# ---------------------------------------

data = sys.stdin.read().strip().split()
if len(data) != 81:
    # 온라인 저지 대응: 공백 개수 변형에도 안전
    grid = []
    for _ in range(9):
        row = list(map(int, sys.stdin.readline().split()))
        grid.append(row)
else:
    nums = list(map(int, data))
    grid = [nums[i*9:(i+1)*9] for i in range(9)]

# 비트마스크: 숫자 d(1..9) -> (1<<d)
ALL = 0b1111111110  # 1~9 사용 가능 비트 마스크

row_mask = [0] * 9
col_mask = [0] * 9
box_mask = [0] * 9

def box_id(r, c):
    return (r // 3) * 3 + (c // 3)

# 초기 마스크 세팅
for r in range(9):
    for c in range(9):
        d = grid[r][c]
        if d:
            bit = 1 << d
            row_mask[r] |= bit
            col_mask[c] |= bit
            box_mask[box_id(r, c)] |= bit

# 빈 칸 목록 (동적으로 MRV로 선택하지만, 위치 캐시는 유지)
empties = [(r, c) for r in range(9) for c in range(9) if grid[r][c] == 0]

# 비트 -> 숫자 빠른 매핑
bit_to_digit = {1 << d: d for d in range(1, 10)}

def candidates(r, c):
    used = row_mask[r] | col_mask[c] | box_mask[box_id(r, c)]
    return ALL & ~used  # 가능한 숫자 비트셋

def solve():
    # MRV: 후보 수가 최소인 칸을 고른다
    target_idx = -1
    target_cands = 0
    min_cnt = 10  # 후보 최소 개수 초기값(불가능한 큰 값)
    for i, (r, c) in enumerate(empties):
        if grid[r][c] != 0:
            continue
        cand = candidates(r, c)
        if cand == 0:
            return False
        # 비트셋 원소 수 계산
        cnt = cand.bit_count()
        if cnt < min_cnt:
            min_cnt = cnt
            target_idx = i
            target_cands = cand
            if cnt == 1:
                break  # 더 찾을 필요 없음

    if target_idx == -1:
        return True  # 모든 칸 채움

    r, c = empties[target_idx]

    # 시도: 후보 비트 순회(최저 비트부터)
    cand = target_cands
    while cand:
        bit = cand & -cand
        cand ^= bit
        d = bit_to_digit[bit]

        # 배치
        grid[r][c] = d
        row_mask[r] |= bit
        col_mask[c] |= bit
        b = box_id(r, c)
        box_mask[b] |= bit

        if solve():
            return True

        # 되돌리기
        grid[r][c] = 0
        row_mask[r] ^= bit
        col_mask[c] ^= bit
        box_mask[b] ^= bit

    return False

solve()

# 출력
out_lines = []
for r in range(9):
    out_lines.append(" ".join(str(grid[r][c]) for c in range(9)))
print("\n".join(out_lines))
