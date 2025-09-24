import ffmpeg
import os
import math

def split_video_with_multiple_texts(input_video_path, output_folder, segment_duration=89, square_resolution=1080):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    try:
        # Probe the input video to get its duration
        probe = ffmpeg.probe(input_video_path, select_streams='v:0', show_entries='format=duration')
        duration = float(probe['format']['duration'])
    except ffmpeg.Error as e:
        print("Error probing video file:")
        print(e.stderr.decode(errors='replace') if e.stderr else str(e))
        return

    # Calculate the number of segments
    num_segments = math.ceil(duration / segment_duration)

    for i in range(num_segments):
        start_time = i * segment_duration
        movie_title = "Output"
        output_video_path = os.path.join(output_folder, f"{movie_title} Part-{i+1}.mp4")
        try:
            # Split the video, convert to square, and overlay multiple texts
            part_text = f"part-{i+1}"
              # Replace with your desired text
            ffmpeg.input(input_video_path, ss=start_time, t=segment_duration).output(
                output_video_path,
                vf=f'scale={square_resolution}:{square_resolution}:force_original_aspect_ratio=decrease,'
                   f'pad={square_resolution}:{square_resolution}:(ow-iw)/2:(oh-ih)/2,'
                   f'drawtext=fontfile=/path/to/font.ttf:text=\'{part_text}\':fontcolor=white:fontsize=48:x=(w-text_w)/2:y=220,'
                   f'drawtext=fontfile=/path/to/font.ttf:text=\'{movie_title}\':fontcolor=White:fontsize=36:x=(w-text_w)/2:y=850',
                vcodec='libx264',
                acodec='aac',
                preset='ultrafast',
                movflags='faststart'
            ).run()
            print(f"Segment {i+1} saved as {output_video_path}")
        except ffmpeg.Error as e:
            print(f"Error processing segment {i+1}:")
            print(e.stderr.decode(errors='replace') if e.stderr else "No error details available.")

# Example usage
input_video_path = r"C:\Users\balaji\Videos\Movie.mp4"
output_folder = r"C:\Users\balaji\Videos\Aim Lab\output1"

split_video_with_multiple_texts(input_video_path, output_folder)
