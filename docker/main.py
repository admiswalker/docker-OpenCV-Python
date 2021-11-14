import cv2 as cv

def test():
    img = cv.imread('./test_in.png')
    print(type(img))
    print(img.shape)
    img_rotate_180 = cv.rotate(img, cv.ROTATE_180)
    cv.imwrite('test_out.png', img_rotate_180)

def main():
    print(cv.__version__)
    test()

main()
