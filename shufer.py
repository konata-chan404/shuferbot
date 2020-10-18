import io, imageio


def get_gif(product_id: int, fps: int = 10, reverse: bool = False):
    gif_bytes = io.BytesIO()

    with imageio.get_writer(gif_bytes, format='gif', mode='I', fps=fps) as writer:
        for i in range(40)[::1*(-1 if reverse else 1)]:         
            try:   
                image = imageio.imread(f"https://media.shufersal.co.il/product_images/products_360/{product_id}/files/360_assets/index/images/{product_id}_{i+1}.jpg")
                writer.append_data(image)
            except:
                return None

    gif_bytes.seek(0)
    return gif_bytes