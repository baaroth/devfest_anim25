import sys

def parse_grid(topographic_map):
    """Parse input into a 2D grid."""
    lines = topographic_map.strip().split('\n')
    return [[int(c) if c.isdigit() else -1 for c in line] for line in lines]

def get_trailheads(grid):
    """Find all positions with height 0."""
    return [(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 0]

def count_reachable_nines(grid, start_row, start_col):
    """Part 1: Count unique 9-height positions reachable from trailhead."""
    rows, cols = len(grid), len(grid[0])
    reachable_nines = set()
    queue = [(start_row, start_col, 0)]
    visited = {(start_row, start_col, 0)}

    while queue:
        row, col, height = queue.pop(0)

        if height == 9:
            reachable_nines.add((row, col))
            continue

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == height + 1:
                state = (nr, nc, height + 1)
                if state not in visited:
                    visited.add(state)
                    queue.append(state)

    return len(reachable_nines)

def count_distinct_paths(grid, row, col, height, memo):
    """Part 2: Count all distinct paths from current position to height 9."""
    if height == 9:
        return 1

    if (row, col, height) in memo:
        return memo[(row, col, height)]

    rows, cols = len(grid), len(grid[0])
    total = 0

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = row + dr, col + dc

        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == height + 1:
            total += count_distinct_paths(grid, nr, nc, height + 1, memo)

    memo[(row, col, height)] = total
    return total

def solve(topographic_map):
    """Solve both parts of the puzzle."""
    grid = parse_grid(topographic_map)
    trailheads = get_trailheads(grid)

    # Part 1: Sum of scores (unique endpoints)
    part1 = sum(count_reachable_nines(grid, r, c) for r, c in trailheads)

    # Part 2: Sum of ratings (distinct paths)
    memo = {}
    part2 = sum(count_distinct_paths(grid, r, c, 0, memo) for r, c in trailheads)

    return part1, part2

# Main execution
puzzle_input = sys.stdin.read()
if puzzle_input.strip():
    part1, part2 = solve(puzzle_input)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
else:
    print("No input provided.")