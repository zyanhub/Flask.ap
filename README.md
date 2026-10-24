# Flask Guestbook 📖

A small guestbook web app built with **Flask** and **SQLite**. Visitors can leave a name and a message, and everyone can read the latest messages.

## Features

- Home, About, Form and Guestbook pages
- Messages saved in a SQLite database, newest first
- Input checks: empty or too-long name/message is rejected
- Safe output: HTML typed by users is shown as plain text, not run
- Clean, mobile-friendly design with automatic dark mode

## Tech Stack

- Python
- Flask
- SQLite
- HTML and CSS (Jinja2 templates)

## Run Locally

1. Clone the repository:
   ```
   git clone https://github.com/zyanhub/Flask.ap.git
   cd Flask.ap
   ```
2. Install the requirements:
   ```
   pip install -r requirements.txt
   ```
3. Start the app:
   ```
   python app.py
   ```
4. Open http://127.0.0.1:5000 in your browser.

The database file `guestbook.db` is created automatically on the first run.

## Project Structure

```
Flask.ap/
├── app.py            # Flask routes and validation
├── database.py       # SQLite helper functions
├── requirements.txt  # Python dependencies
└── templates/
    ├── base.html     # Shared layout, menu and styles
    ├── index.html    # Home page
    ├── about.html    # About page
    ├── form.html     # Message form
    └── guestbook.html# List of messages
```

## Known Limitations

- No login, so anyone can post.
- All messages load on one page (no pagination yet).
- No way to delete messages yet.

## Author

Made by [zyanhub](https://github.com/zyanhub)

## License

MIT
