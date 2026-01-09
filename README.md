# Prerequisites

- Python 3.x installed
- OpenAI API key

# Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/ryderthieu/help-chatbot.git
cd help-chatbot
```

2. **Configure environment variables**

- Copy `.env.sample` to `.env` and add your `OPENAI API KEY`

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the scraper-uploader**

```bash
python main.py
```

# Workflow

1. **Check Vector Store**

   - Kiểm tra `vector_store_id` trong `state.json`.
   - Nếu chưa tồn tại hoặc không hợp lệ → tạo mới.

2. **Process Articles**

   - Tải articles và so sánh hash với state.
   - Xác định trạng thái: **ADDED**, **UPDATED**, **SKIPPED**.
   - Chỉ upload các file **ADDED** hoặc **UPDATED**.
   - Nếu **UPDATED**, xóa file cũ trước khi upload file mới.

3. **Update State**
   - Cập nhật `state.json` để lần chạy sau có thể detect delta.
   - In ra số lượng: `ADDED`, `UPDATED`, `SKIPPED`.

**Note:**

- Articles được lưu trong `articles/` dưới dạng file markdown.
- `state.json` sẽ tự động tạo trong `tracker/state.json` nếu chưa có.
- When uploading files, the default OpenAI chunking strategy will be used.

# Assitant testing in playground

<img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/0b866901-f87f-477f-aab1-ed646f7a8a52" />

# Deploy Scraper as Daily Job

I have deployed the application via Docker Hub to DigitalOcean Droplet. Logs are automatically saved and accessible through a public link. I have scheduled the job to run daily at 10:30 UTC (17:30 Vietnam time).

You can see log file in [here](https://help-chatbot-log.sfo3.digitaloceanspaces.com/program.log)
