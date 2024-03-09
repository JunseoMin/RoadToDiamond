def solution(triangle):
    answer = 0    
    dy_pyra = [[0 for __ in range(len(triangle[_]))] for _ in range(len(triangle))]
    
    for depth in range(len(triangle)):
        for idx in range(len(triangle[depth])):
            if idx == 0 and depth == 0:
                dy_pyra[0][0] = triangle[0][0]
            elif idx == 0:
                dy_pyra[depth][idx] = dy_pyra[depth-1][0] + triangle[depth][idx]
            elif idx == len(triangle[depth])-1:
                dy_pyra[depth][idx] = dy_pyra[depth-1][len(triangle[depth])-2] + triangle[depth][idx]
            else:
                dy_pyra[depth][idx] = max(dy_pyra[depth-1][idx-1],dy_pyra[depth-1][idx]) + triangle[depth][idx]
                
    return max(dy_pyra[len(triangle)-1])