## AudioTranscriber

### Overview
AudioTranscriber is a tool that helps you convert large audio files into text using OpenAI's Whisper API. It manages large files by splitting them into smaller chunks that fit the API's limitations.

### Installation
1. Clone the repository:
```
git clone <repository_url>
```
2. Navigate to the repository folder:
```
cd <repository_folder>
```
3. Install the required packages:
```
pip install -r requirements.txt
```

### Usage
To transcribe your audio files into text:
```
python main.py <input_audio_file> <output_txt_file>
```

### Notes
- This tool currently supports MP3 format for the input audio file. You may need to adjust the code if you have a different file format.
- Ensure you have set up the OpenAI API credentials in the code before running.

### License
MIT License

---

## AudioTranscriber（日本語）

### 概要
AudioTranscriberは、OpenAIのWhisper APIを使用して大きなオーディオファイルをテキストに変換するツールです。APIの制限に合わせてオーディオを小さなチャンクに分割して大きなファイルを管理します。

### インストール方法
1. リポジトリをクローンします:
```
git clone <repository_url>
```
2. リポジトリのフォルダに移動します:
```
cd <repository_folder>
```
3. 必要なパッケージをインストールします:
```
pip install -r requirements.txt
```

### 使い方
オーディオファイルをテキストに変換するには:
```
python main.py <input_audio_file> <output_txt_file>
```

### 注意点
- このツールは現在、入力オーディオファイルのMP3フォーマットをサポートしています。異なるファイル形式の場合は、コードを調整する必要があります。
- 実行する前にコードの中でOpenAI APIの資格情報を設定してください。

### ライセンス
MITライセンス

---
