import colorgram


def extract_colors(image_path, num_colors):
    rgb_colors = []
    colors = colorgram.extract(image_path, num_colors)
    for color in colors:
        # Extract RGB values and convert to tuple
        rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
    return rgb_colors


def main():
    rgb_color_list = extract_colors("hirst\\image.jpg", 30)
    print(rgb_color_list)  # Print the extracted colors


if __name__ == "__main__":
    main()
