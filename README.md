# Flask Web App

A simple and clean Flask web application template with a modern structure. This application serves as a starting point for building web applications with Flask, featuring organized static assets, templates, and a basic home page.

## Features

- Clean and responsive web interface
- Organized project structure with separate directories for templates and static files
- CSS styling and JavaScript functionality
- Ready for development and production deployment

## Project Structure

```
FlaskWebApp/
├── app.py              # Main Flask application
├── templates/          # HTML templates
│   └── index.html     # Home page template
├── static/            # Static assets
│   ├── css/
│   │   └── style.css  # Stylesheet
│   └── js/
│       └── script.js  # JavaScript functionality
├── requirements.txt   # Python dependencies
├── vercel.json        # Vercel deployment configuration
├── LICENSE           # MIT License
└── README.md         # This file
```

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd FlaskWebApp
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Development Mode

To run the application in development mode with debug enabled:
```bash
python app.py
```

The application will be accessible at `http://127.0.0.1:5000/`.

### Production Mode

For production deployment, you can use Gunicorn:
```bash
gunicorn app:app
```

This will run the application on `http://127.0.0.1:8000/` by default.

### Vercel Deployment

This application is configured for easy deployment on Vercel:

1. Install the Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Deploy to Vercel:
   ```bash
   vercel
   ```

The `vercel.json` file is already configured to handle the Flask application routing and build process.

## Dependencies

The application uses the following main dependencies:
- **Flask 2.2.2** - Web framework
- **Jinja2 3.1.2** - Template engine
- **Werkzeug 2.2.2** - WSGI utility library
- **Gunicorn 20.1.0** - Production WSGI server

## Development

### File Structure Explanation
- `app.py` - Main application file containing Flask routes
- `templates/` - Contains HTML templates using Jinja2 templating
- `static/` - Static files (CSS, JavaScript, images)
- `requirements.txt` - Python package dependencies

### Customization
- Modify `templates/index.html` to change the home page content
- Update `static/css/style.css` for styling changes
- Add JavaScript functionality in `static/js/script.js`
- Define new routes in `app.py` for additional pages

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.