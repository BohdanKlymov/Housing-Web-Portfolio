# Housing-Web-Portfolio
A modern, minimalistic portfolio website created to present myself as a reliable future tenant in Bielefeld, Germany.
The project combines clean design, user-friendly navigation, and interactive features to build trust and transparency for landlords.

## About Me

Starting in summer 2026, I will begin my vocational training as a Software Developer (Fachinformatiker für Anwendungsentwicklung) at symmedia GmbH in Bielefeld, Germany.

This website was created to:

Introduce myself beyond a standard rental application

Present my background, career path, and documents clearly

Offer a modern and professional way to get in contact with me

## Features

Clean & modern UI designed for trust and readability

Tab-based navigation (no long scrolling pages)

Personal introduction and tenant profile

Career path overview (education, training, self-learning)

Document section (CV, certificates, training contract)

Contact information (email, phone, WhatsApp, GitHub)

User registration & private chat (one-to-one messaging)

Multilingual support (German / English)

## Technologies Used
### Frontend:

HTML5

CSS3

JavaScript (Vanilla)

### Backend:

Python (Flask)

SQLite (user accounts & chat messages)

## Design Concept

The design focuses on:

Trustworthiness and clarity

Calm, warm color tones

Minimalistic layout with plenty of whitespace

Professional but approachable appearance

The layout is intentionally kept simple and landlord-friendly while still reflecting my background in software development.

## Project Structure

```
HOUSING-PORTFOLIO/
├── .venv/
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   ├── .gitignore
│   └── pyvenv.cfg
├── app/
│   ├── __pycache__/
│   ├── documents/
│   ├── static/
│   │   ├── images/
│   │   ├── script.js
│   │   └── style.css
│   ├── templates/
│   │   ├── base.html
│   │   ├── chat.html
│   │   ├── index.html
│   │   ├── login.html
│   │   └── register.html
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── routes.py
│   └── translations.py
├── instance/
├── .gitignore
├── create_owner.py
├── LICENSE
├── README.md
└── run.py
```


## Structure Explained

| Path                  | Type          | Description                                             |
| --------------------- | ------------- | ------------------------------------------------------- |
| `.venv/`              | Environment   | Python virtual environment (dependencies & interpreter) |
| `app/`                | Application   | Main Flask application package                          |
| `app/static/`         | Static Assets | CSS, JavaScript, and images                             |
| `app/templates/`      | Templates     | Jinja2 HTML templates                                   |
| `app/models.py`       | Backend       | Database models                                         |
| `app/routes.py`       | Backend       | Application routes / views                              |
| `app/config.py`       | Config        | Application configuration                               |
| `app/translations.py` | Utility       | Language / text handling                                |
| `instance/`           | Instance Data | Runtime config (e.g., secrets, DB)                      |
| `create_owner.py`     | Script        | Initial setup / admin creation                          |
| `run.py`              | Entry Point   | Application launcher                                    |
| `README.md`           | Docs          | Project documentation                                   |
| `LICENSE`             | Legal         | License information                                     |


## Usage

This layout follows common **Flask best practices**, making it easy to:

* Scale the project
* Separate frontend and backend logic
* Maintain clean configuration and deployment

You can directly copy this page into your README or documentation.

## License

This project is personal and created for presentation purposes.
All rights reserved.
