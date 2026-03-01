"""
Image Processing Module for CartoonifyAI
Implements multiple cartoon styles with optimized processing
"""

import cv2
import numpy as np
from PIL import Image


class ImageProcessor:
    """Handle all image processing operations"""
    
    @staticmethod
    def preprocess_image(image, max_size=1024):
        """
        Preprocess image for optimal processing
        - Resize if too large
        - Ensure proper format
        """
        img = np.array(image)
        
        # Convert RGBA to RGB if needed
        if img.shape[2] == 4:
            img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
        
        # Resize if image is too large
        height, width = img.shape[:2]
        if max(height, width) > max_size:
            scale = max_size / max(height, width)
            new_width = int(width * scale)
            new_height = int(height * scale)
            img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
        
        return img
    
    @staticmethod
    def classic_cartoon(image, edge_strength=9, color_smoothing=9, color_levels=9):
        """
        Classic Cartoon Style
        - Strong edges with bilateral filtering
        - Color quantization for cartoon effect
        """
        img = np.array(image)
        
        # Convert to grayscale for edge detection
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        
        # Apply median blur to reduce noise
        gray_blur = cv2.medianBlur(gray, 7)
        
        # Detect edges using adaptive thresholding
        edges = cv2.adaptiveThreshold(
            gray_blur,
            255,
            cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY,
            edge_strength,
            9
        )
        
        # Apply bilateral filter for color smoothing while preserving edges
        color = cv2.bilateralFilter(img, color_smoothing, 250, 250)
        
        # Color quantization for cartoon effect
        data = np.float32(color).reshape((-1, 3))
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
        _, labels, centers = cv2.kmeans(data, color_levels, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        centers = np.uint8(centers)
        quantized = centers[labels.flatten()].reshape(color.shape)
        
        # Combine edges with quantized colors
        cartoon = cv2.bitwise_and(quantized, quantized, mask=edges)
        
        return cartoon
    
    @staticmethod
    def sketch_style(image, blur_value=21, sigma_s=60, sigma_r=0.07):
        """
        Sketch Style
        - Pencil sketch effect
        - Black and white with detailed edges
        """
        img = np.array(image)
        
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        
        # Invert the grayscale image
        inverted = 255 - gray
        
        # Apply Gaussian blur
        blurred = cv2.GaussianBlur(inverted, (blur_value, blur_value), 0)
        
        # Invert the blurred image
        inverted_blur = 255 - blurred
        
        # Create sketch by dividing grayscale by inverted blur
        sketch = cv2.divide(gray, inverted_blur, scale=256.0)
        
        # Convert back to RGB for consistency
        sketch_rgb = cv2.cvtColor(sketch, cv2.COLOR_GRAY2RGB)
        
        return sketch_rgb
    
    @staticmethod
    def pencil_color(image, sigma_s=60, sigma_r=0.07, shade_factor=0.02):
        """
        Pencil Color Style
        - Colored pencil sketch effect
        - Maintains colors with sketch-like edges
        """
        img = np.array(image)
        
        # Apply pencil sketch effect (color version)
        sketch_gray, sketch_color = cv2.pencilSketch(
            img,
            sigma_s=sigma_s,
            sigma_r=sigma_r,
            shade_factor=shade_factor
        )
        
        return sketch_color
    
    @staticmethod
    def watercolor_style(image, blur_value=15, edge_strength=7):
        """
        Watercolor Style
        - Soft, painted look
        - Blurred edges with color bleeding effect
        """
        img = np.array(image)
        
        # Apply bilateral filter multiple times for watercolor effect
        watercolor = img.copy()
        for _ in range(3):
            watercolor = cv2.bilateralFilter(watercolor, 9, 75, 75)
        
        # Detect edges
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        edges = cv2.dilate(edges, None)
        edges = cv2.GaussianBlur(edges, (5, 5), 0)
        
        # Create edge mask
        edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
        
        # Blend watercolor with subtle edges
        result = cv2.addWeighted(watercolor, 0.9, edges_colored, 0.1, 0)
        
        return result
    
    @staticmethod
    def oil_painting(image, size=7, dynRatio=1):
        """
        Oil Painting Style
        - Thick brush strokes effect
        - Rich colors
        """
        img = np.array(image)
        
        # Apply oil painting effect
        oil = cv2.xphoto.oilPainting(img, size, dynRatio)
        
        return oil
    
    @staticmethod
    def process_image(image, style="classic", **kwargs):
        """
        Main processing function
        Routes to appropriate style processor
        
        Args:
            image: PIL Image or numpy array
            style: One of ["classic", "sketch", "pencil", "watercolor", "oil"]
            **kwargs: Style-specific parameters
        
        Returns:
            Processed image as numpy array
        """
        # Preprocess image
        img = ImageProcessor.preprocess_image(image)
        
        # Route to appropriate style
        if style == "classic":
            return ImageProcessor.classic_cartoon(
                img,
                edge_strength=kwargs.get('edge_strength', 9),
                color_smoothing=kwargs.get('color_smoothing', 9),
                color_levels=kwargs.get('color_levels', 9)
            )
        elif style == "sketch":
            return ImageProcessor.sketch_style(
                img,
                blur_value=kwargs.get('blur_value', 21),
                sigma_s=kwargs.get('sigma_s', 60),
                sigma_r=kwargs.get('sigma_r', 0.07)
            )
        elif style == "pencil":
            return ImageProcessor.pencil_color(
                img,
                sigma_s=kwargs.get('sigma_s', 60),
                sigma_r=kwargs.get('sigma_r', 0.07),
                shade_factor=kwargs.get('shade_factor', 0.02)
            )
        elif style == "watercolor":
            return ImageProcessor.watercolor_style(
                img,
                blur_value=kwargs.get('blur_value', 15),
                edge_strength=kwargs.get('edge_strength', 7)
            )
        elif style == "oil":
            return ImageProcessor.oil_painting(
                img,
                size=kwargs.get('size', 7),
                dynRatio=kwargs.get('dynRatio', 1)
            )
        else:
            raise ValueError(f"Unknown style: {style}")
    
    @staticmethod
    def create_comparison(original, processed):
        """
        Create side-by-side comparison image
        
        Args:
            original: Original image (PIL or numpy)
            processed: Processed image (numpy array)
        
        Returns:
            Combined image as numpy array
        """
        orig = np.array(original)
        
        # Ensure both images have same height
        if orig.shape[0] != processed.shape[0]:
            scale = orig.shape[0] / processed.shape[0]
            new_width = int(processed.shape[1] * scale)
            processed = cv2.resize(processed, (new_width, orig.shape[0]))
        
        # Concatenate horizontally
        comparison = np.hstack((orig, processed))
        
        return comparison
    
    @staticmethod
    def get_style_info():
        """
        Get information about available styles
        
        Returns:
            Dictionary with style names and descriptions
        """
        return {
            "classic": {
                "name": "Classic Cartoon",
                "description": "Bold edges with smooth colors, like traditional cartoons",
                "icon": "🎨",
                "params": ["edge_strength", "color_smoothing", "color_levels"]
            },
            "sketch": {
                "name": "Pencil Sketch",
                "description": "Black and white sketch with detailed pencil lines",
                "icon": "✏️",
                "params": ["blur_value", "sigma_s", "sigma_r"]
            },
            "pencil": {
                "name": "Colored Pencil",
                "description": "Colored sketch maintaining original hues",
                "icon": "🖍️",
                "params": ["sigma_s", "sigma_r", "shade_factor"]
            },
            "watercolor": {
                "name": "Watercolor",
                "description": "Soft, painted look with blended colors",
                "icon": "🎨",
                "params": ["blur_value", "edge_strength"]
            },
            "oil": {
                "name": "Oil Painting",
                "description": "Thick brush strokes with rich colors",
                "icon": "🖌️",
                "params": ["size", "dynRatio"]
            }
        }
