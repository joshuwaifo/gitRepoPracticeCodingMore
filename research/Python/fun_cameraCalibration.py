from numpy import diag

def my_calibration( sz ):
    row, col = sz
    fx = ( 2555 * col ) / 2592
    fy = ( 2586 * row ) / 1936
    K = diag(
        [
            fx,
            fy,
            1
        ]
    )
    K[ 0, 2 ] = 0.5 * col
    K[ 1, 2 ] = 0.5 * row
    return K