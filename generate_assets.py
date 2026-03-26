"""
Gemini 3 Pro Image (Nano Banana Pro) 遊戲素材生成腳本
使用 Google Gemini API 生成美式漫畫風格的貓狗大戰遊戲素材
"""

import os
import time
from google import genai
from google.genai import types

# API 設定
# 請設定環境變數 GEMINI_API_KEY 或直接在此填入 API key
API_KEY = os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY_HERE")
MODEL = "gemini-2.5-flash-image"  # Gemini 圖片生成模型

# 初始化客戶端
client = genai.Client(api_key=API_KEY)

# 輸出目錄
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# 通用風格描述
STYLE_BASE = """
American comic book style, cel-shaded illustration, bold black outlines,
vibrant saturated colors, dynamic pose, expressive cartoon character,
high quality game asset, clean vector-like art, professional illustration,
suitable for 2D game sprite, front-facing view
"""

# 圖片生成配置
IMAGE_CONFIG = {
    "resolution": "1024x1024",  # 1K 解析度
    "aspect_ratio": "1:1",      # 正方形適合遊戲素材
}

# 所有需要生成的圖片定義
ASSETS_TO_GENERATE = [
    # ========== 貓咪角色 ==========
    {
        "filename": "assets/cat/idle.png",
        "prompt": f"""
        {STYLE_BASE}

        A cute but fierce cartoon CAT character in IDLE/STANDING pose.
        - Orange tabby cat with big expressive eyes
        - Standing upright on two legs like a mascot character
        - Confident and ready stance, arms slightly raised
        - Wearing a small red bandana around neck
        - Fluffy tail curled upward
        - Friendly but competitive expression
        - Full body visible, centered in frame
        - Clean white/transparent background style (solid light gray #f0f0f0)
        - Size: 1024x1024 pixels, high detail
        """
    },
    {
        "filename": "assets/cat/attack.png",
        "prompt": f"""
        {STYLE_BASE}

        A cute but fierce cartoon CAT character in ATTACK/THROWING pose.
        - Same orange tabby cat with red bandana
        - Dynamic throwing motion, one arm extended forward
        - Determined fierce expression, slight smirk
        - Body leaning into the throw
        - Action lines suggesting movement
        - Intense focused eyes
        - Full body visible, centered in frame
        - Clean white/transparent background style (solid light gray #f0f0f0)
        - Size: 1024x1024 pixels, high detail
        """
    },
    {
        "filename": "assets/cat/hurt.png",
        "prompt": f"""
        {STYLE_BASE}

        A cute cartoon CAT character in HURT/DAMAGED pose.
        - Same orange tabby cat with red bandana
        - Pained expression, eyes squeezed shut or X eyes
        - Recoiling backward from impact
        - Small stars or impact symbols around head
        - Fur slightly ruffled
        - Arms up in defensive position
        - Full body visible, centered in frame
        - Clean white/transparent background style (solid light gray #f0f0f0)
        - Size: 1024x1024 pixels, high detail
        """
    },
    {
        "filename": "assets/cat/projectile.png",
        "prompt": f"""
        {STYLE_BASE}

        A cartoon FISH as a throwing projectile item.
        - Cute stylized fish, bright blue and silver colors
        - Comic book style with motion lines
        - Slightly curved body suggesting it's flying through air
        - Shiny scales with highlights
        - Big cartoonish eye
        - Trail effect or speed lines behind it
        - Centered in frame, medium size
        - Clean white/transparent background style (solid light gray #f0f0f0)
        - Size: 1024x1024 pixels, high detail
        """
    },

    # ========== 狗狗角色 ==========
    {
        "filename": "assets/dog/idle.png",
        "prompt": f"""
        {STYLE_BASE}

        A cute but determined cartoon DOG character in IDLE/STANDING pose.
        - Golden retriever or shiba inu style dog
        - Standing upright on two legs like a mascot character
        - Confident and ready stance, tail wagging
        - Wearing a small blue collar with tag
        - Floppy ears perked up with interest
        - Happy but competitive expression, tongue slightly out
        - Full body visible, centered in frame
        - Clean white/transparent background style (solid light gray #f0f0f0)
        - Size: 1024x1024 pixels, high detail
        """
    },
    {
        "filename": "assets/dog/attack.png",
        "prompt": f"""
        {STYLE_BASE}

        A cute but determined cartoon DOG character in ATTACK/THROWING pose.
        - Same golden/shiba dog with blue collar
        - Dynamic throwing motion, powerful stance
        - Determined fierce expression, showing teeth in a grin
        - Body wound up for a big throw
        - Action lines suggesting powerful movement
        - Ears flying back from motion
        - Full body visible, centered in frame
        - Clean white/transparent background style (solid light gray #f0f0f0)
        - Size: 1024x1024 pixels, high detail
        """
    },
    {
        "filename": "assets/dog/hurt.png",
        "prompt": f"""
        {STYLE_BASE}

        A cute cartoon DOG character in HURT/DAMAGED pose.
        - Same golden/shiba dog with blue collar
        - Pained whimpering expression, teary eyes
        - Stumbling backward from impact
        - Small stars or impact symbols around head
        - Ears drooped down
        - Tail tucked
        - Full body visible, centered in frame
        - Clean white/transparent background style (solid light gray #f0f0f0)
        - Size: 1024x1024 pixels, high detail
        """
    },
    {
        "filename": "assets/dog/projectile.png",
        "prompt": f"""
        {STYLE_BASE}

        A cartoon BONE as a throwing projectile item.
        - Classic dog bone shape, white/cream colored
        - Comic book style with motion lines
        - Slightly spinning through air
        - Shiny clean surface with highlights
        - Cartoonish proportions, chunky ends
        - Trail effect or speed lines behind it
        - Centered in frame, medium size
        - Clean white/transparent background style (solid light gray #f0f0f0)
        - Size: 1024x1024 pixels, high detail
        """
    },

    # ========== 特效 ==========
    {
        "filename": "assets/effects/explosion.png",
        "prompt": f"""
        {STYLE_BASE}

        A cartoon EXPLOSION effect for game impact.
        - Classic comic book "POW" style explosion
        - Bright orange, yellow, and red colors
        - Jagged starburst shape
        - Small debris particles flying outward
        - White hot center fading to orange edges
        - Dynamic and impactful appearance
        - Centered in frame
        - Clean white/transparent background style (solid light gray #f0f0f0)
        - Size: 1024x1024 pixels, high detail
        """
    },
    {
        "filename": "assets/effects/shield.png",
        "prompt": f"""
        {STYLE_BASE}

        A cartoon SHIELD/BARRIER effect for game defense.
        - Translucent glowing energy shield bubble
        - Light blue and cyan colors with white highlights
        - Hexagonal pattern or energy ripples on surface
        - Slight glow effect around edges
        - Semi-transparent appearance
        - Circular/dome shape
        - Sparkles or energy particles around it
        - Centered in frame
        - Clean white/transparent background style (solid light gray #f0f0f0)
        - Size: 1024x1024 pixels, high detail
        """
    },
]


def generate_image(prompt: str, output_path: str) -> bool:
    """使用 Gemini API 生成單張圖片"""
    try:
        print(f"  正在生成: {output_path}")

        # 調用 Gemini API 生成圖片
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=['IMAGE', 'TEXT']
            )
        )

        # 確保輸出目錄存在
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # 保存圖片
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                # 取得圖片數據
                image_data = part.inline_data.data
                mime_type = part.inline_data.mime_type

                # 保存為 PNG
                with open(output_path, 'wb') as f:
                    f.write(image_data)

                print(f"  [OK] Saved: {output_path}")
                return True

        print(f"  [FAIL] No image data received")
        return False

    except Exception as e:
        print(f"  [FAIL] Generation failed: {e}")
        return False


def main():
    """主程式：生成所有遊戲素材"""
    print("=" * 60)
    print("[ART] Gemini 3 Pro Image Game Asset Generator")
    print("=" * 60)
    print(f"Model: {MODEL}")
    print(f"Output: {ASSETS_DIR}")
    print(f"Images to generate: {len(ASSETS_TO_GENERATE)}")
    print("=" * 60)

    success_count = 0
    fail_count = 0

    for i, asset in enumerate(ASSETS_TO_GENERATE, 1):
        print(f"\n[{i}/{len(ASSETS_TO_GENERATE)}] {asset['filename']}")

        output_path = os.path.join(BASE_DIR, asset['filename'])

        if generate_image(asset['prompt'], output_path):
            success_count += 1
        else:
            fail_count += 1

        # API 速率限制：每次請求間隔 2 秒
        if i < len(ASSETS_TO_GENERATE):
            print("  [WAIT] 2 seconds...")
            time.sleep(2)

    print("\n" + "=" * 60)
    print("[STATS] Generation Results")
    print("=" * 60)
    print(f"[OK] Success: {success_count}")
    print(f"[FAIL] Failed: {fail_count}")
    print(f"[DIR] Output: {ASSETS_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()
