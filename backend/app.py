from flask import Flask, render_template, request
import numpy as np
from fractions import Fraction

app = Flask(__name__)

#Uses Gaussian elimination on a 3x3 user-inputted matrix
#to reduce to Reduced Row Echelon Form
def row_reduce(matrix):
    
    #Sets matrix to a list of fractions
    matrix = [[Fraction(x) for x in row] for row in matrix]
    rows, cols = len(matrix), len(matrix[0])

    #Row reduction
    for i in range(min(rows, cols)):
        if matrix[i][i] != 0:
            matrix[i] = [x / matrix[i][i] for x in matrix[i]]
        for j in range(rows):
            if j != i:
                matrix[j] = [matrix[j][k] - matrix[j][i] * matrix[i][k] for k in range(cols)]
    return matrix

@app.route('/', methods = ['GET', 'POST'])

def index():
    if request.method == 'POST':
        #Get matrix and call row_reduce
        #Store the reduced matrix in matrix_reduced
        matrix = [
            [Fraction(request.form['a11']), Fraction(request.form['a12']), Fraction(request.form['a13'])],
            [Fraction(request.form['a21']), Fraction(request.form['a22']), Fraction(request.form['a23'])],
            [Fraction(request.form['a31']), Fraction(request.form['a32']), Fraction(request.form['a33'])]
        ]
        matrix_reduced = row_reduce(matrix)
        return render_template('index.html', matrix=matrix, matrix_reduced=rmatrix_reduced)
    return render_template('index.html', matrix=None, matrix_reduced=None) #Set matrix to empty when app is first loaded

if __name__ == '__main__':
    app.run(debug=True) 