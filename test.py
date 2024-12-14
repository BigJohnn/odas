import cv2
import numpy as np
# 创建一个纯白色的 100x100 图像
white_image = np.ones((100, 100, 3), dtype=np.uint8) * 255  # 每个像素点的值为 255

# 使用 cv2.imshow 显示图像
cv2.imshow("White Image", white_image)

# 等待用户按键并关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()