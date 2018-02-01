
"""
Copyright 2013 Steven Diamond

This file is part of CVXPY.

CVXPY is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

CVXPY is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with CVXPY.  If not, see <http://www.gnu.org/licenses/>.
"""

from cvxpy.expressions.variable import Variable


def cumsum_canon(expr, args):
    """Cumulative sum.
    """
    X = args[0]
    axis = expr.axis
    # Implicit O(n) definition:
    # X = Y[:1,:] - Y[1:, :]
    Y = Variable(expr.shape)
    if axis == 0:
        constr = [X[1:, :] == Y[1:, :] - Y[:-1, :], Y[0, :] == X[0, :]]
    else:
        constr = [X[:, 1:] == Y[:, 1:] - Y[:, :-1], Y[:, 0] == X[:, 0]]
    return (Y, constr)