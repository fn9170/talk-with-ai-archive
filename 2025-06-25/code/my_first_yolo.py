from ultralytics import YOLO

# 1. 加载预训练模型
model = YOLO('yolov8n.pt')  # n表示nano，最小最快的版本

# 2. 对图片进行检测
results = model('images.jpeg')
print(results)

# 3. 显示结果
results[0].show()

# 4. 保存结果图片
results[0].save('result.jpg')

print("检测完成！结果保存在 result.jpg")