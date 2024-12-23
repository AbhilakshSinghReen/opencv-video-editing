from os.path import basename as path_basename, join as path_join

from src.data_loader import get_input_files, outputs_dir


def crop_video_to_rect(video_file_path, output_path, rectangle):
    pass


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
