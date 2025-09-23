import cv2
import numpy as np

def add_watermark_with_bitwise(background_path, watermark_path, output_path, position=(10, 10), alpha=0.7):
    """
    使用位操作给图片添加水印
    
    参数:
    - background_path: 背景图片路径
    - watermark_path: 水印图片路径
    - output_path: 输出图片路径
    - position: 水印位置 (x, y)
    - alpha: 水印透明度 (0-1)
    """
    
    # 读取背景图片和水印图片
    background = cv2.imread(background_path)
    watermark = cv2.imread(watermark_path, cv2.IMREAD_UNCHANGED)
    
    if background is None:
        print(f"错误：无法读取背景图片 {background_path}")
        return
    if watermark is None:
        print(f"错误：无法读取水印图片 {watermark_path}")
        return
    
    # 获取图片尺寸
    bg_height, bg_width = background.shape[:2]
    wm_height, wm_width = watermark.shape[:2]
    
    # 调整水印位置，确保不超出背景范围
    x, y = position
    x = max(0, min(x, bg_width - wm_width))
    y = max(0, min(y, bg_height - wm_height))
    
    # 创建水印的ROI区域
    roi = background[y:y+wm_height, x:x+wm_width]
    
    # 处理不同通道的水印图片
    if watermark.shape[2] == 4:  # 带有alpha通道的水印
        # 分离BGR和alpha通道
        watermark_bgr = watermark[:, :, :3]
        watermark_alpha = watermark[:, :, 3] / 255.0 * alpha
        
        # 创建alpha通道的3D版本
        watermark_alpha_3d = np.stack([watermark_alpha] * 3, axis=2)
        
        # 使用位操作进行混合
        # 1. 水印区域乘以alpha
        watermark_weighted = cv2.multiply(watermark_bgr.astype(np.float32), 
                                         watermark_alpha_3d.astype(np.float32))
        
        # 2. 背景区域乘以(1-alpha)
        background_weighted = cv2.multiply(roi.astype(np.float32), 
                                          1.0 - watermark_alpha_3d.astype(np.float32))
        
        # 3. 合并两个部分
        blended = cv2.add(watermark_weighted, background_weighted)
        
    else:  # 不带alpha通道的水印
        # 创建透明度掩码
        alpha_mask = np.ones((wm_height, wm_width, 3)) * alpha
        
        # 使用位操作进行混合
        # 1. 水印区域乘以alpha
        watermark_weighted = cv2.multiply(watermark.astype(np.float32), 
                                         alpha_mask.astype(np.float32))
        
        # 2. 背景区域乘以(1-alpha)
        background_weighted = cv2.multiply(roi.astype(np.float32), 
                                          1.0 - alpha_mask.astype(np.float32))
        
        # 3. 合并两个部分
        blended = cv2.add(watermark_weighted, background_weighted)
    
    # 将混合后的区域转换回uint8并放回原图
    blended_uint8 = np.clip(blended, 0, 255).astype(np.uint8)
    background[y:y+wm_height, x:x+wm_width] = blended_uint8
    
    # 保存结果
    cv2.imwrite(output_path, background)
    print(f"水印添加成功！输出文件: {output_path}")
    
    # 显示结果
    cv2.imshow('Original', cv2.imread(background_path))
    cv2.imshow('Watermarked', background)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def create_text_watermark(text, size=(200, 100), font_scale=1.0, thickness=2):
    """
    创建文字水印图片
    """
    # 创建透明背景
    watermark = np.zeros((size[1], size[0], 4), dtype=np.uint8)
    
    # 设置文字属性
    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (255, 255, 255, 255)  # 白色，不透明
    
    # 获取文字尺寸
    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
    text_x = (size[0] - text_size[0]) // 2
    text_y = (size[1] + text_size[1]) // 2
    
    # 绘制文字
    cv2.putText(watermark, text, (text_x, text_y), font, font_scale, color, thickness)
    
    return watermark

def add_multiple_watermarks(background_path, watermark_path, output_path, positions, alpha=0.5):
    """
    添加多个水印
    """
    background = cv2.imread(background_path)
    watermark = cv2.imread(watermark_path, cv2.IMREAD_UNCHANGED)
    
    if background is None or watermark is None:
        print("错误：无法读取图片")
        return
    
    bg_height, bg_width = background.shape[:2]
    wm_height, wm_width = watermark.shape[:2]
    
    for position in positions:
        x, y = position
        x = max(0, min(x, bg_width - wm_width))
        y = max(0, min(y, bg_height - wm_height))
        
        roi = background[y:y+wm_height, x:x+wm_width]
        
        if watermark.shape[2] == 4:
            watermark_bgr = watermark[:, :, :3]
            watermark_alpha = watermark[:, :, 3] / 255.0 * alpha
            watermark_alpha_3d = np.stack([watermark_alpha] * 3, axis=2)
            
            watermark_weighted = cv2.multiply(watermark_bgr.astype(np.float32), 
                                             watermark_alpha_3d.astype(np.float32))
            background_weighted = cv2.multiply(roi.astype(np.float32), 
                                              1.0 - watermark_alpha_3d.astype(np.float32))
            blended = cv2.add(watermark_weighted, background_weighted)
        else:
            alpha_mask = np.ones((wm_height, wm_width, 3)) * alpha
            watermark_weighted = cv2.multiply(watermark.astype(np.float32), 
                                             alpha_mask.astype(np.float32))
            background_weighted = cv2.multiply(roi.astype(np.float32), 
                                              1.0 - alpha_mask.astype(np.float32))
            blended = cv2.add(watermark_weighted, background_weighted)
        
        blended_uint8 = np.clip(blended, 0, 255).astype(np.uint8)
        background[y:y+wm_height, x:x+wm_width] = blended_uint8
    
    cv2.imwrite(output_path, background)
    print(f"多个水印添加成功！输出文件: {output_path}")

# 使用示例
if __name__ == "__main__":
    # 示例1：添加图片水印
    print("示例1：添加图片水印")
    add_watermark_with_bitwise(
        background_path='cat.png',  # 替换为你的背景图片路径
        watermark_path='cat.1.jpg',    # 替换为你的水印图片路径
        output_path='output_with_watermark.jpg',
        position=(50, 50),
        alpha=0.2
    )
    
    # # 示例2：创建并添加文字水印
    # print("\n示例2：添加文字水印")
    # text_watermark = create_text_watermark("My Watermark", font_scale=1.5)
    # cv2.imwrite('text_watermark.png', text_watermark)
    
    # add_watermark_with_bitwise(
    #     background_path='background.jpg',
    #     watermark_path='text_watermark.png',
    #     output_path='output_with_text_watermark.jpg',
    #     position=(100, 100),
    #     alpha=0.8
    # )
    
    # # 示例3：添加多个水印
    # print("\n示例3：添加多个水印")
    # positions = [(10, 10), (200, 100), (400, 300)]
    # add_multiple_watermarks(
    #     background_path='background.jpg',
    #     watermark_path='watermark.png',
    #     output_path='output_multiple_watermarks.jpg',
    #     positions=positions,
    #     alpha=0.4
    # )