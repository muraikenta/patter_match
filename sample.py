# coding: UTF-8
import cv2

image_paths = {
  "header": [1, 2, 3, 4],
  "sidebar": [1, 2, 3, 4, 5, 6]
}
 
# imread
# http://docs.opencv.org/3.0-beta/modules/imgcodecs/doc/reading_and_writing_images.html#imread

src = cv2.imread("wrong_answer2.png", 1) # 三次元配列を返す
for key, value in image_paths.iteritems():
  for i in value:
    print '----------------------------------------'
    image_path = key + '/' + key + str(i) + '.png'
    print image_path
    tmp = cv2.imread(image_path, 1)
     
    res = cv2.matchTemplate(src, tmp, cv2.TM_CCOEFF_NORMED)
     
    (minval, maxval, minloc, maxloc) = cv2.minMaxLoc(res)

    print "score = max: {0}\n".format(maxval)
    if maxval < 0.9:
      print "OUT............"
    else:
      print "OK!!!!!!!!!!!!!"
      (h, w, d) = tmp.shape
      # (h, w) = tmp.shape
     
      rect_1 = (maxloc[0], maxloc[1])
      rect_2 = (maxloc[0] + w, maxloc[1] + h)
      # print "size ({0}, {1})\n".format(w, h)
      # cv2.rectangle(src, rect_1, rect_2, 0x000000)
       
      result_path = key + '/' + key + str(i) + '_result.png'
      # cv2.imwrite(result_path, src)