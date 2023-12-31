def process_text_file(file_path):
    processed_lines = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        for i in range(len(lines)):
            line = lines[i].strip()

            if line:
                # Split the line into speaker and response (modify dis one for your own dataset)
                parts = line.split(':')
                if len(parts) > 1:
                    speaker = parts[0].strip()
                    response = parts[1].strip()
                    processed_line = f"{speaker}: {response}"
                    processed_lines.append(processed_line)

    processed_text = '   '.join(processed_lines)
    return processed_text


# Example usage
file_path = 'content.txt'
processed_text = process_text_file(file_path)
print(processed_text)
