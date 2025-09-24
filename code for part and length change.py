import ffmpeg
import os
import math

def split_video_with_multiple_texts(input_video_path, output_folder, start_offset=1980, segment_duration=89, square_resolution=1080, start_part=37):
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

    # Calculate the number of segments starting from the offset
    remaining_duration = max(0, duration - start_offset)
    num_segments = math.ceil(remaining_duration / segment_duration)

    for i in range(num_segments):
        start_time = start_offset + i * segment_duration
        part_number = start_part + i
        movie_title = "Kannum Kannum Kollaiyadithaal (2020)"
        output_video_path = os.path.join(output_folder, f"{movie_title} Part - {part_number}.mp4")
        try:
            # Split the video, convert to square, and overlay multiple texts
            part_text = f"Part - {part_number}"
            ffmpeg.input(input_video_path, ss=start_time, t=segment_duration).output(
                output_video_path,
                vf=f'scale={square_resolution}:{square_resolution}:force_original_aspect_ratio=decrease,'
                   f'pad={square_resolution}:{square_resolution}:(ow-iw)/2:(oh-ih)/2,'
                   f'drawtext=fontfile=/path/to/font.ttf:text=\'{part_text}\':fontcolor=white:fontsize=54:x=(w-text_w)/2:y=220,'
                   f'drawtext=fontfile=/path/to/font.ttf:text=\'{movie_title}\':fontcolor=White:fontsize=54:x=(w-text_w)/2:y=850',
                vcodec='libx264',
                acodec='aac',
                preset='ultrafast',
                movflags='faststart'
            ).run()
            print(f"Segment {part_number} saved as {output_video_path}")
        except ffmpeg.Error as e:
            print(f"Error processing segment {part_number}:")
            print(e.stderr.decode(errors='replace') if e.stderr else "No error details available.")

# Example usage
input_video_path = r"C:\Users\balaji\Videos\movies\Kannum Kannum Kollaiyadithaal (2020) full movie Tamil.mp4"
output_folder = r"C:\Users\balaji\Videos\tes"

split_video_with_multiple_texts(input_video_path, output_folder)
