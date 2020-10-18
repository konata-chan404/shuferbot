import io, imageio  
import http.client

def get_gif(product_id: int, fps: int = 10, reverse: bool = False):
    gif_bytes = io.BytesIO()

    try:
        image = imageio.imread(f"https://media.shufersal.co.il/product_images/products_360/{product_id}/files/360_assets/index/images/{str(product_id).zfill(13)}_{i+1}.jpg")
        zero_padding = False
    except:
        zero_padding = True

    with imageio.get_writer(gif_bytes, format='gif', mode='I', fps=fps) as writer:
        for i in range(40)[::1*(-1 if reverse else 1)]:         
            try:   
                image = imageio.imread(f"https://media.shufersal.co.il/product_images/products_360/{product_id}/files/360_assets/index/images/{str(product_id).zfill(13) if zero_padding else product_id}_{i+1}.jpg")
                writer.append_data(image)
            except:
                return None

    gif_bytes.seek(0)
    return gif_bytes