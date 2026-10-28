# 📧 Automated Email Status Reporter

A lightweight Python automation tool that loops through business contacts, generates personalized status updates, attaches corresponding PDF reports, and securely sends them via SMTP.

## 🚀 Features
* **Automated Batching:** Sends targeted status update emails to multiple recipients simultaneously.
* **Dynamic Content:** Customizes messages using Python f-strings based on recipient data and project details.
* **Secure Authentication:** Utilizes `python-dotenv` to keep SMTP credentials hidden via environment variables.
* **File Attachment Handling:** Programmatically reads and attaches PDF reports to each specific email.

## 🛠️ Tech Stack
* **Python** (Core logic, dictionary parsing, file I/O)
* **smtplib & email.message** (Built-in standard library for email dispatching)
* **python-dotenv** (Environment variable management)

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/hasunuhassan/your-repo-name.git](https://github.com/hasunuhassan/automated-email-reporter)
   cd automated-email-reporter