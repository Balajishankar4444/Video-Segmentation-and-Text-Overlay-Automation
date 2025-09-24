# Video Segmentation and Text Overlay Automation

## Overview
This project is a **Python-based tool for automating video segmentation, rendering, and text overlay** using [FFmpeg](https://ffmpeg.org/). It allows you to split long videos into smaller segments, convert them to square resolution, and overlay multiple custom texts (e.g., part numbers and movie titles) on each segment.  

It is designed to **reduce manual effort** and optimize workflows for video processing, rendering, and formatting, making it suitable for **content creation, social media publishing, or testing video processing algorithms**.

---

## Features
- Split long videos into **custom-length segments**.  
- Convert videos to **square resolution** while maintaining aspect ratio.  
- Overlay **dynamic texts** such as part numbers and movie titles.  
- Automatic **encoding and compression** using `libx264` for video and `aac` for audio.  
- Handles **video rendering, format conversion, and padding** for consistent output.  
- Robust error handling for smooth batch processing.  

---

## Technologies Used
- **Python 3** – scripting and automation.  
- **FFmpeg** – video processing, rendering, encoding, and format conversion.  
- **OpenCV** (optional) – for video frame handling if needed.  
- **Automation** – processing large video files efficiently with minimal manual intervention.
