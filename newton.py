import numpy as np

def jacobian_example(x, y):
    return np.array([[1, 1], [2 * x, 2 * y]])

def function_example(x, y):
    return np.array([-x - y + 3, -x ** 2 - y ** 2 + 9])

def x_s_by_gauss(J, b):
    return np.linalg.solve(J, b)

def x_plus_1(x_delta, x_previous=np.array([1, 5])):
    x_next = x_previous + x_delta
    return np.squeeze(x_next)

def loopNewton():
    x_old = np.array([1, 5])

    while True:
        jacobian = jacobian_example(x_old[0], x_old[1])
        function = function_example(x_old[0], x_old[1])

        delta = x_s_by_gauss(jacobian, function)
        x_new = x_plus_1(delta, x_old)
        error = np.max(np.abs(delta))

        print("delta:", delta)
        print("error:", error)
        print("new x:", x_new)

        if error < 0.05:
            break

        x_old = x_new

loopNewton()
