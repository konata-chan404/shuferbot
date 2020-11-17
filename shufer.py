import io, imageio  
import requests

def get_gif(product_id: int, fps: int = 10, reverse: bool = False, mode: str = ''):
    gif_bytes = io.BytesIO()
    zero_padding = requests.head(f"https://media.shufersal.co.il/product_images/products_360/{product_id}/files/360_assets/index/images/{str(product_id).zfill(13)}_1.jpg").status_code = 200

    with imageio.get_writer(gif_bytes, format='gif', mode='I', fps=fps) as writer:
        for i in range(40)[::1*(-1 if reverse else 1)]:         
            try:   
                image = imageio.imread(f"https://media.shufersal.co.il/product_images/products_360/{product_id}/files/360_assets/index/images/{str(product_id).zfill(13) if zero_padding else product_id}_{i+1}.jpg"
                        , pilmode = mode)
                writer.append_data(image)
            except:
                return None

    gif_bytes.seek(0)
    return gif_bytes