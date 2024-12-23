from os.path import basename as path_basename, join as path_join

import cv2

from src.data_loader import get_input_files, outputs_dir


def crop_video_to_rect(video_file_path, output_path, rectangle):
    video_capture = cv2.VideoCapture(video_file_path)

    if not video_capture.isOpened():
        raise ValueError(f"Cannot open video file: {video_file_path}")

    # Extract the rectangle coordinates and size
    x_min = rectangle['x_min']
    y_min = rectangle['y_min']
    x_max = rectangle['x_max']
    y_max = rectangle['y_max']
    width = x_max - x_min
    height = y_max - y_min

    # Get the original video properties
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use MP4 codec
    frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Ensure the cropping rectangle is within video bounds
    if x_min < 0 or y_min < 0 or x_max > frame_width or y_max > frame_height:
        raise ValueError("Cropping rectangle is out of video bounds.")

    # Create the video writer for the output
    video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        # Crop the frame to the specified rectangle
        cropped_frame = frame[y_min:y_max, x_min:x_max]

        # Write the cropped frame to the output video
        video_writer.write(cropped_frame)

    # Release resources
    video_capture.release()
    video_writer.release()


def main():
    print("Input Rectangle:")
    x_min = int(input("    x_min: ").strip())
    y_min = int(input("    y_min: ").strip())
    x_max = int(input("    x_max: ").strip())
    y_max = int(input("    y_max: ").strip())

    rectangle = {
        'x_min': x_min,
        'y_min': y_min,
        'x_max': x_max,
        'y_max': y_max,
    }

    input_files = get_input_files()
    for input_file in input_files:
        output_file_path = path_join(outputs_dir, path_basename(input_file))
        crop_video_to_rect(input_file, output_file_path, rectangle)


if __name__ == "__main__":
    main()
