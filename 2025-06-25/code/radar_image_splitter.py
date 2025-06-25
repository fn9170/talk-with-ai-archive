# radar_image_splitter.py - 雷达图片分割器
import cv2
import numpy as np
import os
from pathlib import Path
import json

class RadarImageSplitter:
    def __init__(self, target_size=640, overlap_ratio=0.3):
        """
        雷达图片分割器
        
        Args:
            target_size: 目标分割尺寸 (640)
            overlap_ratio: 重叠比例 (0.3 = 30%)
        """
        self.target_size = target_size
        self.overlap_ratio = overlap_ratio
        self.stride = int(target_size * (1 - overlap_ratio))
        
        print(f"🎯 分割器配置:")
        print(f"   目标尺寸: {target_size}×{target_size}")
        print(f"   重叠比例: {overlap_ratio*100}%")
        print(f"   步长: {self.stride}")
    
    def split_image(self, image_path, output_dir):
        """
        分割单张长图
        
        Args:
            image_path: 输入图片路径
            output_dir: 输出目录
            
        Returns:
            split_info: 分割信息字典
        """
        # 读取图片
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"无法读取图片: {image_path}")
        
        height, width = image.shape[:2]
        print(f"📏 原图尺寸: {width}×{height}")
        
        # 创建输出目录
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # 获取原图文件名（不含扩展名）
        base_name = Path(image_path).stem
        
        # 分割信息记录
        split_info = {
            "original_image": str(image_path),
            "original_size": [width, height],
            "target_size": self.target_size,
            "overlap_ratio": self.overlap_ratio,
            "stride": self.stride,
            "splits": []
        }
        
        split_count = 0
        
        # 横向分割（x方向）
        x = 0
        while x < width:
            # 确保不超出边界
            if x + self.target_size > width:
                x = max(0, width - self.target_size)
            
            # 纵向处理（y方向）
            if height >= self.target_size:
                y = (height - self.target_size) // 2  # 居中
            else:
                y = 0  # 顶部对齐，后续需要padding
            
            # 提取子图
            if height >= self.target_size:
                sub_image = image[y:y+self.target_size, x:x+self.target_size]
            else:
                # 高度不足时，进行padding
                sub_image = image[y:height, x:x+self.target_size]
                # 底部padding到640
                padding = self.target_size - height
                sub_image = cv2.copyMakeBorder(
                    sub_image, 0, padding, 0, 0, 
                    cv2.BORDER_CONSTANT, value=[0, 0, 0]
                )
            
            # 保存子图
            split_filename = f"{base_name}_split_{split_count:03d}.jpg"
            split_path = output_path / split_filename
            cv2.imwrite(str(split_path), sub_image)
            
            # 记录分割信息
            split_info["splits"].append({
                "filename": split_filename,
                "position": [x, y],
                "size": [self.target_size, self.target_size]
            })
            
            split_count += 1
            print(f"  生成子图 {split_count}: {split_filename} (位置: {x}, {y})")
            
            # 移动到下一个位置
            if x + self.target_size >= width:
                break  # 已经到达最右边
            
            x += self.stride
        
        print(f"✅ 分割完成: {split_count} 个子图")
        
        # 保存分割信息
        info_file = output_path / f"{base_name}_split_info.json"
        with open(info_file, 'w', encoding='utf-8') as f:
            json.dump(split_info, f, indent=2, ensure_ascii=False)
        
        return split_info
    
    def visualize_splits(self, image_path, split_info):
        """
        可视化分割区域
        """
        try:
            import matplotlib.pyplot as plt
            import matplotlib.patches as patches
        except ImportError:
            print("❌ 需要安装matplotlib: pip install matplotlib")
            return
        
        # 读取原图
        image = cv2.imread(image_path)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # 创建图形
        fig, ax = plt.subplots(1, 1, figsize=(20, 6))
        ax.imshow(image_rgb)
        
        # 绘制分割区域
        colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
        for i, split in enumerate(split_info['splits']):
            x, y = split['position']
            size = split['size'][0]
            
            # 绘制矩形框
            rect = patches.Rectangle(
                (x, y), size, size,
                linewidth=2, 
                edgecolor=colors[i % len(colors)], 
                facecolor='none', 
                alpha=0.8
            )
            ax.add_patch(rect)
            
            # 添加编号
            ax.text(x + 10, y + 30, str(i), 
                   color='white', fontsize=12, fontweight='bold',
                   bbox=dict(boxstyle="round,pad=0.3", facecolor=colors[i % len(colors)]))
        
        ax.set_title(f"分割预览 - 原图({split_info['original_size'][0]}×{split_info['original_size'][1]}) → {len(split_info['splits'])}个子图")
        ax.axis('off')
        
        plt.tight_layout()
        plt.show()

# 使用示例
def demo():
    """
    演示如何使用分割器
    """
    print("🚀 雷达图片分割器演示")
    print("=" * 40)
    
    # 创建分割器
    splitter = RadarImageSplitter(
        target_size=640,
        overlap_ratio=0.3  # 30%重叠
    )
    
    # 创建一个模拟的长条图片（如果没有真实图片）
    demo_image = create_demo_image()
    demo_path = "demo_radar_8000x640.jpg"
    cv2.imwrite(demo_path, demo_image)
    print(f"📝 创建演示图片: {demo_path}")
    
    # 分割图片
    try:
        split_info = splitter.split_image(demo_path, "output/splits/")
        
        # 可视化分割效果
        splitter.visualize_splits(demo_path, split_info)
        
        print(f"\n📊 分割结果:")
        print(f"   原图尺寸: {split_info['original_size']}")
        print(f"   子图数量: {len(split_info['splits'])}")
        print(f"   重叠比例: {split_info['overlap_ratio']*100}%")
        print(f"   输出目录: output/splits/")
        
    except Exception as e:
        print(f"❌ 分割失败: {e}")

def create_demo_image(width=8000, height=640):
    """
    创建一个模拟的雷达图片用于演示
    """
    # 创建基础图像
    image = np.zeros((height, width, 3), dtype=np.uint8)
    
    # 添加背景噪声
    noise = np.random.randint(0, 30, (height, width, 3), dtype=np.uint8)
    image = cv2.add(image, noise)
    
    # 添加一些模拟的雷达回波（矩形块）
    colors = [(0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 255, 0)]
    
    # 在不同位置添加目标
    targets = [
        (500, height//2-30, 60, 60),    # 左侧目标
        (1500, height//2-20, 40, 40),   # 中间目标1
        (3200, height//2-25, 50, 50),   # 中间目标2（跨越分割线）
        (4800, height//2-35, 70, 70),   # 中间目标3
        (6500, height//2-15, 30, 30),   # 右侧目标1
        (7200, height//2-40, 80, 80),   # 右侧目标2
    ]
    
    for i, (x, y, w, h) in enumerate(targets):
        color = colors[i % len(colors)]
        cv2.rectangle(image, (x, y), (x+w, y+h), color, -1)
        
        # 添加标签
        cv2.putText(image, f"T{i+1}", (x+5, y+h-5), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    
    # 添加网格线帮助可视化
    for x in range(0, width, 640):
        cv2.line(image, (x, 0), (x, height), (128, 128, 128), 1)
    
    return image

if __name__ == "__main__":
    # 运行演示
    demo() 