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

   - Check the `vector_store_id` in `state.json`.
   - If it does not exist or is invalid → create a new one.

2. **Process Articles**

   - Download articles and compare their hashes with the state.
   - Determine the status: **ADDED**, **UPDATED**, **SKIPPED**.
   - Only upload files that are **ADDED** or **UPDATED**.
   - If **UPDATED**, delete the old file before uploading the new one.

3. **Update State**
   - Update `state.json` so the next run can detect deltas.
   - Print the counts: `ADDED`, `UPDATED`, `SKIPPED`.

**Note:**

- Articles are stored in the `articles/` directory as markdown files.
- `state.json` will be automatically created in `tracker/state.json` if it does not exist.
- When uploading files, the default OpenAI chunking strategy will be used.

# Assitant testing in playground

<img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/0b866901-f87f-477f-aab1-ed646f7a8a52" />

# Deploy Scraper as Daily Job

I have deployed the application via Docker Hub to DigitalOcean Droplet. Logs are automatically saved and accessible through a public link. I have scheduled the job to run daily at 10:30 UTC (17:30 Vietnam time).

You can see log file in [here](https://help-chatbot-log.sfo3.digitaloceanspaces.com/program.log)
