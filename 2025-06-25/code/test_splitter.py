# test_splitter.py - 测试雷达图片分割器
from radar_image_splitter import RadarImageSplitter
import os

def test_splitter():
    """
    测试分割器功能
    """
    print("🧪 测试雷达图片分割器")
    print("=" * 40)
    
    # 创建分割器 - 30%重叠避免目标被切断
    splitter = RadarImageSplitter(
        target_size=640,
        overlap_ratio=0.3
    )
    
    # 检查是否有真实图片，否则使用演示图片
    test_images = [
        "radar_8000x640.jpg",
        "radar_image.jpg", 
        "long_image.jpg"
    ]
    
    image_path = None
    for img in test_images:
        if os.path.exists(img):
            image_path = img
            break
    
    if image_path is None:
        print("📝 未找到测试图片，创建演示图片...")
        # 运行演示
        from radar_image_splitter import demo
        demo()
    else:
        print(f"📷 使用图片: {image_path}")
        
        # 分割图片
        split_info = splitter.split_image(image_path, "output/splits/")
        
        # 显示结果
        print(f"\n📊 分割结果:")
        print(f"   原图: {split_info['original_size'][0]} × {split_info['original_size'][1]}")
        print(f"   子图: {len(split_info['splits'])} 个")
        print(f"   尺寸: {split_info['target_size']} × {split_info['target_size']}")
        print(f"   重叠: {split_info['overlap_ratio']*100}%")
        print(f"   步长: {split_info['stride']} 像素")
        
        # 计算覆盖率
        total_pixels = split_info['original_size'][0] * split_info['original_size'][1]
        split_pixels = len(split_info['splits']) * split_info['target_size'] * split_info['target_size']
        coverage = split_pixels / total_pixels
        
        print(f"   覆盖率: {coverage:.1f}x (重叠导致)")
        
        print(f"\n📁 文件输出:")
        print(f"   目录: output/splits/")
        for i, split in enumerate(split_info['splits'][:5]):  # 只显示前5个
            print(f"   {split['filename']} - 位置({split['position'][0]}, {split['position'][1]})")
        if len(split_info['splits']) > 5:
            print(f"   ... 还有 {len(split_info['splits'])-5} 个文件")

if __name__ == "__main__":
    test_splitter() 