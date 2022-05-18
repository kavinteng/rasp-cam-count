import cv2

def main_flask(url,cap = 0,start = None,time_ref = 10,polygon_employ=None, polygon_nodetect=None):
    cap = cv2.VideoCapture(cap)

    while True:
        if start == None:
            start = time.time()
        end = time.time()
        _, frame = cap.read()
        frame = cv2.resize(frame, (640, 360))

        if end - start > time_ref:
            imencoded = cv2.imencode(".jpg", frame)[1]
            status_code = request_post_image(url,imencoded,polygon_employ,polygon_nodetect)
            start = None

            cv2.waitKey(1)
            if status_code != 200:
                print('break')
                break



    cap.release()
    cv2.destroyAllWindows()
    return status_code

def request_post_image(url, image,polygon_employ,polygon_nodetect):
    file = {'file': ('image.jpg', image.tostring(), 'image/jpeg', {'Expires': '0'})}
    data = {'poly_employ': polygon_employ,'poly_nodetect': polygon_nodetect}
    post_img = requests.post(url, files=file)
    if post_img.status_code == 200:
        response = requests.post(url, json=data)

        print('------posting------')
        if response.ok:
            print("Upload completed successfully!")
            try:
                print(response.json())
            except:
                print('receive')
        else:
            print("Fall upload!")
            response.status_code

        return response.status_code

def set_polygon():
    global array1,array2, img
    # reading the image
    size_img_vdo = (640, 360)
    cap = cv2.VideoCapture(0)
    array1 = []
    array2 = []
    check_click = 0
    while True:
        _, img = cap.read()
        img = cv2.resize(img, size_img_vdo)

        # displaying the image
        # cv2.imshow('image', img)

        # cv2.setMouseCallback('image', click_event)
        # if len(array1) != 0:
        #     print(array1)
        if check_click == 2:
            contours1 = np.array(result1)
            contours2 = np.array(result2)
            cv2.fillPoly(img, pts=[contours2], color=(2, 255, 255))
            cv2.fillPoly(img, pts=[contours1], color=(1, 0, 255))
        # cv2.fillPoly(img, pts=[result3], color=(3, 0, 255))
        cv2.imshow('image', img)
        cv2.setMouseCallback('image', click_event)
        k = cv2.waitKey(0)
        if (k == ord('q')) and (check_click ==3): #q
            break
        elif k == ord('d'): #d
            print('clear array')
            array1 = []
            array2 = []
            check_click = 0
        elif (k == ord('z')) and (check_click ==0): #z
            print('save employee')
            result1 = array1
            array1 = []
            array2 = []
            check_click += 1
        elif (k == ord('x')) and (check_click ==1): #x
            print('save customer')
            result2 = array2
            array1 = []
            array2 = []
            check_click += 1
        elif (k == ord('c')) and (check_click ==2): #c
            try:
                print(f'check array\n{result1}\n{result2}')
                check_click += 1
            except:
                print(f'Non save value: {array1}')
        else:
            pass
        # close the window
    cv2.destroyAllWindows()

    return result1, result2