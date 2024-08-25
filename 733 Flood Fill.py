def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    """
    starting_pixel_color = image[sr][sc]
    row_boundary = len(image) - 1
    column_boundary = len(image[0]) - 1
    stack = []  # keep track of pixels to be examined,[[行，列]], and to be modified
    stack.append([sr, sc])
    max_round = (row_boundary + 1) * (column_boundary + 1)
    count = 0

    while len(stack) > 0 and count <= max_round:
        to_be_examined_pixel = stack.pop()
        row = to_be_examined_pixel[0]
        column = to_be_examined_pixel[1]

        if 0 < row:#上
            up = image[row - 1][column]
            if up == starting_pixel_color and [row - 1, column] not in stack:
                stack.append([row - 1, column])

        if row < row_boundary:#下
            down = image[row + 1][column]
            if down == starting_pixel_color and [row + 1, column] not in stack:
                stack.append([row + 1, column])

        if 0 < column:#左
            left = image[row][column - 1]
            if left == starting_pixel_color and [row, column - 1] not in stack:
                stack.append([row, column - 1])

        if column < column_boundary:#右
            right = image[row][column + 1]
            if right == starting_pixel_color and [row, column + 1] not in stack:
                stack.append([row, column + 1])

        image[row][column] = color
        count += 1

    return image

    >>> image = [[1,1,1],[1,1,0],[1,0,1]]
    >>> floodFill(image, 1, 1, 2)
    [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    >>> image = [[0,0,0],[0,0,0]]
    >>> floodFill(image, 0, 0, 0)
    [[0, 0, 0], [0, 0, 0]]
    """
    starting_pixel_color = image[sr][sc]  # sr: row; sc: column
    if starting_pixel_color == color:
        return image
    row_boundary = len(image) - 1
    column_boundary = len(image[0]) - 1

    image[sr][sc] = color
    # up
    if 0 <= sr - 1:
        if image[sr - 1][sc] == starting_pixel_color:
            floodFill(image, sr - 1, sc, color)
    # down
    if sr + 1 <= row_boundary:
        if image[sr + 1][sc] == starting_pixel_color:
            floodFill(image, sr + 1, sc, color)
    # left
    if 0 <= sc - 1:
        if image[sr][sc - 1] == starting_pixel_color:
            floodFill(image, sr, sc - 1, color)
    # right
    if sc + 1 <= column_boundary:
        if image[sr][sc + 1] == starting_pixel_color:
            floodFill(image, sr, sc + 1, color)

    return image
