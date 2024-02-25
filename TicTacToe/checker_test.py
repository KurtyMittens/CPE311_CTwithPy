
mat = [
  [1,1,1],
  [1,1,1],
  [1,1,1]
]

def sum_lines(matrix):
  center = matrix[int(len(matrix)/2)][int(len(matrix)/2)]
  scoresDict = {"vert":[0 for i in range(len(matrix[0]))], "horz":[0 for i in range(len(matrix[0]))], "diag":[0, center]} # assuming all the  matrix are odd square matrix
  for row in range(len(matrix)):
    for collumn in range(len(matrix[row])):
      scoresDict["horz"][row] += matrix[row][collumn]
      scoresDict["vert"][collumn] += matrix[row][collumn]
      if row == collumn:
        scoresDict['diag'][0] += matrix[row][collumn]
      elif row  == len(matrix[row]) - collumn - 1:
        scoresDict["diag"][1] += matrix[row][collumn]
  print(scoresDict)

sum_lines(mat)
