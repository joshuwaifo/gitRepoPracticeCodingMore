try:
    import homography
    import camera
    import sift

    # compute features
    sift.process_image(
        'book_frontal.JPG',
        'im0.sift'
    )

    l0, d0 = sift.read_features_from_file( 'im0.sift' )

    sift.process_image(
        'book_perspective.JPG',
        'im1.sift'
    )

    l1, d1 = sift.read_features_from_file( 'im1.sift' )

except ModuleNotFoundError:
    print("I am currently unable to import the module homography")