import base64
from typing import Optional
from io import BytesIO

from httpx import AsyncClient
from PIL import Image


async def download_and_convert_image(image_url: str) -> Optional[str]:
    """
    Download an image from URL and convert it to base64.

    Args:
        image_url (str): URL of the image to download

    Returns:
        Optional[str]: Base64 encoded image string or None if failed
    """
    async with AsyncClient() as client:
        # Download the image
        response = await client.get(image_url)
        response.raise_for_status()

        # Open image with PIL
        image = Image.open(BytesIO(response.content))

        # Detect original format, fallback to JPEG if unknown
        original_format = image.format or "JPEG"

        # Handle format-specific conversions
        if original_format == "JPEG" and image.mode in ("RGBA", "LA", "P"):
            # JPEG doesn't support transparency, convert to RGB
            background = Image.new("RGB", image.size, (255, 255, 255))
            if image.mode == "P":
                image = image.convert("RGBA")
            background.paste(
                image, mask=image.split()[-1] if image.mode == "RGBA" else None
            )
            image = background
        elif original_format not in ["JPEG", "PNG", "GIF", "WEBP"]:
            # For unsupported formats, convert to PNG (most compatible)
            original_format = "PNG"

        # Convert to base64
        buffer = BytesIO()
        image.save(buffer, format=original_format, optimize=True)
        buffer.seek(0)

        base64_string = base64.b64encode(buffer.getvalue()).decode("utf-8")

        # Return with correct MIME type
        mime_types = {
            "JPEG": "image/jpeg",
            "PNG": "image/png",
            "GIF": "image/gif",
            "WEBP": "image/webp",
        }
        mime_type = mime_types.get(original_format, "image/jpeg")

        return f"data:{mime_type};base64,{base64_string}"
