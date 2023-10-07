import openai
import sys
import os
import math
from pydub import AudioSegment
import time

# ============================================================
# API情報
# ============================================================

openai.organization = ""
openai.api_key      = ""

# 24.5MBの上限
MAX_SIZE = int(24.5 * 1024 * 1024)
MAX_SIZE_IN_SECONDS = 300  # 5 minutes


# ============================================================
# 音声ファイルの文字起こし関数
# ============================================================

def speech_to_text(filepath):
    retries = 3
    while retries:
        try:
            with open(filepath, "rb") as audio_file:
                response = openai.Audio.transcribe(model="whisper-1", file=audio_file)
            return response.text
        except openai.error.APIConnectionError:
            retries -= 1
            if not retries:
                raise
            print(f"Error communicating with OpenAI. Retrying in 10 seconds. {retries} retries left.")
            time.sleep(10)

# ============================================================
# ファイル分割関数
# ============================================================

def split_file(filepath):
    audio = AudioSegment.from_file(filepath, format="mp3")  # ここではMP3を想定していますが、必要に応じて変更してください。
    length_audio = len(audio)
    num_files = math.ceil(length_audio / (MAX_SIZE_IN_SECONDS * 1000))  # pydubでは長さはミリ秒単位で表されます。

    chunk_filepaths = []
    filename_without_extension, extension = os.path.splitext(filepath)
    
    for i in range(num_files):
        start_time = i * MAX_SIZE_IN_SECONDS * 1000
        end_time = (i+1) * MAX_SIZE_IN_SECONDS * 1000
        chunk_audio = audio[start_time:end_time]
        chunk_filepath = f"{filename_without_extension}.part_{i}{extension}"
        chunk_audio.export(chunk_filepath, format="mp3")  # ここでもMP3を想定していますが、必要に応じて変更してください。
        chunk_filepaths.append(chunk_filepath)

    return chunk_filepaths


# ============================================================
# 主要なロジック
# ============================================================

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_audio_file> <output_txt_file>")
        sys.exit(1)

    input_audio_filepath = sys.argv[1]
    output_txt_filepath = sys.argv[2]

    # ファイルを分割
    chunk_filepaths = split_file(input_audio_filepath)
    num_files = len(chunk_filepaths)
    print(f"Total files to process: {num_files}")

    results = []

    # 各ファイルの処理
    for i, chunk_filepath in enumerate(chunk_filepaths, start=1):
        print(f"Processing file {i}/{num_files}...")
        result = speech_to_text(chunk_filepath)
        os.remove(chunk_filepath)
        with open(output_txt_filepath, 'a') as output_file:  # 'a' mode for appending
            output_file.write(result + "\n")

    print(f"Processing completed. Results saved to {output_txt_filepath}.")
