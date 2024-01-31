import os
import shutil
import argparse


def copy_files(src, dest):
    try:
        for item in os.listdir(src):
            full_path = os.path.join(src, item)

            if os.path.isdir(full_path):
                copy_files(full_path, dest)
            else:
                ext = os.path.splitext(item)[1][1:]
                if ext == '':
                    ext = 'no_extension'

                ext_dir = os.path.join(dest, ext)

                if not os.path.exists(ext_dir):
                    os.makedirs(ext_dir)

                shutil.copy2(full_path, ext_dir)
                print(f"Copied '{full_path}' to '{ext_dir}'")

    except Exception as e:
        print(f"Error processing file {full_path}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Copy files into extension-based directories.")
    parser.add_argument("-s", "--source", help="Source directory path")
    parser.add_argument("-d", "--destination",
                        help="Destination directory path", default="dist")
    args = parser.parse_args()

    if not os.path.exists(args.source):
        raise ValueError(f"Source directory {args.source} does not exist")

    if not os.path.exists(args.destination):
        os.makedirs(args.destination)

    copy_files(args.source, args.destination)


if __name__ == "__main__":
    main()
